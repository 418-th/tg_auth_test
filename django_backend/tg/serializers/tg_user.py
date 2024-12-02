from rest_framework import serializers


class TgUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    username = serializers.CharField(max_length=64, required=True)
    first_name = serializers.CharField(max_length=64, required=True)
    last_name = serializers.CharField(max_length=64, required=True)
