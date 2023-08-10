# app.py
import os
import requests
from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
# import boto3

flight_routes = Blueprint('flight_routes', __name__)

# # Replace 'YOUR_TEQUILA_API_KEY' with your actual Tequila API key
# TEQUILA_API_KEY = 'qpBYzp6Wtw3QAo3UlbInmE89iF35Po-h'

# # # AWS SNS Configuration (Update with your AWS SNS details)
# # AWS_REGION = 'us-east-1'
# # AWS_ACCESS_KEY_ID = 'YOUR_AWS_ACCESS_KEY_ID'
# # AWS_SECRET_ACCESS_KEY = 'YOUR_AWS_SECRET_ACCESS_KEY'
# # SNS_TOPIC_ARN = 'YOUR_SNS_TOPIC_ARN'

# def search_flights(origin, destination, departure_date, return_date):
#     endpoint = 'https://tequila-api.kiwi.com/v2/search'

#     headers = {
#         'apikey': TEQUILA_API_KEY
#     }

#     params = {
#         'fly_from': origin,
#         'fly_to': destination,
#         'date_from': departure_date,
#         'date_to': return_date,
#         'curr': 'USD',
#         'adults': 1,
#         'limit': 10
#     }

#     response = requests.get(endpoint, headers=headers, params=params)

#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None

# # def send_notification(flight_data):
# #     client = boto3.client('sns', region_name=AWS_REGION, aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

# #     message = f"Flight Price Alert: {flight_data['cityFrom']} to {flight_data['cityTo']} - ${flight_data['price']}"
# #     subject = f"Flight Price Alert - {flight_data['cityFrom']} to {flight_data['cityTo']}"

# #     response = client.publish(TopicArn=SNS_TOPIC_ARN, Message=message, Subject=subject)

# #     return response

# @app.route('/api/flights', methods=['GET'])
# def get_flights():
#     origin = request.args.get('origin')
#     destination = request.args.get('destination')
#     departure_date = request.args.get('departure_date')
#     max_price = float(request.args.get('max_price', 0))

#     origin = 'DTW'
#     destination = 'LGA'
#     departure_date = '08/09/2023'
#     return_date = '08/12/2023'
#     max_price = float(1000)

#     if not (origin and destination and departure_date):
#         return jsonify({'error': 'Missing parameters. Please provide origin, destination, and departure_date.'}), 400

#     flights_data = search_flights(origin, destination, departure_date, return_date)

#     if flights_data:
#         filtered_flights = [flight for flight in flights_data['data'] if flight['price'] <= max_price]
#         if filtered_flights:
#             for flight in filtered_flights:
#                 print(flight)
#                 # send_notification(flight)
#             return jsonify(filtered_flights)
#         else:
#             return jsonify({'message': 'No flights available within your budget.'}), 200
#     else:
#         return jsonify({'error': 'Failed to fetch flights data.'}), 500

# if __name__ == '__main__':
#     app.run(debug=True)

