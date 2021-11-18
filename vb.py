"""
vitabot 3000
"""

from services import ConfigurationService, DataService, RecipeGeneratorService

def main():
    """Main entrypoint"""
    configuration_service = ConfigurationService()
    data_service = DataService()
    recipe_service = RecipeGeneratorService(configuration_service, data_service)

    print(recipe_service.create_recipe())

if __name__ == '__main__':
    main()
