from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=50)
    query=models.TextField()
    date_posted=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    img=models.ImageField(default='default.jpg',upload_to='homepics')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('app_home')
