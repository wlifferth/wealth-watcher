import requests
import json

apiKey = 'f515af811125f9dea31a755fe628357e'

class Customer:
    def Print(self):
        print(self.first_name,self.last_name)
        print('id:',self._id)
        print(self.street_number,self.street_name,self.city,self.state,self.zipcode)


    def __init__(self,jsn):
        self._id = jsn['_id']
        self.first_name = jsn['first_name']
        self.last_name = jsn['last_name']
        self.street_number = jsn['address']['street_number']
        self.street_name = jsn['address']['street_name']
        self.city = jsn['address']['city']
        self.state = jsn['address']['state']
        self.zipcode = jsn['address']['zip']


    @staticmethod
    def GetByAccount(id_):
        url = 'http://api.reimaginebanking.com/accounts/{}/customer?key={}'.format(id_,apiKey)
        return Customer(json.loads(requests.get(url).text))

    @staticmethod
    def GetAll():
        url = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey)
        tmp = json.loads(requests.get(url).text)
        customers = list()
        for v in tmp:
            customers.append(Customer(v))
        return customers

    @staticmethod
    def GetById(id_):
        url = 'http://api.reimaginebanking.com/customers/{}?key={}'.format(id_,apiKey)
        return Customer(json.loads(requests.get(url).text))

    @staticmethod
    def Create(fn,ln,address):
        url = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey)
        var = {
                'first_name': fn,
                'last_name': ln,
                'address': {
                    'street_number': address['street_number'],
                    'street_name': address['street_name'],
                    'city': address['city'],
                    'state': address['state'],
                    'zip': address['zip'],
                    }
                }
        response = requests.post(url,data=json.dumps(var),headers={'content-type':'application/json'})
        return response.status_code

    @staticmethod
    def Update(id_,fn=None,ln=None,address=None):
        url = 'http://api.reimaginebanking.com/customers/{}?key={}'.format(id_,apiKey)
        dct = dict()
        if fn is not None:
            dct['first_name'] = fn
        if ln is not None:
            dct['last_name'] = ln
        if address is not None:
            dct['address'] = {
                    'street_number': address['street_number'],
                    'street_name': address['street_name'],
                    'city': address['city'],
                    'state': address['state'],
                    'zip': address['zip'],
                    }
            response = requests.put(url,data=json.dumps(dct),headers={'content-type':'application/json'})
        return response.status_code


class AccountWrapper:
    def Print(self):
        print(self.nickname,self.type,self._id,self.balance,self.customer_id,self.account_number,self.rewards)

    def __init__(self,jsn_list):
        jsn = jsn_list[0]
        self._id = jsn['_id']
        self.type = jsn['type']
        self.nickname = jsn['nickname']
        self.rewards = jsn['rewards']
        self.balance = jsn['balance']
        self.account_number = jsn['account_number']
        self.customer_id = jsn['customer_id']

    @staticmethod
    def GetAll():
        url = 'http://api.reimaginebanking.com/accounts?key={}'.format(apiKey)
        tmp = json.loads(requests.get(url).text)
        accounts = list()
        for v in tmp:
            accounts.append(AccountWrapper(v))
        return accounts

    @staticmethod
    def GetById(id_):
        url = 'http://api.reimaginebanking.com/accounts/{}?key={}'.format(id_,apiKey)
        return AccountWrapper(json.loads(requests.get(url).text))

    @staticmethod
    def GetByCustomer(id_):
        url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(id_,apiKey)
        return AccountWrapper(json.loads(requests.get(url).text))

    @staticmethod
    def Create(id_,t,n,r,b,a):
        url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(id_,apiKey)
        var = {
                "type": t,
                "nickname": n,
                "rewards": r,
                "balance": b,
                "account_number": a
                }
        response = requests.post(url,data=json.dumps(var),headers={'content-type':'application/json'})
        return response.status_code

    @staticmethod
    def Update(id_,t=None,n=None,r=None,b=None,a=None):
        url = 'http://api.reimaginebanking.com/accounts/{}?key={}'.format(id_,apiKey)
        dct = dict()
        if t is not None:
            dct['type']=t
        if n is not None:
            dct['nickname']=n
        if r is not None:
            dct[rewards]=r
        if b is not None:
            dct['balance']=b
        if a is not None:
            dct['account_number']=a
        print(dct)
        response = requests.put(url,data=json.dumps(dct),headers={'content-type':'application/json'})
        print(response.text)
        return response.status_code

    @staticmethod
    def Delete(id_):
        url = 'http://api.reimaginebanking.com/accounts/{}?key={}'.format(id_,apiKey)
        response = requests.delete(url)
        return response.status_code


