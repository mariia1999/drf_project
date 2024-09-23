from rest_framework import serializers
from users.models import Payment, User
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(ModelSerializer):
    payment_history = SerializerMethodField()

    def get_payment_history(self, obj):
        payments = obj.payment_set.all()
        return PaymentSerializer(payments, many=True).data

    class Meta:
        model = User
        fields = ('username', 'email', 'payment_history',)
        



