from rest_framework import serializers


class VacancySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    text = serializers.CharField(max_length=2000)
    status = serializers.CharField(max_length=6)
    created = serializers.DateField()
    username = serializers.CharField(max_length=100)
