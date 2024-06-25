from django import forms
from django.forms import EmailInput
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth import  password_validation
from django.contrib.auth.models import User, Group
import datetime
from django.utils.translation import gettext_lazy as _

class LoginForm(AuthenticationForm):
    username = UsernameField(
        label="",
        widget=forms.TextInput(attrs={
            "autofocus": True,
            "placeholder": "Nome de usuário"}))
    password = forms.CharField(
        label="",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "Senha atual",
            "placeholder": "Palavra-chave"}),
    )

class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(
        label="",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "Palavra-chave",
            "placeholder": "Palavra-chave"
            }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            "placeholder": "Confirmar palavra-chave"
            }),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    email = forms.EmailField(
        required=True,
        widget=EmailInput(attrs={'placeholder': "Endereço de email"}),
        label="")

    gender_choices = [
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('O', 'Outro'),
    ]
    gender = forms.ChoiceField(choices=gender_choices, widget=forms.RadioSelect())
    name = forms.CharField(
        max_length=100, 
        label="Nome completo",
        widget=forms.TextInput(attrs={"placeholder": "Digite seu nome",})
        )

    crr_year = datetime.date.today().year
    years = list(range(crr_year, crr_year-100, -1))
    birthday = forms.DateField(widget=forms.SelectDateWidget(years=years), label="Aniversário")
    
    size_choices = [
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande'),
    ]
    size = forms.ChoiceField(choices=size_choices, widget=forms.RadioSelect())


    style_choices = [
        ('BA', 'Básico'),
        ('MO', 'Moderninho'),
        ('EL', 'Elegante'),
    ]
    style = forms.ChoiceField(choices=style_choices, widget=forms.RadioSelect())

    interests_choices = [
        ('roupas', 'Roupas'),
        ('fitness', 'Fitness'),
        ('beleza', 'Beleza'),
        ('eletronicos', 'Eletrônicos'),
        ('outros', 'Outros')
    ]
    interests = forms.MultipleChoiceField(choices=interests_choices, widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = User
        fields = ("username","email")
        field_classes = {"username": UsernameField}
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Nome de usuário",}),
            }
        labels = {"username": "",}
