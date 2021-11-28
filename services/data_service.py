import pandas as pd
from itertools import zip_longest

class DataService():
    _food_dataset = None
    _food_nutrient_dataset = None
    _nutrient_dataset = None
    _recommended_daily_allowances_dataset = None
    _recommended_daily_maximums_dataset = None
    _cached_fdc_ids = None

    def __init__(self):
        self._food_dataset = pd.read_csv('data/food.csv').set_index('fdc_id')
        self._food_nutrient_dataset = pd.read_csv('data/food_nutrient.csv').set_index(['fdc_id','nutrient_id'])
        self._nutrient_dataset = pd.read_csv('data/nutrients.csv').set_index('id')
        self._recommended_daily_allowances_dataset = pd.read_csv('data/nutrient_recommended_daily_allowances.csv').set_index('nutrient_id')
        self._recommended_daily_maximums_dataset = pd.read_csv('data/nutrient_recommended_daily_maximums.csv').set_index('nutrient_id')

    @property
    def unique_fdc_ids(self):
        '''
        Returns a standard `list` of all FDC IDs in the collection
        '''

        if self._cached_fdc_ids is None:
            self._cached_fdc_ids = list(self._food_dataset.index.unique())

        return self._cached_fdc_ids

    def get_food_nutrients(self, fdc_id):
        '''
        Return all food-nutrient mappings for a given FCD ID
        '''
        return self._food_nutrient_dataset.loc[fdc_id, :]

    def get_nutrients(self, nutrient_ids):
        '''
        Return data for all nutrient IDs requested
        '''
        return self._nutrient_dataset.loc[nutrient_ids]
