from django.apps import AppConfig

class RecipesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipes'

    def ready(self):
        # Регистрируем сигналы при готовности приложения
        import recipes.signals