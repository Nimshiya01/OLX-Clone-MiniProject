from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('login',loginpage,name='login'),
    path('logout',logoutpage,name='logout'),
    path('register',adduser,name='register'),
    path('profile',profilepage,name='profile'),
    path('editprfile/<int:eid>',editprofile,name='editprofile'),
    path('addpost',addpost)
  
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)