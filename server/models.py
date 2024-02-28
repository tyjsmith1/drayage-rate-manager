from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash

from config import db

# Models go here!
class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password_hash = db.Column(db.String)
    email_address = db.Column(db.String)
    role = db.Column(db.String)
    association_id = db.Column(db.Integer, db.ForeignKey("carriers.id"))
    created_at = db.Column(db.Date, nullable=False)
    updated_at = db.Column(db.Date)

    serialize_rules = ('-password_hash','-carrier')

    def __repr__(self):
        return f'<User: {self.id}, {self.username}, {self.role}, {self.association_id}>'
    
class Carrier(db.Model, SerializerMixin):
    __tablename__ = "carriers"

    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String)
    phone = db.Column(db.String)
    address = db.Column(db.String)
    created_at = db.Column(db.Date, nullable=False)
    updated_at = db.Column(db.Date)

    users = db.relationship('User', backref='carrier', lazy='dynamic')
    rates = db.relationship('Rate', backref='carrier', lazy='dynamic')

    serialize_rules = ('-password_hash','-users', '-rates')

    def __repr__(self):
        return f'<Carrier: {self.id}, {self.company_name}>'

class Rate(db.Model, SerializerMixin):
    __tablename__ = "rates"

    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey("carriers.id"))
    origin = db.Column(db.String)
    destination = db.Column(db.String)
    rate = db.Column(db.Numeric(10,2))
    effective_date = db.Column(db.Date)
    expiry_date = db.Column(db.Date)
    accessorial_fees = db.Column(db.Numeric(10,2))
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)

    # serialize_rules = ('-carrier.users', '-carrier.rates')
    serialize_rules = ('-carrier','-user')

    def __repr__(self):
        return f'<Rate: {self.id}, {self.company_id}, {self.origin}, {self.destination}, {self.rate}>'