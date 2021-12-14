import random
import pandas as pd
from models.recipe import Recipe
from . import DataService, RecipeService, ScoringService
from itertools import zip_longest


class PopulationService():
    data_service: DataService = None
    recipe_service: RecipeService = None
    scoring_service: ScoringService = None

    def __init__(
            self,
            data_service: DataService,
            recipe_service: RecipeService,
            scoring_service: ScoringService):
        self.data_service = data_service
        self.recipe_service = recipe_service
        self.scoring_service = scoring_service

    def create_population(self, size: int) -> list[Recipe]:
        return [self.recipe_service.create_recipe() for x in range(size)]

    def breed_population(self, population: list[Recipe]) -> list[Recipe]:
        recipes_and_scores = [
            {'recipe': recipe,
                'score': self.scoring_service.score_recipe(recipe)}
            for recipe in population
        ]

        # Sort scores ascending, remove last 20, clone first 20.
        # Effectively, "last 20 can't participate, first 20 have extra opportunities"
        recipes_and_scores.sort(
            key=lambda recipe_and_score: recipe_and_score['score'])
        recipes_and_scores = recipes_and_scores[:-20]
        recipes_and_scores.extend(recipes_and_scores[:20])

        # Keep the champion
        next_population = []
        next_population.append(recipes_and_scores[0])

        # Determine pairs
        pairs_for_population = [
            {
                'recipe_a': recipes_and_scores[random.randint(0, 199)]['recipe'],
                'recipe_b': recipes_and_scores[random.randint(0, 199)]['recipe']
            }
            for _ in range(199)
        ]

        next_population.extend([self.create_offspring(
            p['recipe_a'], p['recipe_b']) for p in pairs_for_population])

        return next_population

    def create_offspring(self, recipe_a: Recipe, recipe_b: Recipe) -> Recipe:
        splice_index = random.randint(1, 4)
        offspring = [
            *recipe_a[:splice_index],
            *recipe_b[splice_index:]
        ]

        has_mutation = random.randint(1, 100) < 5
        if has_mutation:
            mutation_index = random.randint(0, 4)
            is_for_weight = random.randint(1, 2) == 1

            item_to_mutate = offspring[mutation_index]

            if is_for_weight:
                # Modify the weight slightly
                item_to_mutate.percent_100_grams = item_to_mutate.percent_100_grams + \
                    (random.randint(1, 11) - 6)
            else:
                # Modify the FDC ID
                eligible_food_ids = self.data_service.unique_fdc_ids
                item_to_mutate.fdc_id = eligible_food_ids[random.choice(range(len(eligible_food_ids)))]

        return offspring
