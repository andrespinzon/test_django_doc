import pandas as pd

from django.contrib.gis.geos import Point
from rest_framework.exceptions import APIException
from rest_framework.request import Request
from constance import config

from common.logger import create_logger
from common.paginator import CustomPagination
from core.models import Row
from core.serializers import RowSerializer


class RowService:
    _data: None

    def __init__(self, file_path, dataset_id):
        self._file_path = file_path
        self._dataset_id = dataset_id

    def read_csv_file(self):
        self._data = pd.read_csv(self._file_path)

    def set_dataset(self):
        self._data = self._data.assign(dataset_id=self._dataset_id)

    def create_rows(self):
        self.read_csv_file()
        self.set_dataset()
        return [
            Row(
                point=Point(row['lat'], row['lon']),
                client_id=row['client_id'],
                client_name=row['client_name'],
                dataset_id=row['dataset_id'],
            ) for i, row in self._data.iterrows()
        ]

    @staticmethod
    def get_all_rows(request: Request, dataset_id: int, name: str):
        if not dataset_id:
            raise APIException(detail='The query param dataset_id is required.')
        create_logger(request=request, user=request.user)
        paginator = CustomPagination()
        paginator.page_size = config.PAG_ROW
        rows = Row.objects.load_by_dataset_id_and_name(dataset_id=dataset_id, name=name)
        rows = paginator.paginate_queryset(rows, request)

        data = RowSerializer(
            instance=rows,
            many=True
        ).data
        return paginator.get_paginated_response(data)


