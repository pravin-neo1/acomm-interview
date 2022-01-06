from rest_framework import serializers


class SolutionSerializer(serializers.Serializer):
    A = serializers.ListField(child=serializers.IntegerField(min_value=1, max_value=100000))
    X = serializers.IntegerField(min_value=1, max_value=100000)
    time_req = serializers.IntegerField(min_value=1, max_value=100000, read_only=True)
