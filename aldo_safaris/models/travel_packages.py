
# from aldo_safaris.extensions import db

# class TravelPackage(db.Model):
#     __tablename__ = 'travel_packages'

#     package_id = db.Column(db.Integer, primary_key=True)
#     package_name = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.Text)
#     destinations = db.Column(db.String(255))
#     activities = db.Column(db.String(255))
#     inclusions = db.Column(db.Text)
#     price = db.Column(db.Float)
#     duration = db.Column(db.Integer)
#     availability = db.Column(db.Boolean)
#     image_url = db.Column(db.String(200))

#     # bookings = db.relationship('Booking', backref='travel_package')  # Update the backref name

#     def __repr__(self):
#         return f'<TravelPackage {self.package_name}>'
from aldo_safaris.extensions import db

class TravelPackage(db.Model):
    __tablename__ = 'travel_packages'

    package_id = db.Column(db.Integer, primary_key=True)
    package_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    destinations = db.Column(db.String(255))
    activities = db.Column(db.String(255))
    inclusions = db.Column(db.Text)
    price = db.Column(db.Float)
    duration = db.Column(db.Integer)
    availability = db.Column(db.Boolean)
    image_url = db.Column(db.String(200))

    def __repr__(self):
        return f'<TravelPackage {self.package_name}>'
