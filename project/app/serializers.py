from rest_framework import serializers


class RefbookSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    code = serializers.CharField()
    name = serializers.CharField()


class RefbookElementSerializer(serializers.Serializer):
    code = serializers.CharField()
    value = serializers.CharField()
