from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic.base import TemplateView

def home(request):
    return render(request, 'home.html')

def homemain(request):
    return render(request, 'homemain.html')

def my_logout(request):
    logout(request)
    return redirect('home')

class HomePageView(TemplateView):
    template_name = 'home2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['minha_variavel'] = 'Olá, seja bem vindo ao curso de Django advanced'
        return context