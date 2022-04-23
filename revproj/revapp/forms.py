from django import forms
from .models import RevModel

class RevForm(forms.ModelForm):
    class Meta:
        model=RevModel
        fields="__all__"