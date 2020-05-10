from django import forms
from .models import Post, Comment
from bootstrap_datepicker_plus import DateTimePickerInput


class PostForm(forms.ModelForm):
    checkbox_datetime = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'some'}), required=False)

    class Meta:
        model = Post
        fields = ('title', 'text', 'published_datetime', 'checkbox_datetime', )
        widgets = {
            'published_datetime': DateTimePickerInput(),
        }



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text', )
