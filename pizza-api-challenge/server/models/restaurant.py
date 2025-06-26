from server.config import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.string, nullable = False)
    address = db.Column(db.string, nullable = False)
    
    restaurant_pizzas = db.relationship(
        'RestaurantPizza', 
        back_populates = 'restaurant'
        cascade = 'all, delete-orphan'
        )
