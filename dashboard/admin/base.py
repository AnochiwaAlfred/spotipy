
from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest
from users.models import *
from audio.models import *
from dashboard.forms.authenticator import CustomUserAuth


SITE_FOLDER_NAME = 'spotipy'


class Dashboard(admin.AdminSite):
    site_title="Spotipy"
    site_header="Spotipy Dashboard"
    site_url = '/api/v1/docs'
    index_title = "Super Admin"
    # name = "Spotipy Admin"
    login_template = f"{SITE_FOLDER_NAME}/admin/login.html"
    logout_template = f"{SITE_FOLDER_NAME}/registration/logged_out.html"
    index_template = f"{SITE_FOLDER_NAME}/admin/index.html"
    app_index_template = f"{SITE_FOLDER_NAME}/admin/app_index.html"
    login_form = CustomUserAuth
    # password_change_done_template = f"{SITE_FOLDER_NAME}/registration/password_change_done.html"
    # password_change_template = f"{SITE_FOLDER_NAME}/admin/auth/user/change_password.html"
   
    
    def each_context(self, request):
        context = super().each_context(request)
        app_list = self.get_app_list(request)
        
        if  context is not None:
            context['adminsite'] = self.name
            context['app_lists'] = app_list
            context['title'] = self.site_title
            context['index_title'] = self.index_title
            context['site_header'] = self.site_header
        # Add additional context variables if needed
        return context

    

DASHBOARD = Dashboard(name='spotipy')


