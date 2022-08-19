from rest_framework import serializers
from . models import ADDDATA

class AlldataSerializer(serializers.ModelSerializer):
    # Name=serializers.CharField(max_length=100,required=False,allow_null=True)
    # Number=serializers.CharField(max_length=100,required=False,allow_null=True)
    # Location=serializers.CharField(max_length=100,required=False,allow_null=True)
    class Meta:
        model = ADDDATA
        fields = ['id','Name','Number','Location']


class adddataSerializer(serializers.ModelSerializer):
    Name=serializers.CharField(max_length=100,required=False,allow_null=True)
    Number=serializers.CharField(max_length=100,required=False,allow_null=True)
    Location=serializers.CharField(max_length=100,required=False,allow_null=True)
    class Meta:
        model = ADDDATA
        fields = ['Name','Number','Location']

class upddataSerializer(serializers.ModelSerializer):
    id=serializers.CharField(max_length=100,required=False,allow_null=True)
    Name=serializers.CharField(max_length=100,required=False,allow_null=True)
    Number=serializers.CharField(max_length=100,required=False,allow_null=True)
    Location=serializers.CharField(max_length=100,required=False,allow_null=True)
    class Meta:
        model = ADDDATA
        fields = ['id','Name','Number','Location']