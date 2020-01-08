"""Define the structure of the DB"""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class Effects_list(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    effect_terms = DB.Column(DB.String(120), nullable=False)

    def __repr__(self):
        return '<Effects_list {}>'.format(self.effect_terms)

class Flavors_list(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    flavor_terms = DB.Column(DB.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Flavors_list {}>'.format(self.flavor_terms)
