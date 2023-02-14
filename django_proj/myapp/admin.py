from django.contrib import admin
from .models import Notes, Groups, Tags

# Register your models here.
admin.site.register(Tags)
admin.site.register(Groups)
admin.site.register(Notes)