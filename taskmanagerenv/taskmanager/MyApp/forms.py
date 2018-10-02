from django.contrib.auth.models import User
from django import forms
from .models import Categories, Task, MyMessage


class LoginForm(forms.Form):
    login = forms.CharField(label='login')
    password = forms.CharField(label='password', widget=forms.PasswordInput)


CHOICES = (
    ('medium', 'medium'),
    ('high', 'high'),
    ('very high', 'very high'),
)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("name", "categorie", "deadline")

    priority = forms.CharField(widget=forms.Select(choices=CHOICES))


class MessageForm(forms.ModelForm):
    class Meta:
        model = MyMessage
        fields = ('towho', 'description')
