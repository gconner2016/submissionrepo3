from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from blog.models import IsAuthor, Post

# Register your models here.
class AuthorInline(admin.StackedInline):
    model = IsAuthor
    can_delete = False
    verbose_name_plural = 'Author'

class UserAdmin (BaseUserAdmin):
    inlines = (AuthorInline, )

class PostList(admin.ModelAdmin):
    list_display = ('Post_ID', 'Title', 'Post_Date', 'Post_Content')
    list_filter = ('Post_ID', 'Post_Date')
    search_fields = ('Post_ID',)
    ordering = ['Post_ID']

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Post, PostList)
