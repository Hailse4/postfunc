import json 
from PIL import Image
from django.db import models
from django.contrib.auth.models import User





class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,help_text="Profile Username")
    bio = models.TextField(max_length=100,default="write your bio",blank=True)
    image = models.ImageField(default="default.png",
                              upload_to="profile_img")
    def __str__(self):
          return self.name
        
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        if self.image:
            img = Image.open(self.image.path)
            max_size = (300,300)
            img.thumbnail(max_size)
            img.save(self.image.path)


class PostLikeModel(models.Model):
    profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    post = models.ForeignKey('PostModel',on_delete=models.CASCADE)
    def __str__(self):
        return self.profile.name + "_like"

class PostCommentModel(models.Model):
    profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    comment = models.TextField(max_length=100)
    post = models.ForeignKey('PostModel',on_delete=models.CASCADE)
    
class PostModel(models.Model):
    profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    description = models.TextField(max_length=100,blank=True,default="")
    image = models.ImageField(upload_to="post_pics")
    like = models.ForeignKey(PostLikeModel,on_delete=models.CASCADE)
    comment = models.ForeignKey(PostCommentModel,on_delete=models.CASCADE)
    def __str__(self):
        model_name = self.profile.name + "_post_"+self.pk
        return model_name
     

    
    




