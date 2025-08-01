from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'recipes', views.RecipeViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'favorites', views.FavoriteViewSet)

# Добавим новые ViewSet-ы (нужно их реализовать в views.py)
router.register(r'tags', views.TagViewSet)
router.register(r'recipe-tags', views.RecipeTagViewSet)
router.register(r'likes', views.LikeViewSet)
router.register(r'weight-runs', views.WeeklyPlanViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    # Дополнительные API эндпоинты
    path('api/recipes/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe-detail-api'),
    path('api/recipes/<int:recipe_id>/comments/', views.CommentCreateView.as_view(), name='add-comment-api'),
    path('api/favorites/', views.FavoriteView.as_view(), name='favorites-api'),

    # Веб-страницы
    path('', views.home, name='home'),
    path('weekly-plan/', views.weekly_plan, name='weekly-plan'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('add-recipe/', views.add_recipe, name='add-recipe'),
    path('accounts/register/', views.register, name='register'),
]
