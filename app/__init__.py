def create_app(config_name):
    from .api_0_1 import api as api_0_1_blueprint
    app.register_blueprint(api_0_1_blueprint, url_prefix='/api/v0.1')
