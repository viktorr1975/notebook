from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Notes, Groups, Tags

# Register your models here.
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Tags)
admin.site.register(Groups)
admin.site.register(Notes)