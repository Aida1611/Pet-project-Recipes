from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Profile, Tag, Recipe, RecipeImage,
    Ingredient, RecipeIngredient, RecipeTag,
    Favorite, Comment, Like, WeeklyPlan
)

# Пользователь
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # хешируем пароль
        user.save()
        return user


# Профиль с вложенным пользователем
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'

# Тег
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

# Промежуточная модель RecipeTag с вложенными recipe и tag
class RecipeTagSerializer(serializers.ModelSerializer):
    recipe = serializers.PrimaryKeyRelatedField(read_only=True)
    tag = TagSerializer(read_only=True)

    class Meta:
        model = RecipeTag
        fields = '__all__'

# Ингредиент
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

# Ингредиенты рецепта с вложенным ингредиентом
class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = RecipeIngredient
        fields = '__all__'

# Картинки рецепта
class RecipeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeImage
        fields = ['id', 'image_file']

# Рецепт со вложенными данными
class RecipeSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    ingredients = RecipeIngredientSerializer(many=True, read_only=True)
    images = RecipeImageSerializer(many=True, read_only=True)
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = '__all__'

    def get_tags(self, obj):
        recipe_tags = RecipeTag.objects.filter(recipe=obj)
        return RecipeTagSerializer(recipe_tags, many=True).data

# Комментарий с вложенным пользователем
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = '__all__'

# Избранное с вложенным пользователем
class FavoriteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    recipe = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all())

    class Meta:
        model = Favorite
        fields = '__all__'


# Лайк с вложенным пользователем
class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Like
        fields = '__all__'

# Запись WeightRun с вложенными user и recipe
class WeeklyPlanSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    recipe = RecipeSerializer()

    class Meta:
        model = WeeklyPlan
        fields = '__all__'
