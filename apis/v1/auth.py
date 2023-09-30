from ninja import Router
from decouple import config
from ninja import NinjaAPI, Form
from ninja.security import HttpBearer
from users.models import *
from schemas.auth import *
# from django.contrib.auth import authenticate
# from plugins.hasher import hasherGenerator, decrypter
# import json
# from plugins.sms_token import token_verify, send_sms, send_token_via_sms
# from django.conf import settings

# from alpha_logistics.schemas.auth import AuthResetPassword
# from typing import List, Union

# from plugins.email_token import sendUserEmail
# from plugins.hasher import numbershuffler

router = Router(tags=["Authentication"])


# @router.get("/")
# def get_user(request):
#     auth = request.auth
    
#     user = CustomUser.objects.all().filter(encoded=auth).get()
#     return {
#         "id": user.id,
#         "username": user.username,
#         "email": user.email,
#         "code": user.code,
#     }


# @router.post("/token", auth=None)  # < overriding global auth
# def get_token(request, username: str = Form(...), password: str = Form(...)):
#     """
#     This will be used as signup request.
#     """
#     user = authenticate(username=username, password=password)
#     if user:
#         hh = hasherGenerator()
#         string_formatted = hh.get("encoded").decode("utf-8")
#         hh.update({"rsa_duration": 24, "encoded": string_formatted})

#         CustomUser.objects.all().filter(id=user.id).update(**hh)

#         return {"token": hh.get("encoded")}
    
#     else:
#         return {"token": False}
#         # User is authenticated


# # anochiwaalfred@gmail.com
# # Alfieolli
# @router.get("/verify-token/{otp}", auth=None)  # < overriding global auth
# def verify_token_code(request, otp: str):
#     """
#     Use method to verify otp code sent via sms and email
#     """
#     user = CustomUser.objects.all()
#     if user.filter(token=otp).exists():
#         user = user.filter(token=otp).get()
#         pinid = user.token_pin_id
#         d = token_verify(pin_id=pinid, token=otp)
#         if d.get("verified"):
#             user.is_token_verified = True
#             user.token_pin_id = ""
#             user.token = ""
#             user.save()
#         return {"message": "Verified"}
#     else:
#         return {"message": "Failed"}





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




# @router.post("/logout")
# def logout(request):
#     auth = request.auth
#     user = CustomUser.objects.all().filter(encoded=auth)
#     user.update(**{"encoded": "", "key": "", "message": "", "rsa_duration": 0})
#     return {
#         "message": "User Logged Out; You can sign in again using your username and password."
#     }

@router.post('createSuperUser', response=AuthUserRetrievalSchema)
def createSuperUser(request, data:AuthUserRegistrationSchema, password:str):
    authuser = CustomUser.objects.create(**data.dict())
    if authuser:
        authuser.set_password(password)
        authuser.is_active=True
        authuser.is_staff=True
        authuser.is_superuser=True
        authuser.save()
    return authuser