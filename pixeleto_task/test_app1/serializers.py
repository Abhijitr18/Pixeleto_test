from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User


class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','phone']

    # def create(self, validated_data):
    #     return User.objects.create(validated_data)
    #
    # def update(self,instance,validated_data):
    #     instance.id = validated_data.get('id',instance.id)
    #     instance.username = validated_data.get('username',instance.username)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.phone = validated_data.get('phone', instance.phone)
    #     instance.save()
    #     return instance

    def validate(self,data):
        print(type(data['email']))
        if not (str(data['email']).endswith(".com")):
            raise serializers.ValidationError("not valid mail")
        return data


