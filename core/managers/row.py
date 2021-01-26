from typing import List

from django.db.models import Manager


class RowManager(Manager):
    def load_all(self):
        super().all()

    def load_by_dataset_id_and_name(self, dataset_id: int, name: str = None):
        query = super().filter(dataset_id=dataset_id)
        if name:
            query = query.filter(dataset__name=name)

        return query.all()
