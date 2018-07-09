from django import forms
from . models import HotMetal

class HMform(forms.ModelForm):
    class Meta:
        model = HotMetal
