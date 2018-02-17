#users
#accounts
#transactions

import requests
import json

apiKey = 'f515af811125f9dea31a755fe628357e'

class Customer:
    def __init__(self,jsn):
        self._id = jsn['_id']
        self.first_name = jsn['first_name']
        self.last_name = jsn['last_name']
        self.street_number = jsn['account']['street_number']
        self.street_name = jsn['account']['street_name']
        self.city = jsn['account']['city']
        self.state = jsn['account']['state']
        self.zipcode = jsn['account']['zip']

    @staticmethod
    def GetByAccount(id_):
        url = 'http://api.reimaginebanking.com/accounts/{}/customer?key={}'.format(id_,apiKey)
        return Customer(json.loads(requests.get(url)))

    @staticmethod
    def GetAll():
        url = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey)
        tmp = json.loads(requests.get(url))
        for v in tmp:
            customers.append(Customer(v))
        return customers

    @staticmethod
    def GetById(id_):
        url = 'http://api.reimaginebanking.com/customers/{}?key={}'.format(id_,apiKey)
        return Customer(json.loads(requests.get(url)))

    @staticmethod
    def Create(fn,ln,address):
        url = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey)
        var = {
                'first_name': fn,
                'last_name': ln,
                'address': {
                    'street_number': address['street_number']
                    'street_name': address['street_name']
                    'city': address['city']
                    'state': address['state']
                    'zip': address['zip']
                    }
                }
        response = requests.post(url,data=json.dumps(var),headers={'content-type':'application/json'})
        return response.status_code

    @staticmethod
    def Update(id_,fn=None,ln=None,address=None):
        url = 'http://api.reimaginebanking.com/customers/{}?key={}'.format(id_,apiKey)
        if fn is not None:
            dct['first_name'] = fn
        if ln is not None:
            dct['last_name'] = ln
        if address is not None:
            dct['address'] = {
                    'street_number': address['street_number']
                    'street_name': address['street_name']
                    'city': address['city']
                    'state': address['state']
                    'zip': address['zip']
                    }
        response = requests.put(url,data=json.dumps(dct),headers={'content-type':'application/json'})
        return response.status_code



class Account:
    def __init__(self,jsn):
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
        tmp = json.loads(requests.get(url))
        for v in tmp:
            accounts.append(Account(v))
        return accounts

    @staticmethod
    def GetById(id_):
        url = 'http://api.reimaginebanking.com/accounts/{}?key={}'.format(id_,apiKey)
        return Account(json.loads(requests.get(url)))

    @staticmethod
    def GetByCustomer(id_):
        url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(id_,apiKey)
        return Account(json.loads(requests.get(url)))

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
        response = requests.put(url,data=json.dumps(dct),headers={'content-type':'application/json'})
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
    def GetById(id_)
        url = 'http://api.reimaginebanking.com/transfers/{}?key={}'.format(id_,apiKey)
        return Transfer(json.loads(requests.get(url)))

    @staticmethod
    def GetAll()
        url = 'http://api.reimaginebanking.com/accounts/{}/transfers?key={}'.format(id_,apiKey)
        tmp = json.loads(requests.get(url))
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
