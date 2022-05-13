from rest_framework import serializers
from user.models import User#, UserProfile



# class UserProfileSerializer(serializers.ModelSerializer):
#     user = UserProfileSerializer(many=False)

#     class Meta:
#         model = UserProfile
#         fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'