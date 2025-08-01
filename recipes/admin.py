from django.contrib import admin
from .models import *

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1

class RecipeTagInline(admin.TabularInline):
    model = RecipeTag
    extra = 1

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'difficulty')
    search_fields = ('title', 'description')
    list_filter = ('difficulty', 'created_at')
    inlines = [RecipeIngredientInline, RecipeImageInline, RecipeTagInline]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name')
    search_fields = ('user__username', 'full_name')

admin.site.register(Tag)
admin.site.register(Ingredient)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Favorite)
admin.site.register(WeeklyPlan)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.unregister(User)  # Отменяем стандартную регистрацию

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')