"""
Flight-Tracker accounts view

URLs Include:

auth_routes/login
auth_routes/logout
auth_routes/create
auth_routes/delete
auth_routes/edit
auth_routes/password
"""

from flask import Blueprint, request, jsonify, session, render_template, redirect, url_for
from models import db, User

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/login', methods=['POST', 'GET'])
def show_accounts_login():

    if request.method == 'GET':
        return render_template(url_for('login.html'))

    if request.method == 'POST':
        data = request.json
        username = data.get('username')
        
        user = User.query.filter_by(username=username).first()

        if user:
            # Set session or generate token to mark user as authenticated
            session['user_id'] = user.id
            return jsonify({'message': 'Login successful', 'user': {'id': user.id, 'username': user.username}})
        else:
            return jsonify({'message': 'Invalid credentials'}), 401

@auth_routes.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)  # Remove user from session
    return redirect(url_for('show_accounts_login'))
    # return jsonify({'message': 'Logout successful'})

@auth_routes.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return render_template('user.html', user = user)
    else:
        return redirect(url_for('login'))
# Other authentication-related routes can be added here
