from app import db
from marshmallow import Schema, fields


class PersonalItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String)
    price_1m3_120kg = db.Column(db.Integer)
    price_2m3_220kg = db.Column(db.Integer)
    price_3m3_360kg = db.Column(db.Integer)
    price_4m3_480kg = db.Column(db.Integer)
    price_allowance_for_1m3 = db.Column(db.Integer)


class PersonalItemSchema(Schema):
    id = fields.Integer()
    country = fields.String()
    price_1m3_120kg = fields.Integer()
    price_2m3_220kg = fields.Integer()
    price_3m3_360kg = fields.Integer()
    price_4m3_480kg = fields.Integer()
    price_allowance_for_1m3 = fields.Integer()
