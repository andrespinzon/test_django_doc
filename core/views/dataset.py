from typing import Dict

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.exceptions import APIException

from core.services import DatasetService


@api_view(['POST', 'GET'])
def dataset_view(request: Request) -> Response:

    if request.method == 'POST':
        service: DatasetService = DatasetService()
        data: Dict = service.upload_dataset(request=request, user=request.user)
        return Response(data=data, status=HTTP_201_CREATED)
    elif request.method == 'GET':
        pass
    else:
        raise APIException(detail=f'The method {request.method} is invalid.')