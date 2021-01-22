from typing import Dict

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED


@api_view(['POST'])
def dataset_view(request: Request) -> Response:
    data: Dict = {}
    return Response(data=data, status=HTTP_201_CREATED)
