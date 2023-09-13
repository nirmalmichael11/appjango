from django import forms
from .models import Applicant

class Apllicationform(forms.ModelForm):
    class Meta:
        model=Applicant
        fields=['name','place','age']