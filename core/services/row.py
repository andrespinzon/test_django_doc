import pandas as pd


class RowService:

    def __init__(self, file_path):
        self.file_path = file_path

    def create_row(self):
        print(pd.read_csv(self.file_path))

