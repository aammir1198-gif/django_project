from rest_framework import serializers

from users.models import User

class UserRegisterSerilizer(serializers.ModelSerializer):

    password2 = serializers.CharField()

    class Meta:

        model = User

        fields = ['full_name' , 'phone_number' , 'age' , 'password' , 'password2']

    def validate(self, attrs):

        if attrs['password'] != attrs['password2']:

            raise serializers.ValidationError({'eror' : 'your frist password is not like your second password'})

        return attrs
    
    def create(self, validated_data):

        validated_data.pop('password2')

        password = validated_data.pop('password')

        validated_data['username'] = validated_data['phone_number']

        user = User.objects.create_user(password=password,**validated_data)

        return user

class UserLoginSerilizer(serializers.Serializer):

    phone_number = serializers.CharField()

    password = serializers.CharField()