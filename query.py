###########################
CREATE_ROOMS_TABLE = (
    "CREATE TABLE IF NOT EXISTS rooms (id SERIAL PRIMARY KEY, name TEXT, threshold REAL);"
)
INSERT_ROOM_RETURN_ID = "INSERT INTO rooms (name) VALUES (%s) RETURNING id;"

ROOM_NAME = """SELECT name FROM rooms WHERE id = (%s)"""

#------------------------------#
CREATE_USER_TABLE = """CREATE TABLE IF NOT EXISTS users (user_id INTEGER, username TEXT, passwd TEXT);"""

INSERT_USER_TABLE = ("INSERT INTO users (user_id, username, passwd) VALUES (%s, %s, %s);")

#------------------------------#

CREATE_SENSOR_TABLE = """CREATE TABLE IF NOT EXISTS sensor_%s (sensor_id INTEGER, room_id INTEGER, 
                        temperature REAL, humidity REAL, date TIMESTAMP, FOREIGN KEY(room_id) REFERENCES rooms(id) ON DELETE CASCADE);"""

INSERT_SENSOR_TABLE = (
    "INSERT INTO  sensor_%s (sensor_id, room_id, temperature, humidity, date) VALUES (%s, %s,  %s, %s, %s);"
)
#------------------------------#




ROOM_NUMBER_OF_DAYS = """SELECT COUNT(DISTINCT DATE(date)) AS days FROM sensor_%s WHERE room_id = (%s);"""
ROOM_ALL_TIME_AVG = (
    "SELECT AVG(temperature) as average FROM sensor_%s WHERE room_id = (%s);"
)


ROOM_TERM = """SELECT DATE(sensor_%s.date) as reading_date,
AVG(sensor_%s.temperature)
FROM sensor_%s
WHERE sensor_%s.room_id = (%s)
GROUP BY reading_date
HAVING DATE(sensor_%s.date) > (SELECT MAX(DATE(sensor_%s.date))-(%s) FROM sensor_%s);"""

GLOBAL_NUMBER_OF_DAYS = (
    """SELECT COUNT(DISTINCT DATE(date)) AS days FROM sensor_%s;"""
)
GLOBAL_AVG = """SELECT AVG(temperature) as average FROM sensor_%s;"""

###########################