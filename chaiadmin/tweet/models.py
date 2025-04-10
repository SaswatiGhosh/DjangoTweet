from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    # title=models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.TextField(max_length=240)
    photo= models.ImageField(upload_to='photos/', blank=True ,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    uploaded_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'
