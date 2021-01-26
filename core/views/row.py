from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from core.services import RowService


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def row_view(request: Request) -> Response:
    if request.method == 'GET':
        dataset_id = request.query_params.get('dataset_id', None)
        name = request.query_params.get('name', None)
        return RowService.get_all_rows(request, dataset_id=dataset_id, name=name)
    else:
        raise APIException(detail=f'The method {request.method} is invalid.')
