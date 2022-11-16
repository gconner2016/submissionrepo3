from django import forms
from .models import Comment, Post

class Comment_Form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('User', 'Comment_Title', 'Comment_Content')
        
class Post_Form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('Title', 'Post_Date', 'Post_Summary', 'Post_Content')
        






