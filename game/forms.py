from django import forms
from .models import TopBack



class TopBackForm(forms.ModelForm):
      class Meta:
          model = TopBack
          fields = ['name', 'description', 'email', 'phone', 'document']
