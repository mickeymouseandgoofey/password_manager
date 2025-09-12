from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from .models import Credential
from .forms import CredentialForm, CustomUserCreationForm
from .utils import encrypt_password, decrypt_password

# Home view (optional placeholder)
def vault_home(request):
    return HttpResponse("Welcome to your vault.")

# Dashboard: show saved credentials with decrypted passwords
@login_required
def dashboard(request):
    credentials = Credential.objects.filter(user=request.user)
    for cred in credentials:
        cred.decrypted_password = decrypt_password(cred.password_encrypted)
    return render(request, 'vault/dashboard.html', {'credentials': credentials})

# Add a new credential
@login_required
def add_credential(request):
    if request.method == 'POST':
        form = CredentialForm(request.POST)
        if form.is_valid():
            cred = form.save(commit=False)
            cred.user = request.user
            cred.password_encrypted = encrypt_password(form.cleaned_data['password_plain'])
            cred.save()
            return redirect('dashboard')
    else:
        form = CredentialForm()
    return render(request, 'vault/add_credential.html', {'form': form})

# Register a new user and auto-login
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
