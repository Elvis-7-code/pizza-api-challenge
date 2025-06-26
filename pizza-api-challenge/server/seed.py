from server.app import create_app 
from server.config import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import restaurant_pizza

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    r1 = Restaurant(name= "Mario's Pizza", address = "123 Cheese St")
    r2 = Restaurant(name = "Luigi's slice", address = "456 Dough Ave")

    p1 = Pizza(name = "Margherita", ingredients="Tomato, Mozzarella, Basil")
    p2 = Pizza(name = "Pepperoni", ingredients = "Tomato, Mozzarella, Pepperoni")

    rp1 = restaurant_pizza(price=10, restaurant = r1, pizza = p1)
    rp2 = restaurant_pizza(price=12, restaurant = r1,pizza = p2)
    rp3 = restaurant_pizza(price = 8, restaurant = r2, pizza = p1)

    db.session.add_all([r1, r2, p1, rp1, rp2, rp3])
    db.session.commit()

    print("Seed data inserted successfully!")