from ninja import Router, Schema
from decouple import config
from ninja import NinjaAPI, Form
from ninja.security import HttpBearer
from users.models import *
from schemas.auth import *
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth import authenticate
from plugins.hasher import hasherGenerator, decrypter
import json
from plugins.sms_token import token_verify, send_sms, send_token_via_sms
from django.conf import settings
from django.core.mail import send_mail
import pyotp
from datetime import datetime, timedelta, timezone
from typing import List, Union

router = Router(tags=["Authentication"])


@router.get("/")
def get_user(request):
    auth = request.auth

    user = CustomUser.objects.all().filter(token=auth).get()
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "code": user.code,
    }


@router.post("/token", auth=None)  # < overriding global auth
def get_token(request, username: str = Form(...), password: str = Form(...)):
    """
    This will be used as signup request.
    """
    user = authenticate(username=username, password=password)
    if user:
        hh = hasherGenerator()
        string_formatted = hh.get("token").decode("utf-8")
        hh.update(
            {
                # "rsa_duration": 24,
                "token": string_formatted
            }
        )

        CustomUser.objects.all().filter(id=user.id).update(**hh)

        return {"token": hh.get("token")}

    else:
        return {"token": False}
        # User is authenticated


@router.post("/register/", auth=None)
def register_user(
    request,
    password: str,
    passwordConfirm: str,
    user_data: AuthUserRegistrationSchema = Form(...),
):
    user = CustomUser.objects.create(**user_data.dict())
    if password==passwordConfirm:
        user.set_password(password)
        user.save()

    # Generate OTP
    totp = pyotp.TOTP(pyotp.random_base32())
    user.otp = totp.now()
    user.otp_created_at = datetime.now()
    user.save()

    # Send OTP to the user via email
    send_otp_email2(user)

    return {"message": "Registration successful. Check your email for OTP."}


def send_otp_email(user):
    subject = "Your OTP for Email Verification"
    message = f"Your OTP is: {user.otp}"
    from_email = "anochiwaalfred@gmail.com"  # Change this to your sending email
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)


def send_otp_email2(user):
    import smtplib, ssl
    from email.message import EmailMessage

    email_address = config('SMTP_EMAIL')
    email_password = config('SMTP_PASSWORD')
    port = 465  # This is the default SSL port

    # create email
    msg = EmailMessage()
    msg["Subject"] = "Your OTP for Email Verification"
    msg["From"] = email_address
    msg["To"] = user.email
    msg.set_content(f"Your OTP is: {user.otp}")

    # send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(email_address, email_password)
        server.send_message(msg)


@router.post("/verify-otp/", auth=None)
def verify_otp(request, email: str, otp: str):
    user = CustomUser.objects.get(email=email)
    # totp = pyotp.TOTP(user.otp)

    user_otp_created_at = user.otp_created_at
    utc_otp_created_at = user_otp_created_at.replace(tzinfo=timezone.utc)
    
    if utc_otp_created_at < datetime.now(timezone.utc) - timedelta(minutes=5):
        return {"message": "OTP has expired. Please request a new one."}
    else:
    # if totp.verify(otp):
        if otp==user.otp:
            user.is_verified = True
            user.is_active = True
            user.save()
            return {"message": "Email verification successful."}
        else:
            return {"message": "Invalid OTP. Please try again."}
    
@router.post("/resend-otp/", auth=None)
def resend_otp(request, email: str):
    user = CustomUser.objects.get(email=email)
    send_otp_email2(user)

    return {"message": "OTP Sent. Check your email for OTP"}




# @router.post("/requestForgotPassword/{email}", auth=None)
# def requestforgotpassword(request, email:str):
#     meta =  request.META
#     user = CustomUser.objects.all()

#     if user.filter(email=email).exists():
#         user = CustomUser.objects.all().filter(email=email).get()
#         resetLink =  f"{meta.get('wsgi.url_scheme')}://{meta.get('HTTP_HOST')}/api/v1/auth/resetForgotPassword/{email}/"

#         user.token = numbershuffler() # this a plugin for generating digit code.
#         user.save()
#         # on production check
#         recipent_list =  f"{email}" if config('ENVIRONMENT') == "production" else "anointedngeorge@gmail.com"
#         em = sendUserEmail(
#             recipient_list=recipent_list,
#             subject='Password Reset',
#             context={
#                     'email': email,
#                     'message_date':timezone.now(),
#                     'resetLink':resetLink,
#                     'token':user.token
#                 },
#                 template='forgot_password_reset.html'
#             )
#         return em
#     else:
#         return "Email Does not exist."


# @router.post("/resetForgotPassword/{email}/", auth=None)
# def reset_forgot_password(request, email:str, data:AuthResetPassword=Form(...)):
#     fmData = data.dict()
#     user = CustomUser.objects.all()
#     # will check if token exists
#     if user.filter(email=email).exists(): # true or false

#         if user.filter(token=fmData.token).exists(): # true or false
#             if fmData.new_password == fmData.repeat_password:
#                 user.filter(email=email).get()
#                 user.set_password(fmData.new_password) # set the new password
#                 user.isPassRequest = False # reset password request to false
#                 user.token = "" # reset token to ""
#                 user.save() # save
#                 em = sendUserEmail(
#                     recipient_list=f"{email}",
#                     subject='Password Reset',
#                     context={
#                             'email': email,
#                             'message_date':timezone.now(),
#                         },
#                         template='password_confirmation.html'
#                     )
#                 return {"message":"Password successfully changed."}

#             else:return {"message":"Password does not match."}

#         else:return {"message":"Token does not match."}

#     else:return {"message":"User does not match."}


@router.post("/logout")
def logout(request):
    auth = request.auth
    user = CustomUser.objects.all().filter(token=auth)
    user.update(**{"token": "", "key": ""})
    return {
        "message": "User Logged Out; You can sign in again using your username and password."
    }


@router.post("createSuperUser", response=AuthUserRetrievalSchema)
def createSuperUser(
    request, password: str, data: AuthUserRegistrationSchema = Form(...)
):
    authuser = CustomUser.objects.create(**data.dict())
    if authuser:
        authuser.set_password(password)
        authuser.is_active = True
        authuser.is_staff = True
        authuser.is_superuser = True
        authuser.save()
    return authuser


@router.get("/getAllUsers", response=List[AuthUserRetrievalSchema])
def getAllUsers(request):
    users = CustomUser.objects.all()
    return users


User = get_user_model()


@router.post("/login/")
def login_user(request, data: UserLoginSchema = Form(...)):
    user = authenticate(request, username=data.email, password=data.password)

    if user is not None:
        user2 = CustomUser.objects.get(email=data.email)
        if user2.is_verified == True:
            login(request, user)
            return {"detail": "User logged in successfully"}
        else:
            return {"detail": "User not verified"}

    return {"detail": "Invalid credentials"}


@router.delete("/deleteUser/{user_id}")
def delete_user(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    user.delete()
    return f"User {user.username} deleted successfully"
