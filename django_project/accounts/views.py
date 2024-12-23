from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login

# Create your views here.
def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:sighup')
    else:
        form = SignupForm()
        
    return render(request, 'accounts/signup.html', {'form': form})