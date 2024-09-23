from rest_framework import serializers
from users.models import Payment, User


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(ModelSerializer):
    payment_history = PaymentSerializer(many=True)


    class Meta:
        model = User
        fields = ('username', 'email', 'payment_history',)




