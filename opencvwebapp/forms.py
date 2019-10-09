from django import forms
from .models import ImageUploadModel,Profile


class UploadImageForm(forms.Form):
    title = forms.CharField(max_length=50)
    image = forms.ImageField()
    
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUploadModel
        fields = ('description', 'document' )

class ProfileUploadForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','image']