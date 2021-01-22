from django.db import models

from datetime import date


class Dataset(models.Model):

    __tablename__: str = 'dataset'

    id: int = models.AutoField(primary_key=True)
    name: str = models.CharField('Name', max_length=95)
    date: date = models.DateField('Date', auto_now_add=True, db_index=True)
