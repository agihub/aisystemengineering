import sys
import os

class ApplicationSettings:

    def __init__(self):
        self.ROOT_AISYSTEM_ARCHITECTURE = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath("__file__")))))
        self.DATA_ROOT = os.path.join(self.ROOT_AISYSTEM_ARCHITECTURE, 'system', 'data')
        self.MODELS_ROOT = os.path.join(self.ROOT_AISYSTEM_ARCHITECTURE, 'system', 'models')


app_settings = ApplicationSettings()
