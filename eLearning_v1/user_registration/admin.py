from django.contrib import admin
from .models import users, courses

# Register your models here.
admin.site.register(users)
admin.site.register(courses)