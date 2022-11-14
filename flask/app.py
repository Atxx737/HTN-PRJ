import json
from datetime import datetime
from flask import Flask, request, render_template, session, jsonify, redirect, url_for, flash
from werkzeug.security  import check_password_hash, generate_password_hash
from flask_login import login_required, logout_user, login_user

from dotenv import load_dotenv
import os
from flask_migrate import Migrate
load_dotenv()  # loads variables from .env file into environment

from flask_cors import CORS
from flask_mail import Mail, Message
from models import db, Rooms, Sensors, Users

app = Flask(__name__)
app.debug = os.environ['FLASK_DEBUG']

mail = Mail(app) # instantiate the mail class
   
# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'demoproject.uit@gmail.com'
app.config['MAIL_PASSWORD'] = "asglpxlejhmwwzfc"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
# our database uri

dbtype = os.environ['DB_TYPE']
username = os.environ['DB_USER']
password = os.environ['DB_PASSWORD']
hostname = os.environ['DB_HOST']
port = os.environ['DB_PORT']
dbname = os.environ['DB_NAME']

# # docker_postgres_name = "db-postgres"
# docker_postgres_name = "database-postgres-htn-1.c8cawpg1pytc.ap-southeast-1.rds.amazonaws.com"

app.config["SQLALCHEMY_DATABASE_URI"] = f"{dbtype}://{username}:{password}@{hostname}:{port}/{dbname}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def hello_world():
    if 'username' in session:
        all_rooms = Rooms.query.order_by(Rooms.room_id).all()
        metric= Sensors.query.order_by(Sensors.room_id).all()
            
        templateData={
            "all_rooms":all_rooms,
           
            "metric":metric,
            }

       
        return render_template('index.html',**templateData)
    return redirect(url_for('login'))


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

@app.route("/api/allroom/<string:room_id>", methods=['GET'])
def get_all_room(room_id):
    if request.method == 'GET':
        
        m_temp= Sensors.query.order_by(Sensors.room_id).limit(2).all()
        #    m_temp= db.session.query(Sensors.temperature).filter_by(room_id=room_id).order_by(Sensors.date).all()
    return {"m_temp ": f"{m_temp}"}, 201
    # return render_template('index.html', **all_rooms)

@app.route("/api/room/<string:room_id>", methods=['GET'])
def get_metric_room(room_id):
    # room = Rooms.query.filter_by(room_id=room_id).first()
    all_rooms = Rooms.query.order_by(Rooms.room_id).all() 
    metric = db.session.query(Sensors.date,Sensors.temperature,Sensors.humidity).filter_by(room_id=room_id).order_by(Sensors.date).limit(20).all()
    # m_date= db.session.query(Sensors.date).filter_by(room_id=room_id).order_by(Sensors.date).all()
    # m_temp= db.session.query(Sensors.date,Sensors.temperature).filter_by(room_id=room_id).order_by(Sensors.date).all()
    # m_temp= Sensors.query.filter_by(room_id=room_id).order_by(Sensors.date).all()
    # m_hum= db.session.query(Sensors.humidity).filter_by(room_id=room_id).order_by(Sensors.date)

    roomDetail=Rooms.query.filter_by(room_id=room_id).first()

    room= Sensors.query.filter_by(room_id=room_id).order_by(Sensors.date.desc()).first()
    templateData={
        "all_rooms":all_rooms,
    
        "metric":metric,
        "room":room,
        "roomDetail":roomDetail

    }
    # return render_template('chart.html', all_rooms=all_rooms, m_date=m_date,m_temp=m_temp, m_hum=m_hum)
    return render_template('chart.html', **templateData)

@app.route("/api/sensor", methods=[ 'POST'])
def add_sensor():
    if request.method == 'POST':

        data = request.get_json()
        # _id = data["id"]
        sensor_id = data["sensor_id"]
        room_id = data["room_id"]
        temperature = data["temperature"]
        humidity = data["humidity"]
        date= data["date"]
        sensor= Sensors(sensor_id=sensor_id,room_id=room_id,temperature=temperature,humidity=humidity,date=date)
        db.session.add(sensor)
        db.session.commit()
        roomDetail=Rooms.query.filter_by(room_id=room_id).first()

    if temperature > roomDetail.theshold_tem or humidity > roomDetail.theshold_hum:
        msg = Message(
            'Alert!',
            sender ='demoproject.uit@gmail.com',
            recipients = ['20520625@gm.uit.edu.vn']
        )
        msg.body = 'The temperature or the humidity is over threshold!!!'
        mail.send(msg)
    return {"message": "Sensor added."}, 201
    
# @app.route("/api/sensor/<int:room_id>", methods=['GET'])


@app.route("/api/user", methods=[ 'POST'])
def add_user():
    if request.method == 'POST':
        
        data = request.get_json()
        # sensor_id = data["sensor_id"]
        # user_id = data["user_id"]
        username = data["username"]
        passwd = generate_password_hash(data["passwd"])
        user= Users(username=username,passwd=passwd)
        db.session.add(user)
        db.session.commit()
    return {"message": f"User {username} added."}, 201

# LOGIN METHOD
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_post', methods=['POST'])
def login_post():
    if request.method == 'POST':
        username = request.form.get('username')
        passwd = request.form.get('password') 
        
        user = Users.query.filter_by(username=username).first()
        if user is not None and check_password_hash(user.passwd, passwd):
            session['username'] = user.username
            return redirect(url_for('hello_world'))

        flash('Wrong password or username!')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
	# if 'username' in session:
    session.pop('username', None)
    return redirect('/')
   

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=5000)


# app.secret_key = "secret key"
# app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=10)
# CORS(app)