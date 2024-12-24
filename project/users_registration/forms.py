from django import forms
from .models import Users

class UserForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput, label='Повторите пароль')

    class Meta:
        model = Users
        fields = ['login', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        # Проверка на совпадение паролей
        if password and password2 and password != password2:
            raise forms.ValidationError("Пароли не совпадают")

        return cleaned_data

