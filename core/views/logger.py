from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_202_ACCEPTED
from django.shortcuts import render

from common.logger import get_all_logger


@api_view(['GET'])
def logger_view(request: Request) -> Response:
    data = get_all_logger()
    return Response(data=data, status=HTTP_202_ACCEPTED)


def all_logger_view(request: Request) -> render:
    return render(request, 'core/logger.html')
