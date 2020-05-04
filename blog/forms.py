from django import forms
from .models import Post, Comment
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput

#from django.contrib.admin import widgets
#class DateInput(forms.DateInput):
    #input_type = 'date'


#class TimeInput(forms.TimeInput):
    #publish_time = 'time'
#class CheckboxInput(forms.CheckboxInput):
    #input_type = 'checkbox'

class PostForm(forms.ModelForm):
    #checkbox = forms.BooleanField(widget=CheckboxInput(attrs={'class': 'checkbox'}), required=False)
    #input_type = forms.BooleanField(widget=CheckboxInput(), required=False)
    #created_date = forms.DateField(widget=DateInput(attrs={'class': 'date_created'}))
    #publish_time = forms.TimeField(widget=TimeInput(attrs={'type': 'time'}))
    #fromHour = forms.TimeField(input_format='%I:%M %p', widget=TimePickerWidget(format='%I:%M %p'))

    class Meta:
        model = Post
        fields = ['title', 'text', 'checkbox_datetime', 'published_date', 'published_time']
        widgets = {
            'published_date': DatePickerInput(format='%d/%m/%Y'),
            'published_time': TimePickerInput(format='%H:%M'),
            #'checkbox_datetime': CheckboxInput(),
            #'publish_time': TimeInput()
            #'created_date': DateInput(),
        }

"""
class DateInput(forms.DateInput):
    input_type = 'date'


class PostForm(forms.ModelForm):
    #created_date = forms.DateField(widget=DateInput(attrs={'class': 'date_created'}))
    #fromHour = forms.TimeField(input_format='%I:%M %p', widget=TimePickerWidget(format='%I:%M %p'))
    created_date = forms.DateField(widget=widgets.AdminDateWidget(format='%d/%m/%Y', attrs={'placeholder': 'dd-mm-YY'}))
    publish_time = forms.TimeField(widget=widgets.AdminTimeWidget(format='%H:%M', attrs={'placeholder': 'H:M'}))

    class Meta:
        model = Post
        fields = ('title', 'text', )
        widgets = {
            'publish_time': widgets.AdminDateWidget(),
            'created_date': widgets.AdminDateWidget()
        }
        
"""
"""

class PostForm(forms.ModelForm):
    created_date = forms.DateField(widget=forms.TextInput(format=('%d-%m-%Y'), attrs={'class': 'date_created'}))

    class Meta:
        model = Post
        fields = ('title', 'text', )
        widgets = {'created_date': DateInput()}
"""


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text', )
