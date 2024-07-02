
# from datetime import datetime
# from aldo_safaris.extensions import db

# class Payment(db.Model):
#     __tablename__ = 'payments'

#     payment_id = db.Column(db.Integer, primary_key=True)
#     booking_id = db.Column(db.Integer, db.ForeignKey('bookings.booking_id'), nullable=True)
#     payment_date = db.Column(db.DateTime, default=datetime.utcnow)
#     amount = db.Column(db.Float)
#     payment_method = db.Column(db.String(50))
#     status = db.Column(db.String(20))
#     car_id = db.Column(db.Integer, db.ForeignKey('rentals.id'), nullable=True)

#     # Define the relationship to Booking with a unique backref name
#     booking = db.relationship('Booking', backref='payment_details')

#     # Define the relationship to Rental with a unique backref name
#     rental = db.relationship('Rental', backref='payment_records')  # Changed 'rental' to 'payment_records'

#     def __repr__(self):
#         return f'<Payment {self.payment_id}>'
from datetime import datetime
from aldo_safaris.extensions import db

class Payment(db.Model):
    __tablename__ = 'payments'

    payment_id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('bookings.booking_id'), nullable=True)
    payment_date = db.Column(db.DateTime, default=datetime.utcnow)
    amount = db.Column(db.Float)
    payment_method = db.Column(db.String(50))
    status = db.Column(db.String(20))
    car_id = db.Column(db.Integer, db.ForeignKey('rentals.id'), nullable=True)

    # Define the relationship to Booking with a clear backref name
    booking = db.relationship('Booking', backref='payments')

    # Define the relationship to Rental with a unique backref name
    rental = db.relationship('Rental', backref='payments')  # Simplified and consistent backref name

    def __repr__(self):
        return f'<Payment {self.payment_id}>'

