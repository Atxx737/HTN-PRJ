from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()

# Models
class Rooms(db.Model):
  
    room_id = db.Column(db.String(6), primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    theshold_tem = db.Column(db.Float, nullable=False)
    theshold_hum = db.Column(db.Float, nullable=False)
 
    # repr method represents how one object of this datatable
    # will look like
    def __repr__(self):
        return f"Name : {self.name}, Theshold of temperature: {self.theshold_tem}, Theshold of humidity: {self.theshold_hum}"

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=False, nullable=False)
    passwd = db.Column(db.String(), nullable=False)
 
    # repr method represents how one object of this datatable
    # will look like
    def __repr__(self):
        return f"username : {self.username}, password: {self.passwd}"
    

class Sensors(db.Model):
    sensor_id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.String(6), db.ForeignKey('rooms.room_id', ondelete='CASCADE'), nullable=False)
    temperature = db.Column(db.Float, unique=False, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    date = db.Column(db.TIMESTAMP, nullable=False)
    # repr method represents how one object of this datatable
    # will look like
    def __repr__(self):
        return f"sensor_id : {self.sensor_id}, room_id: {self.room_id}, temperature: {self.temperature}, humidity: {self.humidity}, date: {self.date} "