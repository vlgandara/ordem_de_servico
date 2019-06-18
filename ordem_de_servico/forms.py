from django import forms

from .models import Equipamento, OrdemServico

class PostForm(forms.ModelForm):

    class Meta:
        model = Equipamento
        fields = ('equipamento', 'marca', 'modelo', 'n_serie')

class OrdemForm(forms.ModelForm):

    class Meta:
        model = OrdemServico
        fields = ('equipamento', 'marca', 'modelo', 'n_serie', 'n_os', 'nome', 'empresa', 'cpf', 'end', 'cep', 'telefone', 'falha', 'graunecessidade')
