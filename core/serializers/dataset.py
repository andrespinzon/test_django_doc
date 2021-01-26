from rest_framework.serializers import ModelSerializer

from core.models import Dataset


class DatasetSerializer(ModelSerializer):
    class Meta:
        model = Dataset
        fields = ('id', 'name')