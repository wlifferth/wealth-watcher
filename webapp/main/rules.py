from .models import *
from django.db import models

def rules():
    # unsual merchant spending
    merchant_multiplier = 4
    average_amount = Merchant.objects.annotate(average_amount=models.Avg('purchase__amount'))
    for item in average_amount:
        purchases = item.purchase_set.filter(amount__gte=item.average_amount*merchant_multiplier)
        for purchase in purchases.filter(flag_code='none'):
            purchase.flag_code = 'unusual-merchant-spending'
            purchase.flag_resolution = 'open'
            purchase.save()
            print("Flagging {}".format(purchase))

    # unusual total spending
    spending_cap = 1000
    high_purchases = Purchase.objects.filter(amount__gt=spending_cap).filter(flag_code='none')
    for high_purchase in high_purchases:
        high_purchase.flag_code = 'high-spending'
        purchase.flag_resolution = 'open'
        high_purchase.save()

    # distance rule

    print("done")

    new_purchases = Purchase.objects.filter(flag_code='none').all()
