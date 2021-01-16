# from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)


# @app.route("/")
# def index():
#     return {
#         "message": "App is awake"
#     }


# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:////tmp/text.db'
# db = SQLAlchemy(app)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)

#     def __repr__(self) -> str:
#         return '<User %r>' % self.username


# if __name__ == '__main__':
#     app.run(threaded=True, port=5000)
