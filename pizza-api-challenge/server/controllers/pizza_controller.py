from flask import Blueprint, jsonify , request
from server,models,pizza import Pizza
from server.config import db

bp = Blueprint('pizzas', __name__, url_prefix = '/pizzas')

@bp.route('', methods = ['GET'])
def get_all_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([pizza.to_dict() for pizza in pizzas])

@bp.route('/<init:id>', methods = ['GET'])
def get_pizza(id):
    pizza = Pizza.query.get(id)
    if pizza :
        return jsonify(pizza.to_dict())
    return jsonify ({"error": "Pizza not found"}), 404

@bp.route('', methods = ['POST'])
def create_pizza():
    data = request.get_json()
    new_pizza = Pizza(name = data['name'], ingredients = data ['ingredients'])
    db.session.add(new_pizza)
    db.session.commit()
    return jsonify(new_pizza.to_dict()), 201

@bp.route('/<init:id>', methods= ['DELETE'])
def delete_pizza(id):
    if pizza:
        db.session.delete(pizza)
        db.session.commit()

        return '', 204
    return jsonify({"error":"Pizza not found"}), 404

@bp.route()
def change_pizza(id):
#pizza_controller.py changes
