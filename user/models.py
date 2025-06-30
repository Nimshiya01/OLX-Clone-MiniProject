from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='userprofile')
    bio= models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures',null=True,blank=True)
    address = models.TextField(blank=True)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username
    

class Posts(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    pimg = models.ImageField(upload_to='Posts')
