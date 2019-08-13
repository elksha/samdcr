from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'review', 'reviewb', 'picture', 'pictureb')
        labels = {
            'title' : _('멘티의 이름'),
            'review' : _('처음 만난 모습'),
            'reviewb' : _('달라진 모습'),
            'picture' : _('처음의 사진'),
            'pictureb' : _('달라진 사진')
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment',)
        labels = {
            'comment' : _('')
        }

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password',)
        widgets = {
            'password': forms.PasswordInput()
            }