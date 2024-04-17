from django import forms
from videoapp.models import Video

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['name', 'description', 'url']
