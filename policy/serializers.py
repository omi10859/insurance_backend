import re
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import UserPolicy


class UserPolicySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserPolicy
        fields = '__all__'

class UserPolicyUpdateSerializer(serializers.ModelSerializer):
    
    def validate_premium(self, value):
        if value > 1000000:
            raise ValidationError("Value can't be more then one million")
        
        return value

    class Meta:
        model = UserPolicy
        exclude = ('date_of_purchase', )
