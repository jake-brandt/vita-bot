import pandas as pd

class FoodDataService():
    _dataset = None

    def __init__(self):
        self._dataset = pd.read_csv('data/food.csv').set_index('fdc_id')

    def get_unique_ids(self):
        return self._dataset.index.unique()
