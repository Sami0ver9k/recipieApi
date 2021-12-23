from django.contrib import admin, auth
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _


from core import models


'''this admin change user is used by add new user we just have to add add_fields that
that is used in the add new user page'''

class UserAdmin(BaseUserAdmin):
     ordering=['id']
     list_display=['email', 'name']
     fieldsets=(
         (None,{'fields': ('email','password')}),
         (_('personal info'),{'fields':  ('name',)}),
         (
             _('Permissions'),
             {
                 'fields' :('is_active','is_staff','is_superuser')
             }
         ),
         (_('important dates'),{'fields': ('last_login',)})
     )

     add_fieldsets=(
         (None, {
             'classes': ('wide',),
             'fields': ('email','password2','password2')
         }),
     )



admin.site.register(models.User,UserAdmin)
admin.site.register(models.Tag)

