from flask import Flask, g
from application.views import views
from flask_session import Session

app = Flask(__name__)
app.register_blueprint(views)

SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)

app.config["STATIC_FOLDER"] = "static"
Session(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088)