from multiprocessing import AuthenticationError
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Caregiver, Member, Address, Appointment, Job
from django.contrib.auth.forms import AuthenticationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'given_name', 'surname', 'city', 'phone_number', 'profile_description', 'password1', 'password2']
    
class CustomLoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']

class CaregiverForm(forms.ModelForm):
    class Meta:
        model = Caregiver
        fields = ['gender', 'caregiving_type', 'hourly_rate']

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['house_rules', ]

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['house_number', 'street', 'town' ]

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_date', 'appointment_time', 'work_hours',]
    appointment_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True,
    )
    appointment_time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        required=True,
    )
class JobForm(forms.ModelForm):
    REQUIRED_CAREGIVING_TYPE_CHOICES = [
        ('babysitter', 'Babysitter'),
        ('caregiver for elderly', 'Caregiver for Elderly'),
        ('playmate for children', 'Playmate for Children'),
    ]

    required_caregiving_type = forms.ChoiceField(
        choices=REQUIRED_CAREGIVING_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Job
        fields = ['required_caregiving_type', 'other_requirements']