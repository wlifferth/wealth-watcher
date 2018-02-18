from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from . import rules, sync

flag_messages = {
    'unusual-merchant-spending': "We tagged this transaction as potentially fraudulent because you normally spend much less when you make a transaction with this merchant. If you'd like this kind of transaction to not be flagged in the future, head to the settings page and change Merchant Threshold to a higher value.",
    'high-spending': "We tagged this transaction as potentially fraudulent because of the high dollar amount. If you'd like this kind of transaction to not be flagged in the future, head to the settings page and change Absolute Threshold to a higher value.",
    'distance': "We tagged this transaction as potentially fraudulent because it occured a large distance away from where you normally make transactions. If you'd like this kind of threshold to not be flagged in the future, head to the settings page and change Distance Threshold to a higher value.",
    'untrused-merchant': "We tagged this transaction as potentially fraudulent because it was placed with a merchant that's known to be unreliable. If you'd like this kind of transaction to not be flagged in the future, head to the <strong>settings</strong> page and change Flag Untrusted Merchants to OFF",
    'high-flag-score': "We flagged this transaction as potentially fraudulent because it recieved a high score from our anomaly detection algorithm. We can't be sure why, but it shows some similarities with other fraudulent transactions we've seen. If you'd like this kind of transaction to not be flagged in the future, head to the settings page and change Anomaly Detection Threshold to a lower setting.",
}

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
    purchases = account.purchase_set.order_by('-date').all()
    context['transactions'] = purchases
    return render(request, 'main/dashboard.html', context)

def alerts(request):
    context = {}
    purchases = Purchase.objects.filter(flag_resolution='open')
    for purchase in purchases:
        purchase.flag_message = flag_messages[purchase.flag_code]
        print(purchase)
    context['alerts'] = purchases
    return render(request, 'main/alerts.html', context)


def run_rules(request):
    rules.rules()
    return HttpResponse("rules have been run")

def run_sync(request):
    sync.sync()
    return HttpResponse("sync has been run")

def log_in(request):
    context = {}
    return render(request, 'main/login.html', context)
