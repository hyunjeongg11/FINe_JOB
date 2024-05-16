from rest_framework import serializers
from .models import Deposit_Products, Deposit_Options, Saving_Products, Saving_Options

# Deposit
class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit_Options
        fields = '__all__'
        read_only_fields = ('deposit_product',)


class DepositProductsSerializer(serializers.ModelSerializer):
    deposit_options = DepositOptionsSerializer(many=True, read_only=True)
    class Meta:
        model = Deposit_Products
        fields = '__all__'


class DepositProductDetailSerializer(serializers.ModelSerializer):
    deposit_options = DepositOptionsSerializer(many=True, read_only=True)
    class Meta:
        model = Deposit_Products
        fields = '__all__'


# Saving
class SavingOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving_Options
        fields = '__all__'
        read_only_fields = ('saving_product',)


class SavingProductsSerializer(serializers.ModelSerializer):
    saving_options = SavingOptionsSerializer(many=True, read_only=True)
    class Meta:
        model = Saving_Products
        fields = '__all__'

class SavingProductDetailSerializer(serializers.ModelSerializer):
    saving_options = SavingOptionsSerializer(many=True, read_only=True)
    class Meta:
        model = Saving_Products
        fields = '__all__'