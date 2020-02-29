from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from accounts import forms
# Create your views here.


class HomePage(TemplateView):
    template_name = 'index.html'


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')


class Test(TemplateView):
    template_name = 'test.html'


class Thanks(TemplateView):
    template_name = 'thanks.html'
