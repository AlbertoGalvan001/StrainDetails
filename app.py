from flask_sqlalchemy import SQLAlchemy
from .models import *
from flask import Flask, render_template, request
import pandas as pd
from pandas.io import sql
import tempfile
import os
from .populate import *

def create_app():
    app = Flask(__name__)
    # server name is specified in proc file
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///MedCabinet.db"
    DB.init_app(app)

    #Base landing page
    @app.route('/', methods=['GET', 'POST'])
    def root():
        return render_template('base.html', title='Contents')

    #Reset will drop all tables, including those not in models
    @app.route('/reset')
    def reset():
        DB.drop_all()
        engine = DB.get_engine()
        sql.execute('DROP TABLE IF EXISTS med1;', engine)
        sql.execute('DROP TABLE IF EXISTS symptoms_medcab3;', engine)
        return render_template('reset.html', title='Reset')

    #Populate will load static data and data from files
    @app.route('/populate', methods=['GET', 'POST'])
    def populate():
        DB.create_all()
        populate_effects()
        populate_flavors()
        #Read from file
        populate_med1()
        populate_symptoms_medcab()
        populate_cbd()
        populate_feels()
        populate_hurts()
        populate_reviews()
        populate_helps()

        return render_template('populate.html', title='Populate')

    return app
