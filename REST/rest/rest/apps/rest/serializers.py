from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from .models import Submission


class SubmissionSerializer(serializers.ModelSerializer):
    """
    Submission serializer
    """

    class Meta:
        model = Submission
        fields = "__all__"


class KnapsackItemSerializer(serializers.Serializer):
    weight = serializers.IntegerField()
    value = serializers.IntegerField()


class KnapsackSerializer(serializers.Serializer):
    max_weight = serializers.IntegerField()
    items = KnapsackItemSerializer(many=True)


class KnapsackOutputSerializer(serializers.Serializer):
    max_value = serializers.IntegerField()
