import json

from flask import Flask

from configs import config, get_config_variable




def factory(env:str ='default') -> Flask:

    app = Flask(__name__)
    app.config.from_object(configs[env])

    return app
