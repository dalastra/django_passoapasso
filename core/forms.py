from django import forms
from .models import Contato


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem', 'imagem']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Seu nome'}),
            'email': forms.EmailInput(attrs={'placeholder': 'seuemail@exemplo.com'}),
            'mensagem': forms.Textarea(attrs={'placeholder': 'Digite sua mensagem', 'rows': 4}),
            'imagem': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }

    def clean_nome(self):
        nome = self.cleaned_data['nome'].strip()
        if len(nome) < 3:
            raise forms.ValidationError('O nome deve ter pelo menos 3 caracteres.')
        return nome