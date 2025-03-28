from flask import Flask, request, jsonify
from models.mealData import Meal
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretKey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:adminSenha@localhost:3307/daily-diet'

db.init_app(app)

@app.route("/register", methods=["POST"])
def create_meal():
    data = request.json
    food = data.get("food")
    description = data.get("description")
    timetable = data.get("timetable")
    fl_diet = data.get("fl_diet")

    if food and description and timetable and fl_diet:
        meal = Meal(food=food, description=description, timetable=timetable, fl_diet=fl_diet)
        db.session.add(meal)
        db.session.commit()
        return jsonify({"message": "Refição cadastrada com sucesso!"})

    return jsonify({"message": "Dados inválidos"}), 400

@app.route("/meal", methods=["GET"])
def all_meals():
    meals = Meal.query.all()
    meals_details = [
        {
            "id": meal.id,
            "food": meal.food,
            "description": meal.description,
            "timetable": meal.timetable,
            "fl_diet": meal.fl_diet
    } for meal in meals
    ]
    return jsonify({"Meals": meals_details})

@app.route("/meal/<int:id_meal>", methods=["GET"])
def get_meal(id_meal):
    meal = Meal.query.get(id_meal)

    if meal:
            meal_details = [{
                "id": meal.id,
                "food": meal.food,
                "description": meal.description,
                "timetable": meal.timetable,
                "fl_diet": meal.fl_diet
                }]
            return jsonify({"Meal": meal_details})
    
    return jsonify({"message": "Refeição não encontrada"}), 404

@app.route("/meal/<int:id_meal>", methods=["PUT"])
def update_meal(id_meal):
    data = request.json
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
