from math import atan
from models.recipe import Recipe
from . import ConfigurationService, DataService, RecipeService

_mass_multipliers = {
    'kg': 1000,
    'g': 1.0,
    'mg': 0.001,
    'ug': 0.000001
}


class ScoringService():
    _configuration_service: ConfigurationService = None
    _recipe_service: RecipeService = None
    _data_service: DataService = None

    def __init__(
        self,
        configuration_service: ConfigurationService,
        recipe_service: RecipeService,
        data_service: DataService
    ):
        self._configuration_service = configuration_service
        self._recipe_service = recipe_service
        self._data_service = data_service

    def score_recipe(self, ingredients: Recipe) -> float:
        '''Compute a score for the given recipe. Golf rules - lower is better!'''

        score = 0

        total_mass_g = sum([i.mass_g for i in ingredients])
        pct_ideal_mass = 100 * (total_mass_g / self._configuration_service.smoothie_mass_g)

        # Reward recipes which are extremely close to ideal mass.
        score += atan(abs(pct_ideal_mass - 100))

        return score
