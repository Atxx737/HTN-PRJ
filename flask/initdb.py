# initdb.py

from app import db, app
with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.commit()
    #seed database
    # db.session.add(User(email="michael@mherman.org"))
    # db.session.commit()