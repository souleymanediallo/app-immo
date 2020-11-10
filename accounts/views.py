from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterUserCreationForm
from contacts.models import Contact


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Votre compte a été crée avec succès {username}!")
            return redirect('login')
    else:
        form = RegisterUserCreationForm()
    context = {'form': form}
    return render(request, "accounts/register.html", context)


def dashboard(request):
    user_contacts = Contact.objects.filter(user_id=request.user.id)
    context = {'contacts': user_contacts}
    return render(request, "accounts/dashboard.html", context)