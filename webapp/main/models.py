from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street_number = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)

    def __str__(self):
        return "UserProfile({} {})".format(self.first_name, self.last_name)

class Account(models.Model):
    account_id = models.IntegerField()
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    balance = models.FloatField()
    nickname = models.CharField(max_length=100)

class Merchant(models.Model):
    merchant_id = models.IntegerField()
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    street_number = models.TextField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)

class Purchase(models.Model):
    purchase_id = models.IntegerField()
    date = models.DateField()
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)

class Transfer(models.Model):
    transfer_id = models.IntegerField()
    date = models.DateField()
    payer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='payer')
    payee = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='payee')
    amount = models.FloatField()
