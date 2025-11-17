from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.db import transaction
from .models import Profile
from .forms import UserForm, ProfileForm, RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Use a transaction to avoid race conditions with post_save signals
            with transaction.atomic():
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                )
                # A post_save signal may already create a Profile; ensure idempotence
                Profile.objects.get_or_create(user=user)
            messages.success(request, 'Inscription réussie! Vous pouvez maintenant vous connecter.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenue {user.first_name or user.username}!')
            # Redirection différenciée selon le type d'utilisateur
            if user.is_staff or user.is_superuser:
                return redirect('admin:index')
            else:
                return redirect('dashboard')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
            return render(request, 'accounts/login.html', {'error': True})
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Vous avez été déconnecté.')
    return redirect('home')


@login_required(login_url='login')
def profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profil mis à jour avec succès!')
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile,
    }
    return render(request, 'accounts/profile.html', context)


@login_required(login_url='login')
def become_seller(request):
    profile = request.user.profile
    if profile.role == 'seller':
        messages.info(request, 'Vous êtes déjà un vendeur.')
        return redirect('profile')
    
    if request.method == 'POST':
        profile.role = 'seller'
        profile.store_name = request.POST.get('store_name')
        profile.store_description = request.POST.get('store_description')
        profile.save()
        messages.success(request, 'Vous êtes maintenant vendeur!')
        return redirect('seller_dashboard')
    
    return render(request, 'accounts/become_seller.html')

