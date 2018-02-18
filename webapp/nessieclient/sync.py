from nessie import *
import sys
sys.path.insert(0,'webapp/main')
from models import *

cid = "5a88c0326514d52c7774b548"
aid = "5a88c0af6514d52c7774b549"


def LoadUser():
    customer = Customer.GetById(cid)
    accounts = Account.GetByCustomer(cid)
    merchants = Merchant.GetAll()
    purchases = list()
    for a in accounts:
        purchases.append(Purchase.GetAllByAccount(a._id))
    return customer,accounts,merchants,purchases


def sync():
    customer,accounts,merchants,purchases = LoadUser()
    c = UserProfile.objects.create(
            user_id=customer._id,
            first_name=customer.first_name,
            last_name=customer.last_name,
            street_number=customer.street_number,
            city=customer.city,
            state=customer.state,
            zipcode=customer.zipcode
            )
    c.street_number+=' '
    c.street_number+=customer.street_name
    c.save()

    for var in accounts:
        a = Account.objects.create(
                account_id=var._id,
                user_profile=UserProfile.objects.filter(user_id=var.customer_id).get(),
                balance=var.balance,
                nickname=var.nickname
                )
        a.save()

    for var in merchants:
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

    for lst in purchases:
        for pur in lst:
            p = Purchase.objects.create(
                    purchase_id = pur._id,
                    date = pur.purchase_date,
                    merchant = Merchant.objects.filter(merchant_id=pur.merchant_id).get(),
                    account = Account.objects.filter(account_id=aid).get(),
                    amount = pur.amount,
                    status = pur.status
                    )
            p.save()
