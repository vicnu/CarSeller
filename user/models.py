# import kwargs as kwargs
from django.db import models

# from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg",null=True,blank=True,upload_to='profile_imgs')

    def __str__(self):
        return f"{self.user.username}Profile"

    def save(self,*args,**kwargs):
        super().save(*args, **kwargs)

        img=Image.open(self.image.path)
        if img.height>300 or img.width>300:
            img.thumbnail((300,300))
            img.save(self.image.path)

    @classmethod
    def create(cls, user):
        profile = cls(user=user)
        # do something with the book
        return profile