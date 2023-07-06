# from django.http import HttpResponse
from django.shortcuts import render
# from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm 
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages

@login_required
def dashboard(request):
    ## superuser created by 'python manage.py createsuperuser' does not have its Profile object. Let's create one. 
    if request.user.is_superuser:   
        if not Profile.objects.filter(user=request.user).exists():
            Profile.objects.create(user=request.user)
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password']) 
            new_user.save()
            Profile.objects.create(user=new_user) 
            return render(request, 'account/register_done.html', {'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form':user_form})

@login_required
def user_edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST) 
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            ## to show the photo, pass the profile_form.instance, which is the model instance of the form
            return render(request, 'account/edit_done.html', {'profile_model':profile_form.instance} )
        else: 
            messages.error(request, 'Error updating your profile') 
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', {'user_form':user_form, 'profile_form':profile_form})