class Transfer:
    def __init__(self,jsn):
        self._id = jsn['_id']
        self.type = jsn['type']
        self.transaction_date = jsn['transaction_date']
        self.status = jsn['status']
        self.medium = jsn['medium']
        self.payer_id = jsn['payer_id']
        self.payee_id = jsn['payee_id']
        self.description = jsn['description']

    @staticmethod
    def Delete(id_):
        url = 'http://api.reimaginebanking.com/transfers/{}?key={}'.format(id_,apiKey)
        response = requests.delete(url)
        return response.status_code

    @staticmethod
    def GetById(id_):
        url = 'http://api.reimaginebanking.com/transfers/{}?key={}'.format(id_,apiKey)
        return Transfer(json.loads(requests.get(url).text))

    @staticmethod
    def GetAll():
        url = 'http://api.reimaginebanking.com/accounts/{}/transfers?key={}'.format(id_,apiKey)
        tmp = json.loads(requests.get(url).text)
        transfers = list()
        for v in tmp:
            transfers.append(Customer(v))
        return transfers

    @staticmethod
    def Create(id_,m,p,t,s,d):
        url = 'http://api.reimaginebanking.com/accounts/{}/transfers?key={}'.format(id_,apiKey)
        var = {
                'medium': m,
                'payee_id': p,
                'transaction_date': t,
                'status': s,
                'description': d
                }
        response = requests.post(url,data=json.dumps(var),headers={'content-type':'application/json'})
        return response.status_code

    @staticmethod
    def Update(id_,m=None,p=None,t=None,s=None,d=None):
        dct = dict()
        if m is not None:
            dct['medium']=m
        if p is not None:
            dct['payee_id']=p
        if t is not None:
            dct['transaction_date']=t
        if s is not None:
            dct['status']=s
        if d is not None:
            dct['description']=d
        response = requests.put(url,data=json.dumps(dct),headers={'content-type':'application/json'})
        return response.status_code

class MerchantWrapper:
    def __init__(self,jsn):
        try:
            self._id = jsn['_id']
            self.name = jsn['name']
            self.category = jsn['category']
            self.street_number = jsn['address']['street_number']
            self.street_name = jsn['address']['street_name']
            self.city = jsn['address']['city']
            self.state = jsn['address']['state']
            self.zipcode = jsn['address']['zip']
            self.lat = jsn['geocode']['lat']
            self.lng = jsn['geocode']['lng']
        except:
            pass


    @staticmethod
    def GetAll():
        url = 'http://api.reimaginebanking.com/merchants?key={}'.format(apiKey)
        tmp = json.loads(requests.get(url).text)
        merchants = list()
        for v in tmp:
            merchants.append(MerchantWrapper(v))
        return merchants

    @staticmethod
    def GetById(id_):
        url = 'http://api.reimaginebanking.com/merchants/{}?key={}'.format(id_,apiKey)
        return MerchantWrapper(json.loads(requests.get(url).text))

    @staticmethod
    def Create(n,c,a,g):
        url = 'http://api.reimaginebanking.com/merchants?key={}'.format(apiKey)
        var = {
                'name': n,
                'category': c,
                'address': {
                    'street_number': address['street_number'],
                    'street_name': address['street_name'],
                    'city': address['city'],
                    'state': address['state'],
                    'zip': address['zip']
                    },
                'geocode': {
                    'lat': g['lat'],
                    'lng': g['lng']
                    }
                }
        response = requests.post(url,data=json.dumps(var),headers={'content-type':'application/json'})
        return response.status_code

    @staticmethod
    def Update(id_,n=None,c=None,a=None,g=None):
        url = 'http://api.reimaginebanking.com/merchants/{}?key={}'.format(id_,apiKey)
        dct = dict()
        if n is not None:
            dct['name'] = n
        if c is not None:
            dct['category'] = c
        if a is not None:
            dct['address'] = a
        if g is not None:
            dct['geocode'] = g
        response = requests.put(url,data=json.dumps(dct),headers={'content-type':'application/json'})
        return response.status_code

