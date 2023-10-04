from ninja import Router
from social_django.utils import psa
from social_core.exceptions import AuthException
from django.contrib.sessions.models import Session
from django.shortcuts import redirect
from django.http import HttpResponse
import secrets
import datetime
from users.models import *
from decouple import config



router = Router(tags=['Client Authentication'])



# Step 3: Create an API Endpoint for Google Authentication
backend_name = 'google-oauth2'
CLIENT_ID = config('GOOGLE_OAUTH2_CLIENT_ID')
BACKEND_BASE_URL = config('BACKEND_BASE_URL')
REDIRECT_URI = f'{BACKEND_BASE_URL}api/v1/clientauth/google/callback/'


def generate_and_store_state_token(request):
    # Generate a random state_token
    state_token = secrets.token_urlsafe(32)  # Generates a random URL-safe token

    # Store the state_token in the user's session along with a timestamp
    request.session['state_token'] = state_token
    request.session['state_token_timestamp'] = datetime.datetime.now()

    # Redirect the user to the OAuth2 provider's authentication page
    # Include the state_token as a parameter in the authentication request
    auth_url = f'https://oauth2-provider.com/auth?state={state_token}&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}'
    return redirect(auth_url)

@router.get("/google/auth/")
@psa(backend_name)
def google_authenticate(request, backend):
    """
    Initiates Google OAuth authentication.
    """
    print(backend)
    return generate_and_store_state_token(request)

# Step 4: Handle Google OAuth Callback
@router.get("/google/callback/")
@psa(backend_name)
def google_auth_callback(request, backend=None):
    """
    Handles the callback from Google OAuth.
    """
    try:
        # Validate the state token (replace with actual validation logic)
        state_token = request.query_params.get('state')
        stored_state_token = request.session.get('state_token')
        if state_token != stored_state_token:
            raise AuthException(backend, 'State token validation failed')

        # Authenticate the user and get user data
        user = request.backend.do_auth(request.GET.get('access_token'))

        # Step 5: Exchange Authorization Code for Access Token (use dummy access token)
        access_token = 'dummy_access_token'

        if user:
            # Step 6: Fetch User Information from Google (use dummy user data)
            user_data = {
                "email": user.email,
                "username": user.username,
                "profile_picture": user.profile_picture_url,  # Replace with the actual field name for the profile picture
            }
            
            return user
        return "User doesn't exist"

            # # Step 7: Create User Account or Log In
            # # Check if the user already exists based on email (use dummy email check)
            # existing_user = CustomUser.objects.filter(email=user_data["email"]).first()

            # if not existing_user:
            #     # Create a new user account with fetched user data
            #     new_user = Client.objects.create(
            #         username=user_data["username"],
            #         email=user_data["email"],
            #     )
            #     new_user.save()
            # else:
            #     # Log in the existing user
            #     new_user = existing_user

            # # Step 8: Generate JWT (use dummy JWT generation)
            # jwt_token = 'dummy_jwt_token'

            # # Step 9: Return JWT to the Frontend
            # return Response({"jwt_token": jwt_token})

    except AuthException as auth_exception:
        # Handle authentication exceptions
        return {"error": str(auth_exception), 'status':401}



