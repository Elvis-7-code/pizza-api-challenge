from server.config import db

class Pizza(db.models):
    __tablename__ = 'pizzas'
    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.String, nullable = False)
    ingredients = db.column(db.string, nullable = False)

    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates = 'Pizza')