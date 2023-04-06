from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    image=models.ImageField(upload_to="posts_image/")
    user=models.ForeignKey(User,on_delete=models.CASCADE) #c'est pour gerer les permission. foreingkey permet OneToMany
    
    
    def __str__(self):
        # return f'Titre:{self.title}'
        return self.title