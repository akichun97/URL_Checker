from django import forms
from myapp.models import *


class URLCheck(forms.ModelForm):
    class Meta:
        model = URL
        fields = ["url", "state"]