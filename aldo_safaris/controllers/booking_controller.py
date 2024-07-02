
from flask import Blueprint, request, jsonify
from datetime import datetime
from aldo_safaris.extensions import db
from aldo_safaris.models.booking import Booking
from flask_jwt_extended import jwt_required, get_jwt_identity
import json

# booking_bp = Blueprint('Booking', __name__, url_prefix='/api/v1/booking')

# @booking_bp.route('/register', methods=['POST'])
# @jwt_required()
# def create_booking():
#     try:
#         # Extract booking data from request JSON
#         data = request.json

#         package_id = data.get('package_id')
#         user_id = get_jwt_identity()
#         travel_start_date = data.get('travel_start_date')
#         travel_end_date = data.get('travel_end_date')
#         total_cost = data.get('total_cost')
#         payment_status = data.get('payment_status')
#         booking_status = data.get('booking_status')
#         destination = data.get('destination')
#         accommodation = data.get('accommodation')
#         transportation = data.get('transportation')
#         activities = data.get('activities', [])
#         booking_source = data.get('booking_source')

#         # Basic input validation
#         if not all([package_id, travel_start_date, travel_end_date, total_cost, destination]):
#             return jsonify({"error": "All fields are required"}), 400

#         # Convert activities list to JSON string
#         activities_json = json.dumps(activities)

#         # Create a new booking
#         new_booking = Booking(
#             package_id=package_id,
#             user_id=user_id,
#             date_of_booking=datetime.now(),
#             travel_start_date=datetime.strptime(travel_start_date, '%Y-%m-%d'),
#             travel_end_date=datetime.strptime(travel_end_date, '%Y-%m-%d'),
#             total_cost=total_cost,
#             payment_status=payment_status,
#             booking_status=booking_status,
#             destination=destination,
#             accommodation=accommodation,
#             transportation=transportation,
#             activities=activities_json,  # Store as JSON string
#             booking_source=booking_source
#         )

#         # Add booking to the database and commit
#         db.session.add(new_booking)
#         db.session.commit()

#         return jsonify({'message': 'Booking created successfully', 'booking_id': new_booking.booking_id}), 201

#     except ValueError as ve:
#         return jsonify({'error': 'Invalid input: ' + str(ve)}), 400
#     except KeyError as ke:
#         return jsonify({'error': 'Missing key: ' + str(ke)}), 400
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'error': 'Internal Server Error: ' + str(e)}), 500

# @booking_bp.route('/<int:booking_id>', methods=['GET'])
# @jwt_required()
# def get_booking(booking_id):
#     try:
#         # Get booking by ID
#         booking = Booking.query.get(booking_id)

#         if not booking:
#             return jsonify({'error': 'Booking not found'}), 404

#         # Ensure the current user is the owner of the booking
#         current_user_id = int(get_jwt_identity())
#         if booking.user_id != current_user_id:
#             return jsonify({'error': 'You are not authorized to view this booking'}), 403

#         # Convert booking object to dictionary for response
#         booking_data = {
#             'booking_id': booking.booking_id,
#             'package_id': booking.package_id,
#             'user_id': booking.user_id,
#             'date_of_booking': booking.date_of_booking,
#             'travel_start_date': booking.travel_start_date,
#             'travel_end_date': booking.travel_end_date,
#             'total_cost': booking.total_cost,
#             'payment_status': booking.payment_status,
#             'booking_status': booking.booking_status,
#             'destination': booking.destination,
#             'accommodation': booking.accommodation,
#             'transportation': booking.transportation,
#             'activities': json.loads(booking.activities),  # Convert JSON string back to list
#             'booking_source': booking.booking_source
#         }

#         return jsonify(booking_data), 200

#     except Exception as e:
#         return jsonify({'error': 'Internal Server Error: ' + str(e)}), 500

# @booking_bp.route('/<int:booking_id>', methods=['PUT'])
# @jwt_required()
# def update_booking(booking_id):
#     try:
#         # Get booking by ID
#         booking = Booking.query.get(booking_id)

#         if not booking:
#             return jsonify({'error': 'Booking not found'}), 404

#         # Ensure the current user is the owner of the booking
#         current_user_id = int(get_jwt_identity())
#         if booking.user_id != current_user_id:
#             return jsonify({'error': 'You are not authorized to update this booking'}), 403

#         # Extract booking data from request JSON
#         data = request.json

