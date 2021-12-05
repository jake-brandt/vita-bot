"""
vitabot 3000
"""

from itertools import zip_longest
from services import ConfigurationService, DataService, RecipeService, ScoringService

def main():
    """Main entrypoint"""
    configuration_service = ConfigurationService()
    data_service = DataService()
    recipe_service = RecipeService(configuration_service, data_service)
    scoring_service = ScoringService(configuration_service, recipe_service, data_service)

    #recipe = recipe_service.create_recipe()
    #scoring_service.score_recipe(recipe)
    # nutrient_report = recipe_service.get_nutrient_report(recipe)

    recipes = [recipe_service.create_recipe() for x in range(100)]
    scores = [scoring_service.score_recipe(recipe) for recipe in recipes]
    pairs = list(zip_longest(recipes, scores))
    pairs.sort(key=lambda x: x[1])
    print(pairs)

if __name__ == '__main__':
    main()
