from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=False,unique=True)
    description = models.TextField()
    ingredients = models.TextField(blank=True)
    recipe = models.TextField()
    added_by = models.ForeignKey(User,on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="Recipe/")
    
    def __str__(self):
        return self.name
    
    
    
ratings = [
    ("⭐","⭐"),
    ("⭐⭐","⭐⭐"),
    ("⭐⭐⭐","⭐⭐⭐"),
    ("⭐⭐⭐⭐","⭐⭐⭐⭐"),
    ("⭐⭐⭐⭐⭐","⭐⭐⭐⭐⭐")
]
class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    body = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices=ratings, max_length=20,verbose_name="Rating")   
    
    
class Comment(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    commentator = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
        