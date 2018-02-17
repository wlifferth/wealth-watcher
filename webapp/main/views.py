from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def splash(request):
    context = {}
    return render(request, 'main/splash.html', context)
