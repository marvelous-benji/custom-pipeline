import json


with open('config.json', 'r') as environ:
    environ = json.load(environ)


def get_config_variable(key: str) -> str:

    return environ[key] if environ.get(key)\
    else raise KeyError('Key not found')




class BaseConfig:
    '''
    Sets the base apps configurations to be inherited
    by other configuration enviroments
    '''
    SECRET_KEY = get_config_variable('SECRET_KEY')

class DevelopmentConfig(BaseConfig):

    DEBUG = True

class ProductionConfig(BaseConfig):

    DEBUG = False

class TestConfig(BaseConfig):

    TESTING = True


setting = {
    'development':DevelopmentConfig,
    'production':ProductionConfig,
    'testing':TestConfig,
    'default':DevelopmentConfig
}
