from django import forms
from .models import Customer
from django_countries.widgets import CountrySelectWidget
from django.forms.extras.widgets import SelectDateWidget
import datetime

class RegistrationForm(forms.ModelForm):
    class Meta:
        this_year = datetime.date.today().year
        yr_choice = []
        for yr in range(1920, int(this_year)):
            yr_choice.append(yr)

        model = Customer
        fields = '__all__'

        widgets = {
            'username': forms.TextInput(),
            'birth_date': SelectDateWidget(years=yr_choice),
            'password': forms.PasswordInput(),
            'country': CountrySelectWidget(),

        }
class SignInForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['email','password',]
        widgets={
            'password':forms.PasswordInput(),
        }


    def clean_email(self):
        email=self.cleaned_data.get('email')
        customers=[(customer.email) for customer in Customer.objects.filter(email=email)]
        if not email in customers:
            raise forms.ValidationError("Please first register with us")

        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise  forms.ValidationError("The password is too short, please enter again !!!")

        return password