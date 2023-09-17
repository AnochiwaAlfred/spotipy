
from ninja import NinjaAPI, Router
from ninja.security import django_auth
from ninja.security import HttpBearer
from django.http import HttpResponseForbidden
from users.models import CustomUser
from django.http import HttpResponseForbidden, response
from http import HTTPStatus
from decouple import config 
from apis.v1.tracks import router as tracks_router
from apis.v1.albums import router as albums_router

# from plugins.email_token import sendUserEmail
from django.utils import timezone


# class GlobalAuth(HttpBearer):
#     def authenticate(self, request, token):
#         # meta = request.META
#         # HTTP_USER_AGENT = meta.get('HTTP_USER_AGENT')
#         # # user =  User.objects.all().filter(encoded=token,is_token_verified=True)
#         # user = CustomUser.objects.all().filter(encoded=token, isPassRequest=False)
#         # if user.exists():
#         #     foundUser = user.get()
#         #     # on production check
#         #     recipent_list =  f"{foundUser.email}" if config('ENVIRONMENT') == "production" else "anointedngeorge@gmail.com"
            
#         #     sendUserEmail(
#         #         recipient_list=recipent_list,
#         #         subject=f'Login Notification <{foundUser.email}>',
#         #         context={
#         #                 'email': foundUser.email,
#         #                 'message_date':timezone.now(),
#         #                 "agent":str(HTTP_USER_AGENT),
#         #             },
#         #             template='login_template.html'
#         #     )

#         #     return foundUser.encoded
#             return True
#     def on_auth_fail(self, response):
#         return HttpResponseForbidden("Failed to authenticate! or maybe you requested for a password change.")
    

# authenticator =  GlobalAuth() if config('ENVIRONMENT') == 'production' else None
api = NinjaAPI(
    auth=None,
    title="Spotipy",
    description="This is an API with dynamic OpenAPI info section",
)

# let this be the first one.
# api.add_router("/auth/", auth_router)
# -----------------------------------------
api.add_router("/tracks/", tracks_router)
api.add_router("/albums/", albums_router)



os_router = Router(tags=["OS Endpoints"])


class SuperAuth(HttpBearer):
    def authenticate(self, request, token):
        # user =  User.objects.all().filter(encoded=token,is_token_verified=True)
        user = CustomUser.objects.all().filter(encoded=token)
        if user.exists() and user[0].is_superuser == True:
            foundUser = user.get()
            return foundUser.encoded


super_authenticator = SuperAuth() if config("ENVIRONMENT") == "production" else None


@os_router.delete("/deleteMigrations", auth=super_authenticator)
def delete_migrations(request):
    from spotipy.settings import BASE_DIR
    import os, json, shutil

    BASE_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir))

    dir_list = os.listdir(BASE_DIR)
    dir_list2 = [os.path.join(BASE_DIR, x) for x in dir_list if "." not in x]
    message = "No migration to delete"
    for item in dir_list2:
        if os.path.isdir(item):
            for dir in os.listdir(item):
                if dir == "migrations":
                    # migrationList.append(os.path.join(BASE_DIR, item, dir))
                    try:
                        shutil.rmtree(os.path.join(BASE_DIR, item, dir))
                        message = "Migrations Deleted"
                    except OSError as e:
                        message = f"Error: {e}"
    return message


@os_router.delete("/deletePyCache", auth=super_authenticator)
def delete_pycache_folders(request):
    from spotipy.settings import BASE_DIR
    import os, shutil

    BASE_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir))
    for root, dirs, files in os.walk(BASE_DIR):
        for dir in dirs:
            if dir == "__pycache__":
                folder_path = os.path.join(root, dir)
                shutil.rmtree(folder_path)
                # print(f"Deleted {folder_path}")
    return f"Deleted All Pycache"


def addRouterCheck():
    if config("ENVIRONMENT") == "development":
        api.add_router("/os/", os_router)


addRouterCheck()
