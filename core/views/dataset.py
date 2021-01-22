from typing import Dict

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from core.services import DatasetService


@api_view(['POST'])
def dataset_view(request: Request) -> Response:
    service: DatasetService = DatasetService()
    data: Dict = service.upload_dataset(file=request.FILES, user=request.user)
    return Response(data=data, status=HTTP_201_CREATED)
