import json
from datetime import datetime, timezone
from flask import Flask, request, render_template, session, jsonify
from werkzeug.security  import check_password_hash, generate_password_hash

import os
import psycopg2
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
load_dotenv()  # loads variables from .env file into environment

from flask_cors import CORS

from models import db, Rooms, Sensors, Users

app = Flask(__name__)
app.debug = True

app.config['SECRET_KEY'] = 'thisissecret'
# our database uri
username = "postgres"
password = "mysecretpassword"
dbname = "testdb"
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{username}:{password}@localhost:5432/{dbname}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def hello_world():
    now = datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
    return render_template('index.html', **templateData)


@app.route("/api/room", methods=['POST'])
def add_room():
    if request.method == 'POST':
        data = request.get_json()
        room_id = data["room_id"]
        name = data["name"]
        theshold_tem = data["theshold_tem"]
        theshold_hum= data["theshold_hum"]
        room = Rooms(room_id=room_id,name=name,theshold_tem=theshold_tem,theshold_hum=theshold_hum)
        db.session.add(room)
        db.session.commit()
    return {"id": room_id, "message": f"Room {name} created."}, 201


@app.route("/api/room/<string:room_id>", methods=['GET'])
def get_room(room_id):
    room = Rooms.query.filter_by(room_id=room_id).first()

    return {"room " f"{room_id}": f"{room}"}, 201

@app.route("/api/sensor", methods=[ 'POST'])
def add_sensor():
    if request.method == 'POST':
            data = request.get_json()
            # sensor_id = data["sensor_id"]
            sensor_id = data["sensor_id"]
            room_id = data["room_id"]
            temperature = data["temperature"]
            humidity = data["humidity"]
            date= data["date"]
            sensor= Sensors(sensor_id=sensor_id,room_id=room_id,temperature=temperature,humidity=humidity,date=date)
            db.session.add(sensor)
            db.session.commit()
    return {"message": "Sensor added."}, 201

@app.route("/api/sensor/<int:sensor_id_r>", methods=['GET', 'POST'])
def display_sensor():
    return 1

@app.route("/api/user", methods=[ 'POST'])
def add_user():
    if request.method == 'POST':
        data = request.get_json()
        # sensor_id = data["sensor_id"]
        user_id = data["user_id"]
        username = data["username"]
        passwd = generate_password_hash(data["passwd"])
        user= Users(user_id=user_id,username=username,passwd=passwd)
        db.session.add(user)
        db.session.commit()
    return {"message": f"User {username} added."}, 201

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        # username = request.form.get('username')
        # password = request.form.get('password')
        data = request.get_json()
        username = data["username"]
        passwd = data["passwd"]
        user = Users.query.filter_by(username=username).first()
        if user is not None and check_password_hash(user.passwd, passwd):
            session['user_id'] = user.user_id
            return {"message": f"User {username} logged in successfully.\n"+"Session:" f"{username}"}, 201
        else:
            return {"message": f"User {username} not found."}, 400
    return render_template('index.html')
		
@app.route('/logout')
def logout():
	if 'username' in session:
		session.pop('username', None)
	return jsonify({'message' : 'You successfully logged out'})

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=5000)


# app.secret_key = "secret key"
# app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=10)
# CORS(app)