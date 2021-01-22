from typing import Dict

from django.contrib.auth.models import User

from core.services import RowService
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

        print(self._data)


