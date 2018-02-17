# this is Brent's api key
import requests

apiKey = 'f515af811125f9dea31a755fe628357e'

url = 'http://api.reimaginebanking.com/data?type=Accounts&key={}'.format(apiKey)
response = requests.delete(url)
print('Delete Accounts:',response.text)

url = 'http://api.reimaginebanking.com/data?type=Bills&key={}'.format(apiKey)
response = requests.delete(url)
print('Delete Bills:',response.text)

url = 'http://api.reimaginebanking.com/data?type=Customers&key={}'.format(apiKey)
response = requests.delete(url)
print('Delete Customers:',response.text)

url = 'http://api.reimaginebanking.com/data?type=Deposits&key={}'.format(apiKey)
response = requests.delete(url)
print('Delete Deposits:',response.text)

url = 'http://api.reimaginebanking.com/data?type=Loans&key={}'.format(apiKey)
response = requests.delete(url)
print('Delete Loans:',response.text)

url = 'http://api.reimaginebanking.com/data?type=Purchases&key={}'.format(apiKey)
response = requests.delete(url)
print('Delete Purchases:',response.text)

url = 'http://api.reimaginebanking.com/data?type=Transfers&key={}'.format(apiKey)
response = requests.delete(url)
print('Delete Transfers:',response.text)

url = 'http://api.reimaginebanking.com/data?type=Withdrawals&key={}'.format(apiKey)
response = requests.delete(url)
print('Delete Withdrawals:',response.text)
