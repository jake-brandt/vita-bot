"""
vitabot 3000
"""

from itertools import zip_longest
from services import ConfigurationService, DataService, PopulationService, RecipeService, ScoringService

def main():
    """Main entrypoint"""

    # Instantiate services and DI
    configuration_service = ConfigurationService()
    data_service = DataService()
    recipe_service = RecipeService(configuration_service, data_service)
    scoring_service = ScoringService(configuration_service, recipe_service, data_service)
    population_service = PopulationService(data_service, recipe_service, scoring_service)

    recipes = population_service.create_population(200)
    population_service.breed_population(recipes)
    recipes = population_service.breed_population(recipes)
    print(recipes)

if __name__ == '__main__':
    main()
