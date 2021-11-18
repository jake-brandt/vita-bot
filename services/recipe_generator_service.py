import random
from services import ConfigurationService, DataService


class RecipeGeneratorService():
    configuration_service: ConfigurationService = None
    data_service: DataService = None

    def __init__(
            self,
            configuration_service: ConfigurationService,
            data_service: DataService):
        self.configuration_service = configuration_service
        self.data_service = data_service

    def create_recipe(self):
        food_ids = self.data_service.unique_fdc_ids
        food_ids_length = len(food_ids)
        reqd_base_ingredient_ids = self.configuration_service.required_base_foods

        return list(map(
            lambda _: food_ids[random.choice(range(food_ids_length))],
            # One less because one slot is required for the base ingredient
            range(self.configuration_service.recipe_size - 1))
        ) + [
            # Reserved slot for required base ingredient
            reqd_base_ingredient_ids[random.choice(range(len(reqd_base_ingredient_ids)))]
        ]
