from typing import Dict

from django.contrib.auth.models import User
from django.db.transaction import atomic as atomic_transaction
from rest_framework.exceptions import APIException
from concurrent.futures import ThreadPoolExecutor

from core.models import Dataset
from core.services.row import RowService
from common.validations import validate_allowed_fields, validate_allowed_type_files, \
    validate_allowed_fields_filters, validate_required_fields


class DatasetService:

    _data: Dict

    def upload_dataset(self, file: Dict, user: User):
        self._data = file

        fields = {'file'}
        validate_required_fields(data=self._data, required_fields=fields)
        validate_allowed_fields(data=self._data, allowed_fields=fields)
        validate_allowed_type_files(data=self._data, field='file', type_files={'csv'})
        file = self._data['file']
        self._data.pop('file')

        try:
            with atomic_transaction():
                # TODO: Create dataset
                dataset = Dataset.objects.create(**self._data)
                # TODO: Read file
                print(dataset)
                service = RowService(file_path=file)
                data = service.set_dataset(dataset_id=dataset.id)
                print(data)
                # TODO: Insert data file in row table
        except:
            raise APIException()
