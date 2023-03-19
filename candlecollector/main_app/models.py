from django.db import models
from django.db.models import Model
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class GeeksModel(Model):
    geeks_field = models.ImageField()

class Bookmark(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name 
    def get_absolute_url(self):
        return reverse("bookmarks_detail", kwargs={"pk": self.id}) 

class Book(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    pic = models.ImageField(upload_to ='main_app/static/uploads/', blank=True)
    bookmark = models.ManyToManyField(Bookmark)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"book_id": self.id})
    


    
