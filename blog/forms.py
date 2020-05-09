from django import forms
from .models import Post, Comment
from bootstrap_datepicker_plus import DateTimePickerInput



class PostForm(forms.ModelForm):
    #checkbox = forms.BooleanField(widget=CheckboxInput(attrs={'class': 'checkbox'}), required=False)
    #input_type = forms.BooleanField(widget=CheckboxInput(), required=False)

    class Meta:
        model = Post
        fields = ('title', 'text', 'checkbox_datetime', 'published_datetime', )
        widgets = {
            'published_datetime': DateTimePickerInput(),
            #'checkbox_datetime': CheckboxInput(),
        }



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text', )
