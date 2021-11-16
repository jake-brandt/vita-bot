import pandas as pd

class FoodDataService():
    _dataset = None
    _cached_ids = None

    def __init__(self):
        self._dataset = pd.read_csv('data/food.csv').set_index('fdc_id')

    def get_unique_ids(self):
        '''
        Returns a standard `list` of all FDC IDs in the collection
        '''

        if self._cached_ids is None:
            self._cached_ids = list(self._dataset.index.unique())

        return self._cached_ids
