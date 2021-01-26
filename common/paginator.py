from rest_framework.pagination import PageNumberPagination
from constance import config


class CustomPagination(PageNumberPagination):
    max_page_size = 200
    last_page_strings = ('the_end',)
