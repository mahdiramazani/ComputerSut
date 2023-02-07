from django.apps import AppConfig


class TeacherAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.Teacher_app'

    def ready(self):

        import apps.Teacher_app.signals
