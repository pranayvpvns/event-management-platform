from app.database import db

class Registration(db.Model):
    __tablename__ = "registrations"
    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer,db.ForeignKey("participants.id"))
    event_id = db.Column(db.Integer,db.ForeignKey("events.id"))
    
    participant = db.relationship("Participant", back_populates="registrations")
    event = db.relationship("Event", back_populates="registrations")