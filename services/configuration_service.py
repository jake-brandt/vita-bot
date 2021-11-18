import pandas as pd

class ConfigurationService(object):
    _recipe_size: int = 5
    _required_base_foods: list = None

    @property
    def recipe_size(self):
        '''The number of ingredients in recipes'''
        return self._recipe_size

    @property
    def required_base_foods(self):
        '''At least one of these FDC IDs must be present in a recipe'''
        if self._required_base_foods is None:
            self._required_base_foods = pd.read_csv('config/food_required_base.csv')["fdc_id"].tolist()
        return self._required_base_foods
