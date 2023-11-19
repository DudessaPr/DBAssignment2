from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('users/', views.get_users, name='get_users'),
    path('main_page/', views.main_page, name='main_page'),
    path('registration-member/', views.registration_member, name='registration-member'),
    path('login/', views.custom_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create_caregiver/', views.create_caregiver, name='create_caregiver'),
    path('create_member/', views.create_member, name='create_member'),
    path('create_address/', views.create_address, name='create_address'),
    path('profile/', views.profile, name='profile'),
    path('accept_appointment/<int:appointment_id>/', views.accept_appointment, name='accept_appointment'),
    path('decline_appointment/<int:appointment_id>/', views.decline_appointment, name='decline_appointment'),
    path('delete_appointment/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
    path('create_appointment/<int:jobapp_id>/', views.create_appointment, name='create_appointment'),
    path('edit_member_profile/', views.edit_member_profile, name='edit_member_profile'),
    path('create_job/', views.create_job, name='create_job'),
]
