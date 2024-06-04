from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label="username:")
    password = forms.CharField(max_length=10, label="password", widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=15, label="username:")
    password = forms.CharField(max_length=8, label="password:", widget=forms.PasswordInput())  # passwordun gizli gorunmesi ucun
    confirm = forms.CharField(max_length=8, label="password again:", widget=forms.PasswordInput())

    def clean(self):  # datalari alib yigmaq ucun
        cleaned_data = super().clean()  # super() ile temizlenmiş verileri al
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm")

        if password and confirm and password != confirm:   #xana bos buraxilmissa ve bir birine beraber deyilse
            raise forms.ValidationError("sifreler eyni deyil!")

        values = {                  #dogrudursa deyerleri al 
            "username" : username,
            "password" : password
        }

        return values
