import json
from datetime import datetime
from flask import Flask, request, render_template, session, jsonify, redirect, url_for, flash
from werkzeug.security  import check_password_hash, generate_password_hash
from flask_login import login_required, logout_user, login_user

# from dotenv import load_dotenv
from flask_migrate import Migrate
# load_dotenv()  # loads variables from .env file into environment

from flask_cors import CORS

from models import db, Rooms, Sensors, Users

app = Flask(__name__)
app.debug = True

app.config['SECRET_KEY'] = 'thisissecret'
# our database uri
username = "postgres"
password = "password"
dbname = "htn_db"
docker_postgres_name = "db-postgres"

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{username}:{password}@{docker_postgres_name}:5432/{dbname}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def hello_world():
    # if 'username' in session:
        all_rooms = Rooms.query.order_by(Rooms.room_id).all()
        
        # context={
        # "all_rooms":all_rooms,
        # # "ProjectDone":prjDone,
        # # "ProjectTotal":prjTotal,
        # }

        return render_template('index.html',all_rooms=all_rooms)
    # return redirect(url_for('login'))


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

@app.route("/api/allroom", methods=['GET'])
def get_all_room():
    if request.method == 'GET':
        all_rooms = Rooms.query.order_by(Rooms.room_id).all()
    return {"all_rooms ": f"{all_rooms}"}, 201
    # return render_template('index.html', **all_rooms)

@app.route("/api/room/<string:room_id>", methods=['GET'])
def get_room(room_id):
    room = Rooms.query.filter_by(room_id=room_id).first()
    metric = Sensors.query.order_by(Sensors.room_id).all()
    
    return {"room " f"{room_id}": f"{room} + metric " f"{metric}" }, 201

@app.route("/api/sensor", methods=[ 'POST'])
def add_sensor():
    if request.method == 'POST':

            data = request.get_json()
            _id = data["id"]
            sensor_id = data["sensor_id"]
            room_id = data["room_id"]
            temperature = data["temperature"]
            humidity = data["humidity"]
            date= data["date"]
            sensor= Sensors(id=_id,sensor_id=sensor_id,room_id=room_id,temperature=temperature,humidity=humidity,date=date)
            db.session.add(sensor)
            db.session.commit()
    return {"message": "Sensor added."}, 201
    
# @app.route("/api/sensor/<int:room_id>", methods=['GET'])


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

# LOGIN METHOD
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    if request.method == 'POST':
        username = request.form.get('username')
        passwd = request.form.get('password') 
        
        user = Users.query.filter_by(username=username).first()
        if user is not None and check_password_hash(user.passwd, passwd):
            session['user_id'] = user.user_id
            return redirect(url_for('hello_world'))

        flash('Wrong password or username!')
        return redirect(url_for('login'))


@app.route('/logout')
@login_required
def logout():
	if 'username' in session:
		session.pop('username', None)
	return redirect('/')
   
    # return redirect(url_for('hello_world'))


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=5000)


# app.secret_key = "secret key"
# app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=10)
# CORS(app)