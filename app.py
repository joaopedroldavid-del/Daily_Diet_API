from flask import Flask, request, jsonify
from models.mealData import Meal
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretKey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:adminSenha@localhost:3306/daily-diet'

db.init_app(app)

@app.route("/create", methods=["POST"])
def create_meal():
    return

@app.route("/meal", methods=["GET"])
def all_meals():
    return

@app.route("/meal/<int:id_meal>", methods=["GET"])
def get_meal():
    return

@app.route("/meal/<int:id_meal>", methods=["PUT"])
def update_meal():
    return

@app.route("/meal/<int:id_meal>", methods=["DELETE"])
def delete_meal():
    return


@app.route("/helloworld", methods=["GET"])
def helloWorld():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)
