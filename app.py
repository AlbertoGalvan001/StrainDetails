from flask_sqlalchemy import SQLAlchemy
from .models import *
from flask import Flask, render_template, request
import pandas as pd
from pandas.io import sql
import tempfile
import os

def create_app():
    app = Flask(__name__)
    # server name is specified in proc file
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///MedCabinet.db"
    DB.init_app(app)

    @app.route('/', methods=['GET', 'POST'])
    def root():
        return render_template('base.html', title='Contents', shape='')

    @app.route('/reset')
    def reset():
        DB.drop_all()
        engine = DB.get_engine()
        sql.execute('DROP TABLE med1;', engine)
        sql.execute('DROP TABLE symptoms2_medcab3;', engine)
        return render_template('base.html', title='Reset', shape='')

    @app.route('/populate', methods=['GET', 'POST'])
    def populate():
        DB.create_all()
        list_of_effects = ['Aroused', 'Creative', 'Energetic', 'Euphoric',
                          'Focused', 'Giggly', 'Happy', 'Hungry', 'Relaxed',
                          'Sleepy', 'Talkative', 'Tingly', 'Uplifted']
        for x in range(len(list_of_effects)):
            DB.session.add(Effects_list(id=x,effect_terms=list_of_effects[x]))
            DB.session.commit()
        list_of_flavors = ['Ammonia', 'Apple','Apricot', 'Berry', 'Blue',
                          'Blueberry', 'Citrus', 'Cheese', 'Chemical',
                          'Chestnut', 'Diesel', 'Earthy', 'Flowery',
                          'Fruit', 'Grape', 'Grapefruit', 'Honey',
                          'Lavender', 'Lemon', 'Mango', 'Menthol',
                          'Mint', 'Minty', 'Nutty', 'Orange', 'Peach',
                          'Pepper','Pine','Pineapple','Pungent','Sage',
                          'Skunk','Spicy/Herbal','Strawberry','Sweet',
                          'Tea','Tobacco','Tree','Tropical','Vanilla',
                          'Violet','Woody']
        for x in range(len(list_of_flavors)):
                DB.session.add(Flavors_list(id=x,flavor_terms=list_of_flavors[x]))
                DB.session.commit()
        #Read from file
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        engine = DB.get_engine()

        my_file = os.path.join(THIS_FOLDER, 'med1.csv')
        if my_file:
            df = pd.read_csv(my_file)
            df.to_sql('med1', con=engine)
            DB.session.commit()

        my_file = os.path.join(THIS_FOLDER, 'symptoms6_medcab3.csv')
        if my_file:
            df = pd.read_csv(my_file)
            df.to_sql('symptoms2_medcab3', con=engine)
            DB.session.commit()

        return render_template('base.html', title='Populate', shape='')
    return app
