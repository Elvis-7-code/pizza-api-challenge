from server.config import db

class RestaurantPizza (db.models):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.Integer, nullable = False)

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)

    restaurant = db.relationship('Restaurant', back_populates = 'resetaurant_pizzas')
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')

    def validate(self):
        errors = []
        if not (1 <= self.price <= 30):
            errors.append("Price must be between 1 and 30")
        return errors
    
    def to_dict(self):
        return{
            "id": self.id,
            "price": self.price,
            "restaurant_id": self.restaurant_id,
            "pizza_id": self.pizza_id,
            "pizza": self.pizza.to_dict() if self.pizza else None,
            "restaurant": {
                "id": self.restaurant.id,
                "name": self.restaurant.name,
                "address": self.restaurant.address
            } if self.restaurant else None
        }