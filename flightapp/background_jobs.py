# import schedule
# import time
# from app import app
# from tequila_api import get_flight_price
# from database import get_tracked_flights, update_flight_price, get_users_for_flight
# from notification_service import send_notification

# def check_flight_prices():
#     with app.app_context():
#         tracked_flights = get_tracked_flights()

#         for flight in tracked_flights:
#             current_price = get_flight_price(flight.flight_number)
#             if current_price < flight.max_price:
#                 users_to_notify = get_users_for_flight(flight.id)
#                 for user in users_to_notify:
#                     send_notification(user.email, flight.flight_number, current_price)
#             update_flight_price(flight.id, current_price)

# def start_scheduler():
#     schedule.every(6).hours.do(check_flight_prices)

#     def run_scheduler():
#         while True:
#             schedule.run_pending()
#             time.sleep(1)

#     scheduler_thread = Thread(target=run_scheduler)
#     scheduler_thread.start()