from typing import Dict

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.exceptions import APIException

from core.services import DatasetService


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated, ])
def dataset_view(request: Request) -> Response:
    if request.method == 'POST':
        service: DatasetService = DatasetService()
        data: Dict = service.upload_dataset(request=request)
        return Response(data=data, status=HTTP_201_CREATED)
    elif request.method == 'GET':
        return DatasetService.get_all_dataset(request)
    else:
        raise APIException(detail=f'The method {request.method} is invalid.')
