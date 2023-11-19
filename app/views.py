
from .models import User, Caregiver, Member, Address, Appointment, Job, JobApplication
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm, CustomLoginForm, CaregiverForm, MemberForm, AddressForm, AppointmentForm, JobForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils import timezone


def create_job(request):
    member = request.user.member
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.member = member
            job.date_posted = timezone.now().date()
            job.save()
            return redirect('profile')  
    else:
        form = JobForm()

    return render(request, 'create_job.html', {'form': form})

def accept_appointment(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    appointment.status = 'Accepted'
    appointment.save()
    return redirect('profile')

def decline_appointment(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    appointment.status = 'Declined'
    appointment.save()
    return redirect('profile')

def delete_appointment(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    appointment.delete()
    return redirect('profile')

def edit_member_profile(request):
    member_instance = request.user.member
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member_instance)
        if form.is_valid():
            form.save()
            return redirect('profile')  
    else:
        form = MemberForm(instance=member_instance)
    return render(request, 'edit_member_profile.html', {'form': form})

def create_appointment(request, jobapp_id):
    jobapp = JobApplication.objects.get(id=jobapp_id)
    caregiver = jobapp.caregiver
    job = Job.objects.get(id=jobapp.job.id)
    member = Member.objects.get(user=job.member.user)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.caregiver = caregiver
            appointment.member = member
            appointment.save()
            return redirect('profile')  
    else:
        form = AppointmentForm()

    return render(request, 'create_appointment.html', {'form': form})
def profile(request):
    member = request.user.member
    appointments = Appointment.objects.filter(member=member).order_by('status')

    jobs = Job.objects.filter(member=member)
    job = Job.objects.filter(member=member).first()
    job_applications = JobApplication.objects.filter(job=job)

    return render(request, 'profile.html', {'appointments': appointments, 'jobapps':job_applications, 'jobs':jobs})

def superuser_page(request):
    if request.user.is_superuser:
        
        return render(request, 'superuser_page.html')
    else:
        
        return render(request, 'main_page.html')  

def custom_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main_page')  # Redirect to a profile page or any other page after successful login
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = CustomLoginForm()

    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add a login logic here if needed
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('get_users')  # Redirect to a success page
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def create_caregiver(request):
    user = request.user


    if Caregiver.objects.filter(user=user).exists():

        messages.warning(request, 'You are already registered as a caregiver.')
        return redirect('main_page')  

    if request.method == 'POST':
        form = CaregiverForm(request.POST, request.FILES)
        if form.is_valid():
            caregiver = form.save(commit=False)
            caregiver.user = user  
            caregiver.save()
            return redirect('main_page')  
    else:
        form = CaregiverForm()

    return render(request, 'create_caregiver.html', {'form': form})

@login_required
def create_member(request):
    user = request.user


    if Member.objects.filter(user=user).exists():

        messages.warning(request, 'You are already registered as a member.')
        return redirect('main_page') 

    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            member = form.save(commit=False)
            member.user = user  
            member.save()
            return redirect('create_address')  
    else:
        form = MemberForm()

    return render(request, 'create_member.html', {'form': form})

@login_required
def create_address(request):
    user = request.user
    member = Member.objects.filter(user=user).first()

    if request.method == 'POST':
        form = AddressForm(request.POST, request.FILES)
        if form.is_valid():
            address = form.save(commit=False)
            address.member = member  
            address.save()
            return redirect('main_page')  
    else:
        form = AddressForm()

    return render(request, 'create_address.html', {'form': form})



def get_users(request):
    users = User.objects.all()

    return render(request, 'main.html', {'users':users})

def main_page(request):

    return render(request, 'main_page.html')

def registration_member(request):
    return render(request, 'myapp/registration_member.html')
