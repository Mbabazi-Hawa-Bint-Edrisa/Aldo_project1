
# from flask import Blueprint, request, jsonify
# from flask_jwt_extended import jwt_required, get_jwt_identity
# from datetime import datetime
# from aldo_safaris.extensions import db
# from aldo_safaris.models.car_hiring import Rental

# # Define the blueprint
# car_rental_bp = Blueprint('car_rental', __name__, url_prefix='/api/v1/car_rental')

# # Allowed extensions for image files
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # Rental Routes
# @car_rental_bp.route('/register', methods=['POST'])
# @jwt_required()
# def create_rental():
#     try:
#         # Extract rental data from JSON request
#         data = request.get_json()
#         car_id = data.get('car_id')
#         start_date_str = data.get('start_date')
#         end_date_str = data.get('end_date')

#         # Basic input validation
#         if not all([car_id, start_date_str, end_date_str]):
#             return jsonify({"error": "Car ID, start date, and end date are required"}), 400

#         # Convert dates to datetime objects
#         start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
#         end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

#         if start_date >= end_date:
#             return jsonify({"error": "End date must be after start date"}), 400

#         # Calculate total cost (assuming you have a way to get price_per_day)
#         price_per_day = 100  # Replace with your logic to fetch the price_per_day

#         # Calculate the total cost
#         days_rented = (end_date - start_date).days
#         total_cost = days_rented * price_per_day

#         # Create a new rental
#         new_rental = Rental(
#             car_id=car_id,
#             start_date=start_date,
#             end_date=end_date,
#             total_cost=total_cost,
#             user_id=get_jwt_identity()  # Assuming you have a way to get the user_id
#         )

#         # Add rental to the database and commit
#         db.session.add(new_rental)
#         db.session.commit()

#         return jsonify({'message': 'Rental created successfully', 'rental_id': new_rental.id}), 201

#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'error': str(e)}), 500


# @car_rental_bp.route('/rental/<int:rental_id>', methods=['GET'])
# @jwt_required()
# def get_rental(rental_id):
#     try:
#         # Get rental by ID
#         rental = Rental.query.get(rental_id)

#         if not rental:
#             return jsonify({'error': 'Rental not found'}), 404

#         # Ensure the current user is the owner of the rental
#         current_user_id = get_jwt_identity()
#         if rental.user_id != current_user_id:
#             return jsonify({'error': 'You are not authorized to view this rental'}), 403

#         # Convert rental object to dictionary for response
#         rental_data = {
#             'rental_id': rental.id,
#             'car_id': rental.car_id,
#             'start_date': rental.start_date.strftime('%Y-%m-%d'),
#             'end_date': rental.end_date.strftime('%Y-%m-%d'),
#             'total_cost': rental.total_cost,
#             'user_id': rental.user_id
#         }

#         return jsonify(rental_data), 200

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500


# @car_rental_bp.route('/rental/<int:rental_id>', methods=['PUT'])
# @jwt_required()
# def update_rental(rental_id):
#     try:
#         # Get rental by ID
#         rental = Rental.query.get(rental_id)

#         if not rental:
#             return jsonify({'error': 'Rental not found'}), 404

#         # Ensure the current user is the owner of the rental
#         current_user_id = get_jwt_identity()
#         if rental.user_id != current_user_id:
#             return jsonify({'error': 'You are not authorized to update this rental'}), 403

#         # Extract rental data from JSON request
#         data = request.get_json()
#         car_id = data.get('car_id')
#         start_date_str = data.get('start_date')
#         end_date_str = data.get('end_date')

#         # Basic input validation
#         if not all([car_id, start_date_str, end_date_str]):
#             return jsonify({"error": "Car ID, start date, and end date are required"}), 400

#         # Convert dates to datetime objects
#         start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
#         end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

#         if start_date >= end_date:
#             return jsonify({"error": "End date must be after start date"}), 400

#         # Calculate total cost (assuming you have a way to get price_per_day)
#         price_per_day = 100  # Replace with your logic to fetch the price_per_day

#         # Calculate the total cost
#         days_rented = (end_date - start_date).days
#         total_cost = days_rented * price_per_day

#         # Update rental fields
#         rental.car_id = car_id
#         rental.start_date = start_date
#         rental.end_date = end_date
#         rental.total_cost = total_cost

#         # Commit changes to the database
#         db.session.commit()

#         return jsonify({'message': 'Rental updated successfully'}), 200

#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'error': str(e)}), 500


# @car_rental_bp.route('/rental/<int:rental_id>', methods=['DELETE'])
# @jwt_required()
# def delete_rental(rental_id):
#     try:
#         # Get rental by ID
#         rental = Rental.query.get(rental_id)

#         if not rental:
#             return jsonify({'error': 'Rental not found'}), 404

