import os
import json

class Configuration:
    settings: dict = None

    @staticmethod
    def load_configuration():
        env = os.getenv("PYTHON_ENVIRONMENT", None)
        if env is None:
            env = 'Dev'

        env_file = os.path.join('src', 'configs', f'configuration.{env}.json')
        with open(env_file, 'r') as f:
            Configuration.settings = json.load(f)


if Configuration.settings is None:
    Configuration.load_configuration()