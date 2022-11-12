# initdb.py

from app import db, app
from models import Rooms, Users
with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.commit()

    #seed database
    db.session.add(Rooms(room_id="STR01",name='Machines Storage',theshold_tem="50",theshold_hum="80"))
    db.session.add(Rooms(room_id="STR02",name='Facilities Storage',theshold_tem="60",theshold_hum="80"))
    db.session.add(Rooms(room_id="DRY01",name='Dried Veggies Storag',theshold_tem="30",theshold_hum="65"))
    db.session.add(Rooms(room_id="DAI02",name='Dairy Storage',theshold_tem="25",theshold_hum="85"))
    db.session.add(Rooms(room_id="CTL01",name='Control Panel 1',theshold_tem="50",theshold_hum="85"))

    db.session.add(Users(user_id="1",username="admin",passwd="admin"))
    db.session.commit()