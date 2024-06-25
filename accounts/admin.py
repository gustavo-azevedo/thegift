from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import UserInfo


# Register your models here.
admin.site.register(UserInfo)
