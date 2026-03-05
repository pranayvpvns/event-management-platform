from app.database import db

class Participant(db.Model):
    __tablename__="participants"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(50),nullable=False)
    phone=db.Column(db.String(20))
    
    registrations=db.relationship("Registration",back_populates="participant")