from django import forms


class FormularioContato(forms.Form):
    nome = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Informe seu nome', 'class': 'form-control'})
    )
    email = forms.EmailField(
        max_length=255,
        widget=forms.EmailInput(attrs={'placeholder': 'Informe o e-mail', 'class': 'form-control'})
    )
    telefone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Seu telefone', 'class': 'form-control'})
    )
    mensagem = forms.CharField(
        max_length=255,
        widget=forms.Textarea(attrs={'placeholder': 'Sua mensagem', 'class': 'form-control', 'rows': 3})
    )
