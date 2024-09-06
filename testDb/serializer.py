from rest_framework import serializers
from .models import User
from .response_messages import ResponseMessage


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate_name(self, value):
        if User.objects.filter(name=value).exists():
            raise serializers.ValidationError(ResponseMessage.NAME_EXISTS)
        return value

    def validate_age(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                ResponseMessage.AGE_LESS_THAN_ZERO)
        elif value > 100:
            raise serializers.ValidationError(
                ResponseMessage.AGE_GREATER_THAN_HUNDRED)
        return value
