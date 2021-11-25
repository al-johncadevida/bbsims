from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from . models import Post
# from .models import Comment
#
# class CommentUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('name', 'body',)
#
#     widgets = {
#         'name': forms.TextInput(attrs={'class': 'form-control'}),
#         'body': forms.Textarea(attrs={'class': 'form-control'}),
#     }

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Post'))