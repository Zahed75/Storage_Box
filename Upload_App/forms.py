from django import forms
from .models import Uploader

class EditForm(forms.ModelForm):

    class Meta:
        model = Uploader
        fields=('upload_title', 'file_details', 'thumbnail')