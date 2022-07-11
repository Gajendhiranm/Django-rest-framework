from rest_framework import serializers

class CustomerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length = 255)
    last_name = serializers.CharField(max_length = 255)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=255)
    birth_date = serializers.DateField()