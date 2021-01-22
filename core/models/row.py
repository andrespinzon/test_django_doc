from django.db import models
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models import PointField
from django.contrib.auth.models import User

from core.models import Dataset


class Row(models.Model):
    __tablename__: str = 'row'

    id: int = models.AutoField(primary_key=True)
    dataset: Dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    point: Point = PointField('Point')
    client: User = models.ForeignKey(User, on_delete=models.CASCADE)
    client_name: str = models.CharField('Client Name', max_length=45)
