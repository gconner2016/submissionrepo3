from django.db import models
from django.contrib.auth.models import User

class IsAuthor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_author = models.BooleanField(default=False)


class Post(models.Model):
    """Model Representing a post."""
    Post_ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=200, unique=True)
    Notification_ID = models.IntegerField(blank=False, null=False)
    Post_Date = models.DateTimeField(auto_now_add=True)
    Post_Summary = models.CharField(max_length=200, unique=True)
    Post_Content = models.CharField(max_length=400)
    User = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    

    def __str__(self):
        return self.Title
      
class Comment(models.Model):
    """Model Representing a comment."""
    Comment_ID = models.AutoField(primary_key=True)
    Post_ID = models.ForeignKey(Post, on_delete=models.CASCADE)
    Comment_Title = models.CharField(max_length=50)
    User = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    Comment_Content = models.CharField(max_length=300)
  
    def __str__(self):
        return self.Comment_Title

class Notification(models.Model):
    Notification_ID = models.AutoField(primary_key=True)
    Author = models.ForeignKey(IsAuthor, on_delete=models.CASCADE, null=False)
    User = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
