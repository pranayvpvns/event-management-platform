from app.database import db

class Event(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    capacity = db.Column(db.Integer)
    trainer_id = db.Column(db.Integer, db.ForeignKey("trainers.id"))
    trainer = db.relationship("Trainer", back_populates="events")
    registrations = db.relationship("Registration", back_populates="event")