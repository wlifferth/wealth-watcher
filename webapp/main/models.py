from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user_id = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street_number = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)

    def __str__(self):
        return "UserProfile({} {})".format(self.first_name, self.last_name)

class Account(models.Model):
    account_id = models.CharField(max_length=100)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    balance = models.FloatField()
    nickname = models.CharField(max_length=100)

class Merchant(models.Model):
    merchant_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    street_number = models.TextField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)

    def __str__(self):
        return "Merchant({})".format(self.name)

class Purchase(models.Model):
    purchase_id = models.CharField(max_length=100)
    date = models.DateField()
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.FloatField()
    status = models.CharField(max_length=100, default="completed")
    flag_rating = models.FloatField(default=0)
    flag_code = models.CharField(max_length=100, default='none')
    flag_resolution = models.CharField(max_length=100, default='none')

    def __str__(self):
        return "Purchase(${} at {})".format(self.amount, self.merchant.name)

class Transfer(models.Model):
    transfer_id = models.CharField(max_length=100)
    date = models.DateField()
    payer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='payer')
    payee = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='payee')
    amount = models.FloatField()
