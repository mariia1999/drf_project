from rest_framework import serializers
from users.models import Payment, User
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(ModelSerializer):
    payment_history = PaymentSerializer(many=True)
    
    class Meta:
        model = User
        fields = ('email', 'city', 'payment_history',)
        



