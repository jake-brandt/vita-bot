"""
vitabot 3000
"""

from services import ConfigurationService, DataService, RecipeService

def main():
    """Main entrypoint"""
    configuration_service = ConfigurationService()
    data_service = DataService()
    recipe_service = RecipeService(configuration_service, data_service)

    recipe = recipe_service.create_recipe()
    nutrient_report = recipe_service.get_nutrient_report(recipe)

if __name__ == '__main__':
    main()
