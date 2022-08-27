import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_map
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import FLASK, jasonify

engine=create_engine("sqlite://hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement=Base.classes.measurement
Statation=Base.classes.station
session=Session(engine)

app= Flask(__name__)

@app.rount("/")
def welcome():
    return(
        '''
        Welcome to the Climate Analysis API!
        Available Routes:
        /api/v1.0/precipitation
        /api/v1.0/stations
        /api/v1.0/tobs
        /api/v1.0/temp/start/end
        ''')

