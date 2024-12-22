from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '\x19\x9f\xb2\xfd\xe8\x0eb\xac\x15w\xaa\x1d\x07\xc7fsm\x90\x81NV\x81i\x99\xb1\x85\xf5\x7f\xc3{g\xfc\xe2\xb7h\x95?=\x8e\x977\x12'

    from .routes import main
    app.register_blueprint(main)

    return app