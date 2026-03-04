from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Setup CORS
CORS(app)

# Setup the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Registering blueprints for different routes
from auth import auth as auth_blueprint
from portfolio import portfolio as portfolio_blueprint
from market import market as market_blueprint
from alert import alert as alert_blueprint

app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(portfolio_blueprint, url_prefix='/portfolio')
app.register_blueprint(market_blueprint, url_prefix='/market')
app.register_blueprint(alert_blueprint, url_prefix='/alert')

# Main route
@app.route('/')
def home():
    return "Welcome to the Stock Portfolio Web App!"

if __name__ == '__main__':
    app.run(debug=True)