from .models import *
import os
import pandas as pd

def populate_effects():
  list_of_effects = ['Aroused', 'Creative', 'Energetic', 'Euphoric',
                    'Focused', 'Giggly', 'Happy', 'Hungry', 'Relaxed',
                    'Sleepy', 'Talkative', 'Tingly', 'Uplifted']
  for x in range(len(list_of_effects)):
      DB.session.add(Effects_list(id=x,effect_terms=list_of_effects[x]))
      DB.session.commit()
  return(len(list_of_effects))

def populate_flavors():
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
    return(len(list_of_flavors))

def populate_med1():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    engine = DB.get_engine()
    my_file = os.path.join(THIS_FOLDER, 'med1.csv')
    if my_file:
        df = pd.read_csv(my_file)
        df.to_sql('med1', con=engine)
        DB.session.commit()
    return()

def populate_symptoms_medcab():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    engine = DB.get_engine()
    my_file = os.path.join(THIS_FOLDER, 'symptoms6_medcab3.csv')
    if my_file:
        df = pd.read_csv(my_file)
        df.to_sql('symptoms_medcab3', con=engine)
        DB.session.commit()
    return()

def populate_cbd():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    engine = DB.get_engine()
    my_file = os.path.join(THIS_FOLDER, 'cbd.csv')
    if my_file:
        df = pd.read_csv(my_file)
        df.to_sql('cbd', con=engine)
        DB.session.commit()
    return()

def populate_feels():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    engine = DB.get_engine()
    my_file = os.path.join(THIS_FOLDER, 'feels.csv')
    if my_file:
        df = pd.read_csv(my_file)
        df.to_sql('feels', con=engine)
        DB.session.commit()
    return()

def populate_helps():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    engine = DB.get_engine()
    my_file = os.path.join(THIS_FOLDER, 'helps.csv')
    if my_file:
        df = pd.read_csv(my_file)
        df.to_sql('helps', con=engine)
        DB.session.commit()
    return()

def populate_hurts():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    engine = DB.get_engine()
    my_file = os.path.join(THIS_FOLDER, 'hurts.csv')
    if my_file:
        df = pd.read_csv(my_file)
        df.to_sql('hurts', con=engine)
        DB.session.commit()
    return()

def populate_reviews():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    engine = DB.get_engine()
    my_file = os.path.join(THIS_FOLDER, 'reviews.csv')
    if my_file:
        df = pd.read_csv(my_file)
        df.to_sql('reviews', con=engine)
        DB.session.commit()
    return()
