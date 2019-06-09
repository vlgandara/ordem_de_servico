from django import forms

from .models import Equipamento

class PostForm(forms.ModelForm):

    class Meta:
        model = Equipamento
        fields = ('equipamento', 'marca', 'modelo', 'n_serie')
