from django import forms
from . import models


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(username=username)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("username", forms.ValidationError("User does not exist"))


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ["username", "first_name", "last_name", "email"]
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username"}),
            "first_name": forms.TextInput(attrs={"placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
        }

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm password"}),
        label="confirm password",
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            models.User.objects.get(username=username)
            raise forms.ValidationError("username already exists")
        except models.User.DoesNotExist:
            return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("User already exists with this email")
        except models.User.DoesNotExist:
            return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("password confirmation doest not match")
        else:
            return password1

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.username = username
        user.email = email
        user.set_password(password)
        user.save()
