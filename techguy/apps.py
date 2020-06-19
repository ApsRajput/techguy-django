from django.apps import AppConfig


class BaseConfig(AppConfig):
    name = 'techguy'

    def ready(self):
    	import techguy.signals