from  django import forms

class RegisterForm(forms.Form):
	username=forms.CharField(max_length=100)
	password=forms.CharField(max_length=100,widget=forms.PasswordInput)
	email=forms.EmailField(max_length=100)
	image=forms.ImageField()

class LoginForm(forms.Form):
        username=forms.CharField(max_length=100)
        password=forms.CharField(max_length=100,widget=forms.PasswordInput)
        
class AddPage(forms.Form):
        title=forms.CharField(max_length=100)
        description=forms.CharField(max_length=100)
        image=forms.ImageField()
        price=forms.CharField(max_length=100)
        buildingtype=forms.CharField(max_length=100)
