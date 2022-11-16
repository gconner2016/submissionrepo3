from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from blog.models import IsAuthor

# Register your models here.
class AuthorInline(admin.StackedInline):
    model = IsAuthor
    can_delete = False
    verbose_name_plural = 'Author'

class UserAdmin (BaseUserAdmin):
    inlines = (AuthorInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
