from .nessie import *
from .models import *

cid = "5a88c0326514d52c7774b548"
aid = "5a88c0af6514d52c7774b549"


def LoadUser():
    customer = Customer.GetById(cid)
    accounts = AccountWrapper.GetByCustomer(cid)
    print(type(accounts))
    print(accounts)
    merchants = MerchantWrapper.GetAll()
    """
    merchants = list()
    merchants.append(MerchantWrapper.GetByID())
    """
    purchases = list()
    for a in [accounts]:
        purchases.append(PurchaseWrapper.GetAllByAccount(a._id))
    return customer,accounts,merchants,purchases


def sync():
    customer,accounts,merchants,purchases = LoadUser()
    if UserProfile.objects.count() == 0:
        c = UserProfile.objects.create(
                user_id=customer._id,
                first_name=customer.first_name,
                last_name=customer.last_name,
                street_number=customer.street_number,
                city=customer.city,
                state=customer.state,
                zip=customer.zipcode
                )
        c.street_number+=' '
        c.street_number+=customer.street_name
        c.save()
    else:
        print("yo")
    user_objects= UserProfile.objects.filter(user_id=accounts.customer_id)
    for uo in user_objects:
        print(uo)
    if Account.objects.count() == 0:
        for var in [accounts]:
            a = Account.objects.create(
                    account_id=var._id,
                    user_profile=UserProfile.objects.filter(user_id=var.customer_id).get(),
                    balance=var.balance,
                    nickname=var.nickname
                    )
            a.save()
    else:
        print("We averted disaster!")

    new_count = 0
    for var in merchants:
        try:
            if Merchant.objects.filter(merchant_id=var._id).count() == 0:
                m = Merchant.objects.create(
                        merchant_id = var._id,
                        name = var.name,
                        category = var.category,
                        street_number = var.street_number,
                        city = var.city,
                        state = var.state,
                        zipcode = var.zipcode
                        )
                m.street_number+=' '
                m.street_number+=customer.street_name
                m.save()
                new_count += 1
        except:
            pass
    print("NEW COUNT: {}".format(new_count))
    new_count = 0
    for lst in purchases:
        for pur in lst:
            if Purchase.objects.filter(purchase_id=pur._id).count() == 0:
                try:
                    p = Purchase.objects.create(
                            purchase_id = pur._id,
                            date = pur.purchase_date,
                            merchant = Merchant.objects.filter(merchant_id=pur.merchant_id).get(),
                            account = Account.objects.filter(account_id=pur.payer_id).get(),
                            amount = pur.amount,
                            status = pur.status
                            )
                    p.save()
                    new_count += 1
                except:
                    pass
    print("NEW COUNT: {}".format(new_count))
    Account.objects.update(account_id=1)
    UserProfile.objects.update(user_id=1)

