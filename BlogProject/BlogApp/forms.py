from django import forms
from .models import BlogModel

# creates the a from that pulls all the fields in the modeltouch

class NewBlogForm(forms.ModelForm):
    class Meta():
        model = BlogModel
        fields = '__all__'
        # fields = ['title',]

