from django import forms
from django.contrib.auth.models import User
from .models import Question, Answer

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['body']
