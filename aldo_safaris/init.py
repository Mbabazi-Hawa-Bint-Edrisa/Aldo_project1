from flask import Flask
from aldo_safaris.extensions import db, migrate, jwt, bcrypt
from aldo_safaris.controllers.booking_controller import booking_bp 
from aldo_safaris.controllers.payments_controller import payment_bp
from aldo_safaris.controllers.car_hiring_controller import car_rental_bp 
from aldo_safaris.controllers.notifications_controller import notification_bp
from aldo_safaris.controllers.t_package_controller import travel_package_bp
from aldo_safaris.controllers.user_accounts_controller import customer


def create_app():
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)

    # Register blueprints
    app.register_blueprint(booking_bp, url_prefix='/api/v1/booking')
    app.register_blueprint(car_rental_bp, url_prefix='/api/v1/car_rental')
    app.register_blueprint(notification_bp, url_prefix='/api/v1/notification')
    app.register_blueprint(payment_bp, url_prefix='/api/v1/payment')
    app.register_blueprint(travel_package_bp, url_prefix='/api/v1/travel_package')
    app.register_blueprint(customer, url_prefix='/api/v1/customer')
 

    return app
