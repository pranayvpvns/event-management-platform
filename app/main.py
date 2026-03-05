from flask import Flask,render_template,redirect,request
from app.database import db
from app.models import *
from app.mongo import event_logs, user_activity

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///events.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db.init_app(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/participants")
def view_participants():
    participants = Participant.query.all()
    return render_template("participants.html", participants=participants)

@app.route("/participants/add", methods=["GET", "POST"])
def add_participant():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        new_participant = Participant(name=name,email=email,phone=phone)
        db.session.add(new_participant)
        db.session.commit()
        user_activity.insert_one({"action": "Participant Created","name": name,"email": email})
        return redirect("/participants")
    return render_template("add_participant.html")

@app.route("/participants/delete/<int:id>")
def delete_participant(id):
    participant = Participant.query.get(id)
    db.session.delete(participant)
    db.session.commit()
    return redirect("/participants")

@app.route("/trainers")
def view_trainers():
    trainers = Trainer.query.all()
    return render_template("trainers.html", trainers=trainers)

@app.route("/trainers/add", methods=["GET", "POST"])
def add_trainer():
    if request.method == "POST":
        name = request.form["name"]
        expertise = request.form["expertise"]
        trainer = Trainer(name=name, expertise=expertise)
        db.session.add(trainer)
        db.session.commit()
        return redirect("/trainers")
    return render_template("add_trainer.html")

@app.route("/trainers/delete/<int:id>")
def delete_trainer(id):
    trainer = Trainer.query.get(id)
    db.session.delete(trainer)
    db.session.commit()
    return redirect("/trainers")

@app.route("/events")
def view_events():
    events = Event.query.all()
    trainers = Trainer.query.all()
    return render_template("events.html",events=events,trainers=trainers)

@app.route("/events/add", methods=["GET", "POST"])
def add_event():
    trainers = Trainer.query.all()
    if request.method == "POST":
        title = request.form["title"]
        capacity = request.form["capacity"]
        trainer_id = request.form["trainer_id"]
        event = Event(title=title,capacity=capacity,trainer_id=trainer_id)
        db.session.add(event)
        db.session.commit()
        event_logs.insert_one({
        "action": "Event Created",
        "title": title,
        "capacity": capacity
    })
        return redirect("/events")
    return render_template("add_event.html",trainers=trainers)

@app.route("/events/delete/<int:id>")
def delete_event(id):
    event = Event.query.get(id)
    db.session.delete(event)
    db.session.commit()
    return redirect("/events")

@app.route("/register", methods=["GET", "POST"])
def register_event():
    participants = Participant.query.all()
    events = Event.query.all()
    if request.method == "POST":
        participant_id = request.form["participant_id"]
        event_id = request.form["event_id"]
        event = Event.query.get(event_id)
        current_count = Registration.query.filter_by(event_id=event_id).count()
        if event.capacity and current_count >= event.capacity:
            return "Event is full!"
        registration = Registration(participant_id=participant_id,event_id=event_id)
        db.session.add(registration)
        db.session.commit()
        event_logs.insert_one({
        "action": "Participant Registered",
        "participant_id": participant_id,
        "event_id": event_id
    })
        return redirect("/events")
    return render_template("register_event.html",participants=participants,events=events)

@app.route("/event/<int:event_id>/participants")
def event_participants(event_id):
    registrations = Registration.query.filter_by(event_id=event_id).all()
    return render_template("event_participants.html",registrations=registrations)

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)