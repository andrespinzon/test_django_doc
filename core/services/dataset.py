from typing import Dict

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.transaction import atomic as atomic_transaction
from rest_framework.exceptions import APIException
from rest_framework.request import Request
from rest_framework.status import HTTP_400_BAD_REQUEST

from common.paginator import CustomPagination
from core.models import Dataset, Row
from core.serializers import DatasetSerializer
from core.services.row import RowService
from common.validations import validate_allowed_fields, validate_allowed_type_files, \
    validate_allowed_fields_filters, validate_required_fields

from constance import config

class DatasetService:

    _data: Dict

    def upload_dataset(self, request: Request, user: User):
        self._data = request.data

        fields = {'file', 'name'}
        validate_required_fields(data=self._data, required_fields=fields)
        validate_allowed_fields(data=self._data, allowed_fields=fields)
        validate_allowed_type_files(data=self._data, field='file', type_files={'csv'})

        try:
            with atomic_transaction():
                dataset = Dataset.objects.create(**{'name': self._data.get('name')})
                service = RowService(file_path=self._data['file'], dataset_id=dataset.id)
                row_objects = service.create_rows()
                Row.objects.bulk_create(row_objects)
        except ValidationError as error:
            raise APIException(
                detail=f'The operation is invalid. Message: {error.messages[0]}',
                code=HTTP_400_BAD_REQUEST
            )

    @staticmethod
    def get_dataset(request: Request):
        paginator = CustomPagination()
        paginator.page_size = config.PAG_DATASET
        datasets = Dataset.objects.load_all()
        datasets = paginator.paginate_queryset(datasets, request)
        data = DatasetSerializer(
            instance=datasets,
            many=True
        ).data
        return paginator.get_paginated_response(data)

