from nessie import *


def LoadUser(cid):
    customer = Customer.GetById(cid)
    accounts = Account.GetByCustomer(cid)
    merchants = Merchant.GetAll()
    purchases = list()
    for a in accounts:
        purchases.append(Purchase.GetAllByAccount(a._id))
    return customer,accounts,merchants,purchases


