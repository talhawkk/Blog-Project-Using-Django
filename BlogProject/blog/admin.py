from django.contrib import admin
from .models import Post, Category
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'category','title', 'image' , 'content']

admin.site.register(Category)
