from flask import Flask, request, jsonify
from models.mealData import Meal
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretKey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:adminSenha@localhost:3307/daily-diet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route("/register", methods=["POST"])
def create_meal():
    data = request.get_json()

    if not data:  
        return jsonify({"message": "Dados inválidos"}), 400

    required_fields = ["food", "description", "timetable", "fl_diet"]
    if not all(field in data for field in required_fields):  
        return jsonify({"message": "Campos obrigatórios ausentes"}), 400

    meal = Meal(**data)
    db.session.add(meal)
    db.session.commit()
    return jsonify({"message": "Refeição cadastrada com sucesso"}), 201


@app.route("/meal", methods=["GET"])
def all_meals():
    meals = Meal.query.all()
    
    meals_details = [meal.to_dict() for meal in meals] 
    
    return jsonify({"Meals": meals_details})

@app.route("/meal/<int:id_meal>", methods=["GET"])
def get_meal(id_meal):
    meal = Meal.query.get(id_meal)

    if meal:
        return jsonify({"Meal": meal.to_dict()})
    
    return jsonify({"message": "Refeição não encontrada"}), 404

@app.route("/meal/<int:id_meal>", methods=["PUT"])
def update_meal(id_meal):
    data = request.get_json()
    meal = Meal.query.get(id_meal)

    if meal:
        meal.food = data.get("food")
        meal.description = data.get("description")
        meal.timetable = data.get("timetable")
        meal.fl_diet  = data.get("fl_diet")

        db.session.commit()
        return jsonify({"message": "Refeição atualizada com sucesso"})
    
    return jsonify({"message": "Refeição não encontrada"}), 404

@app.route("/meal/<int:id_meal>", methods=["DELETE"])
def delete_meal(id_meal):
    meal = Meal.query.get(id_meal)

    if meal:
        db.session.delete(meal)
        db.session.commit()
        return jsonify({"message": "Refeição deletada com sucesso"})
    
    return jsonify({"message": "Refeição não encontrada"}), 404



@app.route("/helloworld", methods=["GET"])
def helloWorld():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)
