from django.contrib import admin

# Register your models here.
from . models import Profile,Posts

admin.site.register(Profile)
admin.site.register(Posts)