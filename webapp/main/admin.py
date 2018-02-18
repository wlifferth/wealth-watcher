from django.contrib import admin

# Register your models here.
from .models import UserProfile, Account, Purchase, Merchant, Transfer

admin.site.register(UserProfile)
admin.site.register(Account)
admin.site.register(Purchase)
admin.site.register(Merchant)
admin.site.register(Transfer)