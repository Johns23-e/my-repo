from django.shortcuts import render

context = {'title': 'Django Project'}
# Create your views here.
def base(request):
    return render(request, 'base.html', context)

def home(request):
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', context)