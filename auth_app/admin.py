from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import Group as DjangoGroup, Group

from auth_app.models import User


class UserAdmin(DjangoUserAdmin):
    pass


admin.site.unregister(DjangoGroup)
admin.site.register(Group)
#admin.site.register(User, UserAdmin)
