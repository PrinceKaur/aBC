from rest_framework import serializers
from django.contrib.auth.models import User
from task.models import products,User1

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email','password')
        
class Register1Serializer(serializers.ModelSerializer):
    class Meta:
        model = User1       
        USER_CHOICES = (
            (1, 'seller'),
            (2, 'buyer'))
        choices = serializers.ChoiceField(
                        choices = USER_CHOICES)
        

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = ('product_name',
                  'product_price', 'product_quantity')


# class CurrencySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = currency
#         fields=('Amount','Choose_Currency','Select_Bank','Bank_Account_Number','IFCSno')