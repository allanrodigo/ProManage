from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from django.core.exceptions import ValidationError
from .models import Project, Task

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Please provide a valid email.')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already in use")
        return email

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
        label="Username"
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}),
    )

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

TaskFormSet = inlineformset_factory(Project, Task, fields=('title', 'description', 'due_date', 'is_completed'), extra=1, can_delete=True, widgets={
    'title': forms.TextInput(attrs={'class': 'form-control'}),
    'description': forms.Textarea(attrs={'class': 'form-control'}),
    'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
})

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        def __init__(self, *args, **kwargs):
            super(TaskForm, self).__init__(*args, **kwargs)
            self.fields['due_date'].required = False  

