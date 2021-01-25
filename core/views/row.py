from typing import Dict

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_202_ACCEPTED
from rest_framework.exceptions import APIException

from core.services import RowService


@api_view(['GET'])
def row_view(request: Request) -> Response:
    if request.method == 'GET':
        dataset_id = request.query_params.get('dataset_id', None)
        return RowService.get_all_rows(request, dataset_id=dataset_id)
    else:
        raise APIException(detail=f'The method {request.method} is invalid.')
''