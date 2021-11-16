from services import ConfigurationService
from services.data import FoodDataService

class RecipeGeneratorService():
    food_data_service: FoodDataService = None

    def __init__(self, configuration_service: ConfigurationService, food_data_service: FoodDataService):
        self.food_data_service = food_data_service

    def create_recipe(self):
        pass
