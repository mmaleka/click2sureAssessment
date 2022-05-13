from rest_framework import serializers
from transaction.models import Transaction
from account.api.serializers import AccountSerializer


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        # fields = '__all__'
        fields = [
            'account',
            'user',
            'action',
            'amount'
        ]


class USerTransactionSerializer(serializers.ModelSerializer):
    account = AccountSerializer(many=False)
    class Meta:
        model = Transaction
        fields = '__all__'