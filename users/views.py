from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required




# Create your views here.
def register(request) :

  if request.method == 'POST' :
    form = UserRegisterForm(request.POST)

    if form.is_valid() :
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Account created for { username }. Login to continue')

      return redirect('login')

  else :
    form = UserRegisterForm()

  return render(request, 'users/register.html', { 'form':form })



@login_required
def profile(request) :

 
  return render(request, 'users/profile.html')



@login_required
def update_profile(request) :

  u_form = UserUpdateForm()
  p_form = ProfileUpdateForm()

  context = {
    'u_form': u_form,
    'p_form': p_form
  }

  return render(request, 'users/update_profile.html', context)