from django import template
from django.conf import settings
from dashboard.applist_manifest import APPLIST
from django.utils.html import format_html
from django.utils.safestring import mark_safe
import json
from django import template
from django.apps import apps
register = template.Library()



filename_path = settings.CUSTOM_ADMIN_NAVIGATION_TEMPLATE if settings.CUSTOM_ADMIN_NAVIGATION_TEMPLATE != "" else "admin/app_list.html"
@register.inclusion_tag(filename=filename_path, takes_context=True)
def app_list_tag( context ):
    try:
        context_name = settings.CUSTOM_ADMIN_NAVIGATION_CONTEXT_NAME if settings.CUSTOM_ADMIN_NAVIGATION_CONTEXT_NAME != '' else 'data_app_list'
        context[context_name] = APPLIST
        return context
    except Exception as e:
        return str(e)
    
    
# @register.simple_tag(takes_context=True)
@register.inclusion_tag(filename="spotipy/admin/change_list_display.html", takes_context=True)
def dynamic_list_display(context, app_name, model_name):
    # Get the model class
    model_class = apps.get_model(app_name, model_name)

    # Try to call the "list_d" method first
    try:
        list_display = model_class.custom_list_display()
        context["list_display"] = list_display
    except AttributeError:
        # Fallback to the original behavior if "list_d" doesn't exist
        list_display = getattr(model_class._meta, "list_display", None)
    # print(context)
    return context



@register.simple_tag
def assign(value):
    """
    Assigns a value to a variable.
    """
    return value