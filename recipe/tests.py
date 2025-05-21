from django.test import TestCase
from .models import Category, Recipe

class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(name="Dessert")
        self.assertEqual(str(category), "Dessert")

    def test_iter_method(self):
        category = Category.objects.create(name="Soups")
        self.assertEqual(list(iter(category)), ["Soups"])


class RecipeModelTest(TestCase):
    def test_create_recipe(self):
        category = Category.objects.create(name="Drinks")
        recipe = Recipe.objects.create(
            title="Lemonade",
            description="Refreshing drink",
            instructions="Mix water, lemon and sugar",
            ingredients="Water, Lemon, Sugar",
            category=category
        )
        self.assertEqual(str(recipe), "Lemonade")
        self.assertEqual(recipe.category.name, "Drinks")