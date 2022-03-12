from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




# Create your models here.
class Post(models.Model) :
  project_name = models.CharField(max_length=50)
  date_posted = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='posts/')

  def __str__(self) :
    return self.project_name

  class Meta :
    ordering = ['-date_posted']