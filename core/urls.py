from django.urls import path

from core.views import dataset_view

dataset_urlpatterns = [
    path('', dataset_view)
]

row_urlpatterns = [
    # path('', )
]
