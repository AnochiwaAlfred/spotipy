from django.contrib import admin
from dashboard.admin.base import DASHBOARD
from audio.models import *
from users.models import *
from dashboard.admin.base import SITE_FOLDER_NAME




class _AlbumAdmin(admin.ModelAdmin):
    change_list_template = f"{SITE_FOLDER_NAME}/admin/change_list.html" 
    change_form_template = f"{SITE_FOLDER_NAME}/admin/change_form.html" 
    list_display = ALBUM_LIST_DISPLAY
    pass

# add_form_template
# change_form_template
# change_list_template
# delete_confirmation_template
# delete_selected_confirmation_template
# object_history_template
# popup_response_template

# change_form_template
# change_form_object_tools
class _GenreAdmin(admin.ModelAdmin):
    change_list_template = f"{SITE_FOLDER_NAME}/admin/change_list.html" 
    change_form_template = f"{SITE_FOLDER_NAME}/admin/change_form.html" 
    
    
    list_display = GENRE_LIST_DISPLAY
    


class _LikeSongAdmin(admin.ModelAdmin):
    change_list_template = f"{SITE_FOLDER_NAME}/admin/change_list.html" 
    change_form_template = f"{SITE_FOLDER_NAME}/admin/change_form.html" 
    list_display = LIKE_SONG_DISPLAY
    


class _PlaylistAdmin(admin.ModelAdmin):
    change_list_template = f"{SITE_FOLDER_NAME}/admin/change_list.html" 
    change_form_template = f"{SITE_FOLDER_NAME}/admin/change_form.html" 
    list_display = PLAYLIST_LIST_DISPLAY
    


class _TrackAdmin(admin.ModelAdmin):
    change_list_template = f"{SITE_FOLDER_NAME}/admin/change_list.html" 
    change_form_template = f"{SITE_FOLDER_NAME}/admin/change_form.html" 
    list_display = TRACK_LIST_DISPLAY
    


class _FollowerAdmin(admin.ModelAdmin):
    change_list_template = f"{SITE_FOLDER_NAME}/admin/change_list.html" 
    change_form_template = f"{SITE_FOLDER_NAME}/admin/change_form.html" 
    list_display = FOLLOWER_DISPLAY
    


class _ArtistAdmin(admin.ModelAdmin):
    change_list_template = f"{SITE_FOLDER_NAME}/admin/change_list.html" 
    change_form_template = f"{SITE_FOLDER_NAME}/admin/change_form.html" 
    list_display = ARTIST_DISPLAY
    


class _ClientAdmin(admin.ModelAdmin):
    change_list_template = f"{SITE_FOLDER_NAME}/admin/change_list.html" 
    change_form_template = f"{SITE_FOLDER_NAME}/admin/change_form.html" 
    list_display = CLIENT_DISPLAY
    


class _UserAdmin(admin.ModelAdmin):
    change_list_template = f"{SITE_FOLDER_NAME}/admin/change_list.html" 
    change_form_template = f"{SITE_FOLDER_NAME}/admin/change_form.html" 
    list_display = CUSTOM_USER_DISPLAY
    

DASHBOARD.register(Album, _AlbumAdmin )
DASHBOARD.register(Genre, _GenreAdmin )
DASHBOARD.register(LikeSong, _LikeSongAdmin )
DASHBOARD.register(Playlist, _PlaylistAdmin )
DASHBOARD.register(Track, _TrackAdmin )
DASHBOARD.register(Follower, _FollowerAdmin )
DASHBOARD.register(Artist, _ArtistAdmin )
DASHBOARD.register(Client, _ClientAdmin )
DASHBOARD.register(CustomUser, _UserAdmin )