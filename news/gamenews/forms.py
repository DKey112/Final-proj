from django import forms
from .models import Post, Game

choices = Game.objects.all().values_list('name','slug')
choice_list= []
for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ('title', 'content','post_pic','game')

    widgets={
        'Discipline' : forms.Select(choices=choice_list, attrs={'class':'form-control'}),
        'Post Pictures' : forms.ImageField(label=u'Post Pictures', widget=forms.FileInput(attrs={'multiple': 'multiple'}))
    }
    