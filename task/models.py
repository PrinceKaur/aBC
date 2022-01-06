from django.db import models
from django.contrib.auth.models import User

class products(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()
   

class user2(models.Model):
	# seller = models.BooleanField(default=False)
 #    buyer = models.BooleanField(default=False)

	user1 = models.ForeignKey(products, on_delete=models.CASCADE)

class User1(models.Model):


    USER_CHOICES = (
        ('1', 'seller'),
        ('2', 'buyer')
        
    )
    
    user_choice = models.CharField(max_length=2, choices=USER_CHOICES)
    User1 = models.ForeignKey(User, on_delete=models.CASCADE)

# 

# class currency(models.Model):
#     Amount=models.CharField(max_length=200)
#     Choose_Currency=models.CharField(max_length=200)
#     select_Bank=models.CharField(max_length=200)
#     Bank_Account_Number=models.CharField(max_length=200)
#     IFCSno=models.CharField(max_length=200)
   
