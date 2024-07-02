
from datetime import datetime
from aldo_safaris.extensions import db

class Rental(db.Model):
    __tablename__ = 'rentals'

    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, nullable=False)
    car_image_url = db.Column(db.String(255), nullable=True)
    price_per_day = db.Column(db.Float, nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    total_cost = db.Column(db.Float, nullable=False)

    # Define the relationships
    user = db.relationship('User', backref=db.backref('rentals', lazy=True))
    # car = db.relationship('Car', backref=db.backref('rentals', lazy=True))  # Uncomment when defining Car model

    def __repr__(self):
        return f'<Rental {self.id} - Car ID {self.car_id}>'

    @classmethod
    def get_available_rentals(cls):
        """Fetch available rentals."""
        return cls.query.filter(
            cls.car_image_url != None,  # Only rentals with car image URLs
            cls.price_per_day != None   # Only rentals with a defined price per day
        ).all()
