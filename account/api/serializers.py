from rest_framework import serializers
from account.models import Account

class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['phone_number', 'username', 'email','password']
        extra_kwargs = { 
                    'password': {'write_only' : True}
        }

    def save(self):
        account = Account(
                    email=self.validated_data['email'],
                    username=self.validated_data['username'],
                    phone_number=self.validated_data['phone_number'],

        )
        password = self.validated_data['password']

        account.set_password(password)
        account.save()
        return account