#         # Update booking fields if provided in request
#         if 'package_id' in data:
#             booking.package_id = data['package_id']
#         if 'travel_start_date' in data:
#             booking.travel_start_date = datetime.strptime(data['travel_start_date'], '%Y-%m-%d')
#         if 'travel_end_date' in data:
#             booking.travel_end_date = datetime.strptime(data['travel_end_date'], '%Y-%m-%d')
#         if 'total_cost' in data:
#             booking.total_cost = data['total_cost']
#         if 'payment_status' in data:
#             booking.payment_status = data['payment_status']
#         if 'booking_status' in data:
#             booking.booking_status = data['booking_status']
#         if 'destination' in data:
#             booking.destination = data['destination']
#         if 'accommodation' in data:
#             booking.accommodation = data['accommodation']
#         if 'transportation' in data:
#             booking.transportation = data['transportation']
#         if 'activities' in data:
#             booking.activities = json.dumps(data['activities'])  # Convert list to JSON string
#         if 'booking_source' in data:
#             booking.booking_source = data['booking_source']

#         # Commit changes to the database
#         db.session.commit()

#         return jsonify({'message': 'Booking updated successfully'}), 200

#     except ValueError as ve:
#         return jsonify({'error': 'Invalid input: ' + str(ve)}), 400
#     except KeyError as ke:
#         return jsonify({'error': 'Missing key: ' + str(ke)}), 400
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'error': 'Internal Server Error: ' + str(e)}), 500

# @booking_bp.route('/<int:booking_id>', methods=['DELETE'])
# @jwt_required()
# def delete_booking(booking_id):
#     try:
#         # Get booking by ID
#         booking = Booking.query.get(booking_id)

#         if not booking:
#             return jsonify({'error': 'Booking not found'}), 404

#         # Ensure the current user is the owner of the booking
#         current_user_id = int(get_jwt_identity())
#         if booking.user_id != current_user_id:
#             return jsonify({'error': 'You are not authorized to delete this booking'}), 403

#         # Delete booking from the database
#         db.session.delete(booking)
#         db.session.commit()

#         return jsonify({'message': 'Booking deleted successfully'}), 200

#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'error': 'Internal Server Error: ' + str(e)}), 500

# @booking_bp.route('/user_bookings', methods=['GET'])
# @jwt_required()
# def get_user_bookings():
#     try:
#         # Get the current user ID from JWT token
#         current_user_id = int(get_jwt_identity())

#         # Retrieve all bookings for the current user
#         bookings = Booking.query.filter_by(user_id=current_user_id).all()

#         # Convert bookings to list of dictionaries for response
#         bookings_data = [
#             {
#                 'booking_id': booking.booking_id,
#                 'package_id': booking.package_id,
#                 'user_id': booking.user_id,
#                 'date_of_booking': booking.date_of_booking,
#                 'travel_start_date': booking.travel_start_date,
#                 'travel_end_date': booking.travel_end_date,
#                 'total_cost': booking.total_cost,
#                 'payment_status': booking.payment_status,
#                 'booking_status': booking.booking_status,
#                 'destination': booking.destination,
#                 'accommodation': booking.accommodation,
#                 'transportation': booking.transportation,
#                 'activities': json.loads(booking.activities),  # Convert JSON string back to list
#                 'booking_source': booking.booking_source
#             } for booking in bookings
#         ]

#         return jsonify(bookings_data), 200

#     except Exception as e:
#         return jsonify({'error': 'Internal Server Error: ' + str(e)}), 500
from flask import Blueprint, request, jsonify
from datetime import datetime
from aldo_safaris.extensions import db
from aldo_safaris.models.booking import Booking
from aldo_safaris.models.travel_packages import TravelPackage
#from aldo_safaris.models.users import User
from flask_jwt_extended import jwt_required, get_jwt_identity
import json

booking_bp = Blueprint('Booking', __name__, url_prefix='/api/v1/booking')

