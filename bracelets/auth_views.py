from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import UserRegistrationForm


def register_admin(request):
    if request.user.is_authenticated:
        return redirect('bracelets_list')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            authenticated = authenticate(
                request,
                username=user.username,
                password=form.cleaned_data['password'],
            )
            if authenticated:
                login(request, authenticated)
                messages.success(request, f'Welcome, {authenticated.username}. Your account is ready.')
                return redirect('bracelets_list')
    else:
        form = UserRegistrationForm()

    return render(request, 'bracelets/register.html', {'form': form})


def login_admin(request):
    if request.user.is_authenticated:
        return redirect('bracelets_list')

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next')
            if user.username == 'admin' and not next_url:
                return redirect('admin_dashboard')
            return redirect(next_url or 'bracelets_list')
    else:
        form = AuthenticationForm()

    return render(request, 'bracelets/login.html', {
        'form': form,
        'next': request.GET.get('next', ''),
    })


def logout_admin(request):
    logout(request)
    return redirect('bracelets_list')
