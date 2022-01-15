from flask import Flask
from models.wishlist import db
from mainpage import mainpage_blueprints
from sqlalchemy_utils import database_exists


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Пользователь:Пароль@localhost/БД'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    if database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
        print('База данных уже создана')
    else:
        db.create_all(app=app)
        print('База данных создана')
    mainpage_blueprints(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)