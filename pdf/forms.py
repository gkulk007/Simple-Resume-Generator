from django import forms
from .models import Profile
class CKForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
    
    