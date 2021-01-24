import pandas as pd


class RowService:
    _data: None

    def __init__(self, file_path):
        self.file_path = file_path

    def create_row(self):
        self._data = pd.read_csv(self.file_path)

    def set_dataset(self, dataset_id):
        self.create_row()
        return self._data.assign(dataset_id=dataset_id)
