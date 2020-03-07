from django.apps import AppConfig


class ImagesConfig(AppConfig):
    name = 'images'

    def ready(self):
        # Импортируем файл с функцией-подписчиком на сигнал
        import images.signals

