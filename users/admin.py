from django.contrib import admin
from .models import UserModel

class UserAdminModel(admin.ModelAdmin):
    readonly_fields = ('created', )

admin.site.register(UserModel, UserAdminModel)