from django.contrib import admin
from .models import Film, Chapter, User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

fields_user = list(UserAdmin.fieldsets)
fields_user.append(
    ("History", {'fields': ('movies_watched',)})
)
UserAdmin.fieldsets = tuple(fields_user)

admin.site.register(Film)
admin.site.register(Chapter)
admin.site.register(User, UserAdmin)
