from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        exclude = ('user','like_users', )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            "content" : forms.TextInput(
                attrs={
                    # "class" : "form-control mt-2",
                    "style" : 'width: 80%; background-color: black; color : black',
                    # "float" :"center",
                    "disply" : "inline-block",
                    "placeholder" : "댓글을 입력해주세요."
                }
            )}
        labels = {
            "content": "댓글"
        }