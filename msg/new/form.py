from django import forms
from new.models import Info

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ('user_name','message')
