from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_date')
    list_filter = ('status')
    search_fields = ['title','content']







admin.site.register(Post)