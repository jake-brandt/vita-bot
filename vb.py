"""
vitabot 3000
"""

from services import ConfigurationService, RecipeGeneratorService
from services.data import FoodDataService

def main():
    """Main entrypoint"""
    configuration_service = ConfigurationService()
    food_service = FoodDataService()
    recipe_service = RecipeGeneratorService(configuration_service, food_service)

    print(recipe_service.create_recipe())

if __name__ == '__main__':
    main()
