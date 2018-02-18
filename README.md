# wealth-watcher
An app to help you manage your finance and identify potential fraud before it's too late.

## MicroStrategy Visualizations
We'll use MicroStrategy Visualizations to help users understand what's going on with their finances easily.

## CapitalOne Nessie API
Users can easily link their CapitalOne bank accounts so all their financial data is there as soon as they log in.

## AWS Backend
We want to be able to scale up and never leave users without access to the security and peace of mind WealthWatcher provides

## Django App
Django app to stitch it all together

## Anomaly Detection
Using machine learning we can pinpoint transactions that might be fraudulent


# Models

## UserProfile
+ user_id
+ first_name
+ last_name
+ street_number
+ city
+ state
+ zip

## Account
+ account_id
+ user_id
+ balance
+ nickname

## Purchase
+ purchase_id
+ date
+ merchant
+ amount
+ account_id
+ status

## Merchant
+ merchant_id
+ name
+ category
+ street_number
+ city
+ state
+ zip

## Transfer
+ transfer_id
+ date
+ payer_id
+ payee_id
+ amount

# Rules Based Approach

# Distance -- 'distance'
If distance between user and transaction is higher than n, flag as potentially fraudulent

# Untrusted Merchant -- 'untrusted-merchant'
If merchant is not on list of known merchants flag as potentially fraudulent

# Unusual High Spending -- 'unusually-high-spending'
If spending is unusually high, flag as potentially fraudulent

# Unusually High Merchant Spending -- 'unusual-merchant-spending'
If spending is higher than 2x median transaction for vendor, flag as potentially fraudulent
