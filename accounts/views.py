from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate

from .forms import RegistrationForm, LoginForm
from  .models import User


def redirectTo(url):
    return HttpResponseRedirect(reverse(url))

class LoginView(View):
    template = 'accounts/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirectTo('blog:home')
        f = LoginForm()
        return render(request, self.template, {'form': f})

    def post(self, request):
        f = LoginForm(request.POST)
        c = {'form': f}
        if f.is_valid():
            email = f.cleaned_data['email']
            password = f.cleaned_data['password']
            u = authenticate(email=email, password=password)
            if u is None:
                c['error_msg'] = 'Invalid email and/or password'
            else:
                login(request, u)
                return redirectTo('blog:home')
        return render(request, self.template, c)

class RegView(View):
    template = 'accounts/registration.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirectTo('blog:home')
        f = RegistrationForm()
        return render(request, self.template, context={'form': f})

    def post(self, request):
        f = RegistrationForm(request.POST)
        c = {'form': f}
        if f.is_valid():
            first_name = f.cleaned_data['first_name']
            last_name = f.cleaned_data['last_name']
            email = f.cleaned_data['email']
            password = f.cleaned_data['password']
            password_conf = f.cleaned_data['password_conf']
            if password != password_conf:
                c['error_msg'] = 'Password did not match'
            else:
                u = User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
                u.save()
                login(request, u)
                return redirectTo('blog:home')
        return render(request, self.template, context=c)

class ProfileView(View):
    pass

def signOut(request):
    logout(request)
    return redirectTo('blog:home')
