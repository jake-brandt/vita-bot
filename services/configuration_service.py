import pandas as pd

class ConfigurationService(object):
    _smoothie_mass_g: float = 340
    _recipe_size: int = 5
    _required_base_foods: list = None
    _minimum_base_food_mass_g: float = 110

    @property
    def smoothie_mass_g(self):
        '''Total mass of an ideal smoothie, in grams'''
        return self._smoothie_mass_g

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

    @property
    def minimum_base_food_mass_g(self):
        '''Minimum mass of an ideal smoothie's base food'''
        return self._minimum_base_food_mass_g
