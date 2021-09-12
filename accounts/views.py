from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import LoginForm, SignupForm


def login_view(request):
    next_url = None
    if 'next' in request.GET:
        next_url = request.GET['next']

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data.get('username')
            password = data.get('password')
            user = authenticate(username=username, password=password)
            if user is None:
                messages.warning(request, 'Either email or password is wrong!')
                return redirect('login')
            login(request, user)
            if next_url:
                return redirect(next_url)
            else:
                return redirect('index')
        else:
            messages.warning(request, 'Something went wrong while filling up the form')
    return render(request, 'accounts/login.html', {'next_url': next_url})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong while filling up the form')
    return render(request, 'accounts/signup.html')


def logout_view(request):
    logout(request)
    return redirect('index')
