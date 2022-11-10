import json
from datetime import datetime, timezone
from flask import Flask, request, render_template, session, jsonify
from werkzeug.security  import check_password_hash

import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env file into environment

from flask_cors import CORS
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

from query import *

app = Flask(__name__)
url = os.environ.get("DATABASE_URL")  # gets variables from environment
connection = psycopg2.connect(url)

@app.route('/')
def hello_world():
    now = datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
    return render_template('index.html', **templateData)


@app.route("/api/room", methods=[ 'POST'])
def create_room():
    data = request.get_json()
    name = data["name"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_ROOMS_TABLE)
            cursor.execute(INSERT_ROOM_RETURN_ID, (name,))
            room_id = cursor.fetchone()[0]
    return {"id": "room_id", "message": f"Room {name} created."}, 201


@app.route("/api/room/<int:room_id>", methods=['GET'])
def get_room_all(room_id):
    # with connection:
    #     with connection.cursor() as cursor:
    #         cursor.execute(ROOM_NAME, (room_id,))
    #         name = cursor.fetchone()[0]
    #         cursor.execute(ROOM_ALL_TIME_AVG, (room_id,))
    #         average = cursor.fetchone()[0]
    #         cursor.execute(ROOM_NUMBER_OF_DAYS, (room_id,))
    #         days = cursor.fetchone()[0]
    return {"name": "name", "average": round("average", 2), "days": 'days'}

@app.route("/api/sensor", methods=[ 'POST'])
def add_sensor():
    data = request.get_json()
    # sensor_id = data["sensor_id"]
    sensor_id = sensor_id

    temperature = data["temperature"]
    humidity = data["humidity"]
    room_id = data["room"]
    # try:
    #     date = datetime.strptime(data["date"], "%m-%d-%Y %H:%M:%S")
    # except KeyError:
    #     date = datetime.now(timezone.utc)
    # with connection:
    #     with connection.cursor() as cursor:
    #         cursor.execute(CREATE_SENSOR_id_TABLE)
    #         cursor.execute(INSERT_SENSOR_id_TABLE, (sensor_id, temperature, humidity, date))
    return {"message": "Sensor added."}, 201

@app.route("/api/sensor/<int:sensor_id_r>", methods=['GET', 'POST'])

@app.route("/api/user/<int:id>", methods=['GET', 'POST'])
def create_user():
    data = request.get_json()
    name = data["name"]
    # with connection:
    #     with connection.cursor() as cursor:
    #         cursor.execute(CREATE_ROOMS_TABLE)
    #         cursor.execute(INSERT_ROOM_RETURN_ID, (name,))
    #         room_id = cursor.fetchone()[0]
    return {"id": "user_id", "message": f"User {name} created."}, 201




@app.route('/login', methods=['POST'])
def login():
	conn = None;
	cursor = None;
	try:
		_json = request.json
		_username = _json['username']
		_password = _json['password']
		print(_json)		
  
		# validate the received values
		if _username and _password:
			#check user exists			
			conn = mysql.connect()
			cursor = conn.cursor()
			
			sql = "SELECT * FROM user WHERE username=%s"
			sql_where = (_username,)
			
			cursor.execute(sql, sql_where)
            
			row = cursor.fetchone()
			
			if row:
				# if check_password_hash(row[2], _password):
				if _password == row[2]:
					session['username'] = row[1]
					
					return jsonify({'message' : 'You are logged in successfully', 'username' : row[1]})
				else:
					resp = jsonify({'message' : 'Bad Request - invalid password'})
					resp.status_code = 400
					return resp
			else:
				resp = jsonify({'message' : 'Bad Request - invalid credendtials'})
				resp.status_code = 400
				return resp
		else:
			resp = jsonify({'message' : 'Bad Request - invalid credendtials'})
			resp.status_code = 400
			return resp

	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()
		
@app.route('/logout')
def logout():
	if 'username' in session:
		session.pop('username', None)
	return jsonify({'message' : 'You successfully logged out'})

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=5000)


app.secret_key = "secret key"
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=10)
CORS(app)