from rest_framework import serializers

class AccountSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=120)
    date_of_birth = serializers.DateField