@booking_bp.route('/register', methods=['POST'])
@jwt_required()
def create_booking():
    try:
        data = request.json
        
        package_id = data.get('package_id')
        user_id = get_jwt_identity()  # This assumes JWT provides user_id
        travel_start_date = data.get('travel_start_date')
        travel_end_date = data.get('travel_end_date')
        total_cost = data.get('total_cost')
        payment_status = data.get('payment_status')
        booking_status = data.get('booking_status')
        destination = data.get('destination')
        accommodation = data.get('accommodation')
        transportation = data.get('transportation')
        activities = data.get('activities', [])
        booking_source = data.get('booking_source')

        # Validate essential fields
        if not all([package_id, travel_start_date, travel_end_date, total_cost, destination]):
            return jsonify({"error": "All required fields must be provided"}), 400
        
        # Validate that the package_id exists
        package = TravelPackage.query.get(package_id)
        if not package:
            return jsonify({'error': 'Invalid package_id'}), 400

        # Convert date strings to datetime objects
        travel_start_date = datetime.strptime(travel_start_date, '%Y-%m-%d')
        travel_end_date = datetime.strptime(travel_end_date, '%Y-%m-%d')

        # Create new booking
        new_booking = Booking(
            package_id=package_id,
            user_id=user_id,
            travel_start_date=travel_start_date,
            travel_end_date=travel_end_date,
            total_cost=total_cost,
            payment_status=payment_status,
            booking_status=booking_status,
            destination=destination,
            accommodation=accommodation,
            transportation=transportation,
            activities=json.dumps(activities),  # Store activities as JSON string
            booking_source=booking_source,
            date_of_booking=datetime.now()
        )

        db.session.add(new_booking)
        db.session.commit()

        return jsonify({'message': 'Booking created successfully', 'booking_id': new_booking.booking_id}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error: ' + str(e)}), 500


@booking_bp.route('/<int:booking_id>', methods=['GET'])
@jwt_required()
def get_booking(booking_id):
    try:
        booking = Booking.query.get(booking_id)
        
        if not booking:
            return jsonify({'error': 'Booking not found'}), 404
        
        current_user_id = get_jwt_identity()
        if booking.user_id != current_user_id:
            return jsonify({'error': 'You are not authorized to view this booking'}), 403

        booking_data = {
            'booking_id': booking.booking_id,
            'package_id': booking.package_id,
            'user_id': booking.user_id,
            'date_of_booking': booking.date_of_booking,
            'travel_start_date': booking.travel_start_date,
            'travel_end_date': booking.travel_end_date,
            'total_cost': booking.total_cost,
            'payment_status': booking.payment_status,
            'booking_status': booking.booking_status,
            'destination': booking.destination,
            'accommodation': booking.accommodation,
            'transportation': booking.transportation,
            'activities': json.loads(booking.activities),  # Convert JSON string back to list
            'booking_source': booking.booking_source
        }

        return jsonify(booking_data), 200

    except Exception as e:
        return jsonify({'error': 'Internal Server Error: ' + str(e)}), 500


@booking_bp.route('/<int:booking_id>', methods=['PUT'])
@jwt_required()
def update_booking(booking_id):
    try:
        booking = Booking.query.get(booking_id)

        if not booking:
            return jsonify({'error': 'Booking not found'}), 404

        current_user_id = get_jwt_identity()
        if booking.user_id != current_user_id:
            return jsonify({'error': 'You are not authorized to update this booking'}), 403

        data = request.json

        if 'package_id' in data:
            package_id = data['package_id']
            package = TravelPackage.query.get(package_id)
            if not package:
                return jsonify({'error': 'Invalid package_id'}), 400
            booking.package_id = package_id

        if 'travel_start_date' in data:
            booking.travel_start_date = datetime.strptime(data['travel_start_date'], '%Y-%m-%d')
        if 'travel_end_date' in data:
            booking.travel_end_date = datetime.strptime(data['travel_end_date'], '%Y-%m-%d')
        if 'total_cost' in data:
            booking.total_cost = data['total_cost']
        if 'payment_status' in data:
            booking.payment_status = data['payment_status']
        if 'booking_status' in data:
            booking.booking_status = data['booking_status']
        if 'destination' in data:
            booking.destination = data['destination']
        if 'accommodation' in data:
            booking.accommodation = data['accommodation']
        if 'transportation' in data:
            booking.transportation = data['transportation']
        if 'activities' in data:
            booking.activities = json.dumps(data['activities'])  # Store activities as JSON string
        if 'booking_source' in data:
            booking.booking_source = data['booking_source']

        db.session.commit()

        return jsonify({'message': 'Booking updated successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error: ' + str(e)}), 500


@booking_bp.route('/<int:booking_id>', methods=['DELETE'])
@jwt_required()
def delete_booking(booking_id):
    try:
        booking = Booking.query.get(booking_id)

        if not booking:
            return jsonify({'error': 'Booking not found'}), 404

        current_user_id = get_jwt_identity()
        if booking.user_id != current_user_id:
            return jsonify({'error': 'You are not authorized to delete this booking'}), 403

        db.session.delete(booking)
        db.session.commit()

        return jsonify({'message': 'Booking deleted successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error: ' + str(e)}), 500


@booking_bp.route('/user_bookings', methods=['GET'])
@jwt_required()
def get_user_bookings():
    try:
        current_user_id = get_jwt_identity()

        bookings = Booking.query.filter_by(user_id=current_user_id).all()

        bookings_data = [
            {
                'booking_id': booking.booking_id,
                'package_id': booking.package_id,
                'user_id': booking.user_id,
                'date_of_booking': booking.date_of_booking,
                'travel_start_date': booking.travel_start_date,
                'travel_end_date': booking.travel_end_date,
                'total_cost': booking.total_cost,
                'payment_status': booking.payment_status,
                'booking_status': booking.booking_status,
                'destination': booking.destination,
                'accommodation': booking.accommodation,
                'transportation': booking.transportation,
                'activities': json.loads(booking.activities),  # Convert JSON string back to list
                'booking_source': booking.booking_source
            } for booking in bookings
        ]

        return jsonify(bookings_data), 200

    except Exception as e:
        return jsonify({'error': 'Internal Server Error: ' + str(e)}), 500
