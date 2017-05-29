from customuser.forms import UserLoginForm, UserSignupForm
from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.base import TemplateView, View


class HomeView(TemplateView):

    template_name = 'home/home.html'
    template_main = 'home/index.html'

    def get(self, request, *args, **kwargs):
        template = self.template_name
        if request.user.is_authenticated:
            template = self.template_main
        ctx = {
            'form': kwargs.get('form'),
            'next': request.GET.get('next')
        }
        return render(request, template, ctx)


class LoginView(TemplateView):

    template_name = 'home/login.html'
    form = UserLoginForm

    def post(self, request, *args, **kwargs):
        form = self.form(data=request.POST, request=request)
        if form.is_valid():
            user = form.user
            login(request, user)
            next_url = request.POST.get('next')
            if next_url:
                return HttpResponseRedirect(next_url)
            # If the user has only one company redirects to it.
            return redirect('home_app:home')
        # Get the form with its errors and go to get method to let it decide the
        # template.
        kwargs['form'] = form
        return self.get(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home_app:home')
        # Get the form with its errors and go to get method to let it decide the
        ctx = {
            'form': kwargs.get('form'),
            'next': request.GET.get('next')
        }
        return render(request, self.template_name, ctx)


class LogoutView(View):

    @transaction.atomic
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('home_app:login'))


class SignupView(TemplateView):
    template_name = 'home/signup.html'
    message = None

    def get_context_data(self, **kwargs):
        context = super(SignupView, self).get_context_data(**kwargs)
        context['message'] = self.message
        return context

    def post(self, request, *args, **kwargs):
        form = UserSignupForm(data=request.POST)
        if form.is_valid():
            # user = form.save()
            # Logging the user.
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            logged_user = authenticate(username=username, password=password)
            if logged_user is not None:
                login(request, logged_user)
                return redirect(reverse('home_app:home'))
        else:
            try:
                key = form.errors.keys()[0]
                self.message = form.errors.get(key)[0]
            except Exception as error:
                print(error)
                self.message = 'Los datos ingresados son erroneos.'
        return self.get(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(reverse('home_app:home'))
        return super(SignupView, self).get(request, *args, **kwargs)
