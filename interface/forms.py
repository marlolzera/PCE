from django.contrib.auth.models import User
from django.forms import ModelForm, CharField, PasswordInput, Textarea, EmailField, TextInput, EmailInput
from interface.models import UsuarioInfo


class UsuarioForm(ModelForm):

    username = CharField(max_length=100, label=u'Usuário',
                       widget=TextInput(attrs={'placeholder': 'login',
                                                'class': 'form-control'}))

    password = CharField(max_length=25, required=True, label=u'Senha',
                      widget=PasswordInput(attrs={'placeholder': 'password',
                                                  'class': 'form-control'}))

    email = EmailField(max_length=100, label=u'Email',
                       widget=EmailInput(attrs={'placeholder': 'Email',
                                                'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UsuarioInfoForm(ModelForm):

    endereco = CharField(max_length=200, label=u'Endereço',
                         widget=Textarea(attrs={'cols': 40,
                                                'rows': 5,
                                                'placeholder': 'Endereço',
                                                'class': 'form-control'}))

    class Meta:
        model = UsuarioInfo
        fields = ('endereco',)