#         # Ensure the current user is the owner of the rental
#         current_user_id = get_jwt_identity()
#         if rental.user_id != current_user_id:
#             return jsonify({'error': 'You are not authorized to delete this rental'}), 403

#         # Delete rental from the database
#         db.session.delete(rental)
#         db.session.commit()

#         return jsonify({'message': 'Rental deleted successfully'}), 200

#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'error': str(e)}), 500
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
from aldo_safaris.extensions import db
from aldo_safaris.models.car_hiring import Rental

# Define the blueprint
car_rental_bp = Blueprint('car_rental', __name__, url_prefix='/api/v1/car_rental')

# Allowed extensions for image files
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to validate dates
def validate_dates(start_date, end_date):
    try:
        start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
        return start_date_obj, end_date_obj
    except ValueError:
        return None, None

# Rental Routes

@car_rental_bp.route('/rentals', methods=['POST'])
@jwt_required()
def create_rental():
    try:
        data = request.get_json()

        car_id = data.get('car_id')
        car_image_url = data.get('car_image_url')
        price_per_day = data.get('price_per_day')
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        user_id = get_jwt_identity()

        # Basic input validation
        if not all([car_id, price_per_day, start_date, end_date]):
            return jsonify({"error": "Car ID, price per day, start date, and end date are required"}), 400

        # Validate and convert dates
        start_date, end_date = validate_dates(start_date, end_date)
        if not start_date or not end_date:
            return jsonify({"error": "Invalid date format. Please use YYYY-MM-DD"}), 400

        if start_date >= end_date:
            return jsonify({"error": "End date must be after start date"}), 400

        # Calculate total cost
        days_rented = (end_date - start_date).days
        total_cost = days_rented * price_per_day

        # Create rental object
        new_rental = Rental(
            car_id=car_id,
            car_image_url=car_image_url,
            price_per_day=price_per_day,
            start_date=start_date,
            end_date=end_date,
            user_id=user_id,
            total_cost=total_cost
        )

        # Save to database
        db.session.add(new_rental)
        db.session.commit()

        return jsonify({'message': 'Rental created successfully', 'rental_id': new_rental.id}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@car_rental_bp.route('/rentals/<int:rental_id>', methods=['GET'])
@jwt_required()
def get_rental(rental_id):
    try:
        rental = Rental.query.get(rental_id)

        if not rental:
            return jsonify({'error': 'Rental not found'}), 404

        # Check if the current user is authorized to view this rental
        current_user_id = get_jwt_identity()
        if rental.user_id != current_user_id:
            return jsonify({'error': 'You are not authorized to view this rental'}), 403

        rental_data = {
            'rental_id': rental.id,
            'car_id': rental.car_id,
            'car_image_url': rental.car_image_url,
            'price_per_day': rental.price_per_day,
            'start_date': rental.start_date.strftime('%Y-%m-%d'),
            'end_date': rental.end_date.strftime('%Y-%m-%d'),
            'user_id': rental.user_id,
            'total_cost': rental.total_cost
        }

        return jsonify(rental_data), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@car_rental_bp.route('/rentals/<int:rental_id>', methods=['PUT'])
@jwt_required()
def update_rental(rental_id):
    try:
        rental = Rental.query.get(rental_id)

        if not rental:
            return jsonify({'error': 'Rental not found'}), 404

        current_user_id = get_jwt_identity()
        if rental.user_id != current_user_id:
            return jsonify({'error': 'You are not authorized to update this rental'}), 403

        data = request.get_json()

        car_id = data.get('car_id')
        car_image_url = data.get('car_image_url')
        price_per_day = data.get('price_per_day')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if not all([car_id, price_per_day, start_date, end_date]):
            return jsonify({"error": "Car ID, price per day, start date, and end date are required"}), 400

        start_date, end_date = validate_dates(start_date, end_date)
        if not start_date or not end_date:
            return jsonify({"error": "Invalid date format. Please use YYYY-MM-DD"}), 400

        if start_date >= end_date:
            return jsonify({"error": "End date must be after start date"}), 400

        days_rented = (end_date - start_date).days
        total_cost = days_rented * price_per_day

        rental.car_id = car_id
        rental.car_image_url = car_image_url
        rental.price_per_day = price_per_day
        rental.start_date = start_date
        rental.end_date = end_date
        rental.total_cost = total_cost

        db.session.commit()

        return jsonify({'message': 'Rental updated successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@car_rental_bp.route('/rentals/<int:rental_id>', methods=['DELETE'])
@jwt_required()
def delete_rental(rental_id):
    try:
        rental = Rental.query.get(rental_id)

        if not rental:
            return jsonify({'error': 'Rental not found'}), 404

        current_user_id = get_jwt_identity()
        if rental.user_id != current_user_id:
            return jsonify({'error': 'You are not authorized to delete this rental'}), 403

        db.session.delete(rental)
        db.session.commit()

        return jsonify({'message': 'Rental deleted successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
