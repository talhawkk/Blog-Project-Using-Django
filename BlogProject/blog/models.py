from django.db import models

# Create your models here.
class Post(models.Model):
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)  # Category ko foreign key ke through link kiya hai
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  

    def __str__(self):
        return self.name
