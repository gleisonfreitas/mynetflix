from django.apps import AppConfig


class FilmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'film'

    def ready(self):
        from .models import User
        import os

        email = os.getenv('ADMIN_EMAIL')
        password = os.getenv('ADMIN_PASSWORD')

        users = User.objects.filter(email=email)
        if not users:
            User.objects.create_superuser(
                username='admin',
                email=email,
                password=password,
                is_active=True,
                is_staff=True )
