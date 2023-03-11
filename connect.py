# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import psycopg2
# from IPython.display import display, HTML # used to print out pretty pandas dataframes
# import matplotlib.dates as dates
# import matplotlib.lines as mlines

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# con = psycopg2.connect('postgres://lumineuxp:hgnuPHIJS9O7@ep-raspy-hall-234246.ap-southeast-1.aws.neon.tech/syn_voice_app', sslmode='require')
# query = 'select * from tales'
# db = pd.read_sql_query(query,con)

# create the extension
db = SQLAlchemy()

class Tales(db.Model):
    __tablename__ = "tales"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    story = db.Column(db.String, nullable=False) 
    cover_img = db.Column(db.String, nullable=False)