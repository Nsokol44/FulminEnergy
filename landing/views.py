from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from landing.models import Information
from landing.forms import SignUpForm
from django.urls import reverse
# Create your views here.


def signUp(request):

    form = SignUpForm(request.POST or None)

    if request.method == 'POST':

            if form.is_valid():
                data = form.save(commit=False)
                data.firstName = request.POST["firstName"]
                data.lastName = request.POST["lastName"]
                data.email = request.POST["email"]
                data.questions = request.POST["questions"]
                data.save()

                return HttpResponseRedirect(reverse('post-sign-up'))

            else:
                form = SignUpForm(request.POST)

    return render(request, 'landing/index.html', context = {'form': form })


def successSignUp(request):
    return render(request, 'landing/success.html')
