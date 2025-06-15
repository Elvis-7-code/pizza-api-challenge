from flask import Flask
from .config import db
from .models import restaurant, pizza, restaurant_pizza
from .controllers import restaurant_controller, pizza_controller, restaurant_pizza_controller