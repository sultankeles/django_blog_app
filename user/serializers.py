from rest_framework import serializers

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token

from dj_rest_auth.serializers import TokenSerializer


class RegisterSerializer(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()

    email = serializers.EmailField(
        required = True,
        validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password],
        style = {'input_type':'password'}
        )
    password2 = serializers.CharField(write_only = True, required = True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'password',
            'password2',
        )

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({
                'message':'The entered passwords did not match. Please enter again.'
            })
        return data
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password2')
        
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def get_token(self, obj):
        token = Token.objects.get(user=obj)
        return token.key 
    
    
class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')


class CustomTokenSerializer(TokenSerializer):
    user = UserTokenSerializer(read_only=True)

    class Meta:
        model = Token
        fields = ('key', 'user')