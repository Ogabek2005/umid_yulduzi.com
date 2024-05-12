from rest_framework import serializers
from . import models
class PetitonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Petittion
        fields = "__all__"