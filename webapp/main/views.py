from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def splash(request):
    context = {}
    return render(request, 'main/splash.html', context)

def users(request):
    context = {}
    ups = UserProfile.objects.all()
    data = ""
    for up in ups:
        data += str(up)
    return HttpResponse(data)

def user(request, user_id):
    context = {}
    up = UserProfile.objects.filter(user_id=user_id).get()
    account = up.account_set.get()
    purchases = account.purchase_set.all()
    data = ""
    for purchase in purchases:
        data += str(purchase) + '<br>'
    return HttpResponse(data)

def dashboard(request):
    context = {}
    user_id = 1
    up = UserProfile.objects.filter(user_id=user_id).get()
    account = up.account_set.get()
    purchases = account.purchase_set.all()
    context['transactions'] = purchases
    return render(request, 'main/dashboard.html', context)
