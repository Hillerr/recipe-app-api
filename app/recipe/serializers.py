from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import Ingredient, Tag, Recipe


class TagSerializer(ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)


class IngredientSerializer(ModelSerializer):
    """Serializer for the ingredient objects"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)


class RecipeSerializer(ModelSerializer):
    """Serializer for recipe objects"""
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Recipe
        fields = (
            'id', 'title', 'ingredients', 'tags',
            'time_minutes', 'price', 'link'
        )
        read_only_fields = ('id',)
