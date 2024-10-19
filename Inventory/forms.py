from django import forms
from .models import Raga

class RagaForm(forms.ModelForm):
    class Meta:
        model = Raga
        fields = ['name']