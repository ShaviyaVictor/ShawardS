from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image



# Create your models here.
class Profile(models.Model) :
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  location = models.CharField(max_length=35)
  bio = models.CharField(max_length=150)
  profile_img = models.ImageField(default='default.jpg', upload_to='profile_images/')


  def __str__(self) :
    return f'{self.user.username}\'s Profile'

  
  def save(self) :
    super().save()

    img = Image.open(self.profile_img.path)

    if img.height > 300 or img.width > 300 :
      output_size = (300, 300)
      img.thumbnail(output_size)
      img.save(self.profile_img.path)