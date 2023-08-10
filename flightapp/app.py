from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api import flight_routes 
# from background_jobs import start_scheduler

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

app.register_blueprint(flight_routes)

if __name__ == '__main__':
    # start_scheduler()
    app.run(debug=True)