from django.contrib import admin
from users.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    search_fields = ["email__startswith", "username__startswith"]
    list_display = [
        "id",
        "username",
        "email",
        "firstName",
        "lastName",
        "is_staff",
        "is_superuser",
    ]
    list_filter = ["is_staff", "is_superuser"]
    list_display_links = ["username", "email"]
    ordering = ["id"]
    filter_horizontal = []
    fieldsets = [
        (None, {"fields": ["username", "email", "password"]}),
        ("Personal Info", {"fields": ["firstName", "lastName", "phone"]}),
        ("Image", {"fields": ["super_image"]}),
        ("Permissions", {"fields": ["is_staff", "is_superuser"]}),
    ]


@admin.register(Client)
class ClientAdmin(UserAdmin):
    search_fields = ["email__startswith", "username__startswith"]
    list_display = [
        "id", 
        "username", 
        "email", 
        "firstName", 
        "lastName",
        ]
    list_display_links = ["username", "email"]
    list_filter = []
    ordering = ["id"]
    filter_horizontal = []
    fieldsets = [
        (None, {"fields": ["username", "email", "password"]}),
        (
            "Personal Info",
            {"fields": ["firstName", "lastName", "phone", "image", "favoriteTracks"]},
        ),
        ("Permissions", {"fields": []}),
    ]


@admin.register(Artist)
class ArtistAdmin(UserAdmin):
    search_fields = [
        "email__startswith",
        "username__startswith",
    ]
    list_display = [
        "id",
        "username",
        "email",
        "firstName",
        "lastName",
        "stageName",
        # "bio",
        "image",
        "coverImage",
        "is_staff",
    ]
    list_display_links = ["username", "email"]
    list_filter = ["is_staff"]
    ordering = ["id"]
    filter_horizontal = []
    fieldsets = [
        (None, {"fields": ["username", "email", "password"]}),
        (
            "Personal Info", 
            {
                "fields": [
                    "firstName", 
                    "lastName", 
                    "phone", 
                    "stageName",
                    "bio",
                    "image",
                    "coverImage",
                    "dateOfBirth"
                ]
            }
        ),
        ("Permissions", {"fields": ["is_staff"]}),
    ]


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = FOLLOWER_DISPLAY