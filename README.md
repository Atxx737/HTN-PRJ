# BACK-END WEB SERVER USING FLASK FRAMEWORK 
 
<h3> API in server </h3>

`POST` method : client send data to server

- `/api/room`: client send data of room to create new room

> {
    "room_id":"STR01", 
    "name":"Machines Storage",
    "theshold_tem": "50",
    "theshold_hum":"85"
}

- `/api/sensor`: update temperature and humidity of room

> {
	"sensor_id":"DHT01",
    "room_id":"STR01", 
    "temperature":"30",
    "humidity": "50",
    "date":"2022-11-11 9:57 PM"
}

- `/api/user`: clien send data of user to create new user

> {
    "username":"admin", 
    "passwd":"admin"
}



<h3> To run this you can use Docker </h3>

1. Install Docker 
2. Clone this repo, using command `git clone git@github.com:Atxx737/HTN-PRJ.git`
3. In this folder of repo - where the docker-compose.yml file in it, run this command `docker compose up -d` or `docker-compose up -d`
4. Open website with URL `http://localhost` or `http://your_ip_machine`

<h3> Note: Create file /flask/.env with format </h3>

DB_TYPE=<type_database>

DB_HOST=<host_database>

DB_PORT=<port_running_database>

DB_NAME=<name_database>

DB_USER=<username_of_database>

DB_PASSWORD=<password_of_database>


FLASK_APP=app.py 

FLASK_DEBUG=1

SECRET_KEY=<your_sercet_key>

F_MAIL_USERNAME=<your_email_to_sending_alert>

F_MAIL_PASSWORD=<your_password_of_email>