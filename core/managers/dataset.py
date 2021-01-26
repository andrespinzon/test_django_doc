from typing import List

from django.db.models import Manager


class DatasetManager(Manager):

    def load_all(self) -> List:
        return super().all().order_by('id')
