from rest_framework.serializers import ModelSerializer, SerializerMethodField

from core.models import Row


class RowSerializer(ModelSerializer):
    class Meta:
        model = Row
        fields = ('id', 'dataset_id', 'point', 'client_id', 'client_name')
