from email.policy import default
from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model) :
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  location = models.CharField(max_length=35)
  bio = models.CharField(max_length=150)
  profile_img = models.ImageField(default='default.jpg', upload_to='profile_images/')


  def __str__(self) :
    return f'{self.user.username}\'s Profile'

  