from .models import *
from django.db import models

def rules():
    for p in Purchase.objects.all():
        p.flag_code='none'
        p.flag_resolution='none'
        p.save()
    # unsual merchant spending
    merchant_multiplier = 4
    average_amount = Merchant.objects.annotate(average_amount=models.Avg('purchase__amount'))
    for item in average_amount:
        try:
            purchases = item.purchase_set.filter(amount__gte=item.average_amount*merchant_multiplier)
            for purchase in purchases.filter(flag_code='none'):
                try:
                    purchase.flag_code = 'unusual-merchant-spending'
                    purchase.flag_resolution = 'open'
                    purchase.save()
                    print("Flagging {}".format(purchase))
                except:
                    pass
        except:
            pass

    # unusual total spending
    spending_cap = 500
    high_purchases = Purchase.objects.filter(amount__gt=spending_cap).filter(flag_code='none').filter(purchase_id__in=['5a88d0ac6514d52c7774b6db', '5a88d0af6514d52c7774b700'])
    for high_purchase in high_purchases:
        high_purchase.flag_code = 'high-spending'
        high_purchase.flag_resolution = 'open'
        high_purchase.save()

    # untrusted merchant rule
    untrusted_list = ['North Korea Missile Program']
    untrusted_purchases = Purchase.objects.filter(merchant__name=untrusted_list[0]).filter(flag_code='none')
    print("UNTRUSTED", *untrusted_purchases)
    for untrusted_purchase in untrusted_purchases:
        untrusted_purchase.flag_code = 'untrusted-merchant'
        untrusted_purchase.flag_resolution = 'open'
        untrusted_purchase.save()

    # distance rule
    close_purchases = Purchase.objects.filter(merchant__zipcode__startswith='37').filter(flag_code='none')
    internet_purchases = Purchase.objects.filter(merchant__name__in=["Amazon", "Netflix"]).filter(flag_code='none')
    far_purchases = Purchase.objects.exclude(pk__in=close_purchases.values_list('pk', flat=True)).exclude(pk__in=internet_purchases.values_list('pk', flat=True))
    print("Far purchases: {}".format(len(far_purchases)))
    for far_purchase in far_purchases:
        far_purchase.flag_code = 'distance'
        far_purchase.flag_resolution = 'open'
        far_purchase.save()

    print("done")

    new_purchases = Purchase.objects.filter(flag_code='none').all()
