from app import app
    from flask import render_template, request
from app.models.event import Event
from app.models.event_list import *

@app.route('/')
def index():
    return render_template('index.html', title="Home", event_list=event_list)

@app.route("/add-event", methods=["POST"])
def add_event():
    date = request.form["date"]
    name = request.form["name"]
    no_of_guests = request.form["no-of-guests"]
    room_location = request.form["room-location"]
    description = request.form["description"]
    is_weekly = False
    try:
        if request.form["is-weekly"]:
            is_weekly = True
    except:
        pass

    new_event = Event(date=date, name=name, num_guests=no_of_guests, room_location=room_location, description=description, is_weekly=is_weekly)
    add_new_event(new_event)
    return render_template("index.html", title="Home", event_list=event_list)

@app.route("/remove-event", methods=["POST"])
def remove_event()
    for item in event_list:
        if event.name