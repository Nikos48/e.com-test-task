from tinydb import TinyDB
db = TinyDB("templates.json")

db.insert({
    "name": "registration",
    "user_phone": "phone",
    "user_email": "email",
    "registraion_date": "date",
    "biography": "text"
})

db.insert({
    "name": "login",
    "login": "text",
    "password": "text"
})

db.insert({
    "name": "call",
    "host": "phone",
    "destination": "phone"
})

db.insert({
    "name": "message",
    "message": "text",
    "host": "email",
    "destination": "email",
    "message_date": "date"
})