class PurchaseWrapper:
    def __init__(self,jsn):
        self._id = jsn['_id']
        self.type = jsn['type']
        self.merchant_id = jsn['merchant_id']
        self.payer_id = jsn['payer_id']
        self.purchase_date = jsn['purchase_date']
        self.amount = jsn['amount']
        self.status = jsn['status']
        self.medium = jsn['medium']
        self.description = jsn['description']

    @staticmethod
    def GetAllByAccount(id_):
        url = 'http://api.reimaginebanking.com/accounts/{}/purchases?key={}'.format(id_,apiKey)
        tmp = json.loads(requests.get(url).text)
        purchases = list()
        for v in tmp:
            purchases.append(PurchaseWrapper(v))
        return purchases

    @staticmethod
    def GetAllByMerchant(id_):
        url = 'http://api.reimaginebanking.com/merchants/{}/purchases?key={}'.format(id_,apiKey)
        tmp = json.loads(requests.get(url).text)
        purchases = list()
        for v in tmp:
            purchases.append(PurchaseWrapper(v))
        return purchases

    @staticmethod
    def GetAllByAccountAndMerchant(id_a,id_m):
        url = 'http://api.reimaginebanking.com/merchants/{}/accounts/{}/purchases?key={}'.format(id_m,id_a,apiKey)
        tmp = json.loads(requests.get(url).text)
        purchases = list()
        for v in tmp:
            purchases.append(PurchaseWrapper(v))
        return purchases

    @staticmethod
    def GetById(id_):
        url = 'http://api.reimaginebanking.com/purchases/{}?key={}'.format(id_,apiKey)
        return AccountWrapper(json.loads(requests.get(url).text))

    @staticmethod
    def Create(aid,mid,m,p,a,s,d):
        url = 'http://api.reimaginebanking.com/accounts/{}/purchases?key={}'.format(aid,apiKey)
        var = {
                'merchant_id': mid,
                'medium': m,
                'purchase_date': p,
                'amount': a,
                'status': s,
                'description': d
                }
        response = requests.post(url,data=json.dumps(var),headers={'content-type':'application/json'})
        return response.status_code

    @staticmethod
    def Update(id_,t=None,mid=None,pid=None,pd=None,a=None,s=None,m=None,d=None):
        url = 'http://api.reimaginebanking.com/purchases/{}?key={}'.format(id_,apiKey)
        dct = dict()
        if t is not None:
            dct['type'] = t
        if mid is not None:
            dct['merchant_id'] = mid
        if pid is not None:
            dct['payer_id'] = pid
        if pd is not None:
            dct['purchase_date'] = pd
        if a is not None:
            dct['amount'] = a
        if s is not None:
            dct['status'] = s
        if m is not None:
            dct['medium'] = m
        if d is not None:
            dct['description'] = d
        response = requests.put(url,data=json.dumps(dct),headers={'content-type':'application/json'})
        return response.status_code

    @staticmethod
    def Delete(id_):
        url = 'http://api.reimaginebanking.com/purchases/{}?key={}'.format(id_,apiKey)
        response = requests.delete(url)
        return response.status_code
