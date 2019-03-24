from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def profile(request):
    context = {
        'title': request.user.username,
    }
    return render(request, 'users/profile.html', context)


def inici(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login')
