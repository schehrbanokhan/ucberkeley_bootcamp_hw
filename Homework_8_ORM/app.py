import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import datetime as dt

# Setting up Database 

engine = create_engine("sqlite:///Resources/hawaii.sqlite")


Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

# Setting up flask

app = Flask(__name__)

# Flask Routes

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/2017-02-03<br/>"
        f"/api/v1.0/2017-06-10/2017-06-25<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    last_date = dt.datetime.strptime(last_date[0], '%Y-%m-%d')
    

    year_ago = last_date - dt.timedelta(days=366)
    

    prcp_date = session.query( Measurement.prcp,Measurement.date).filter(Measurement.date >= year_ago).\
                order_by(Measurement.date).all()
    
    prcp1 = pd.DataFrame(prcp_date, columns=["Precipitation", "Date"])

    prcp1.set_index(["Date"], inplace = True, drop = True)

    prcp1.sort_index(inplace=True)
    prcp_dict = prcp1.to_dict()
    session.close() 
    return jsonify(prcp_dict)

#Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():
    station = session.query(Station.station,Station.name).all()
    session.close()
    return jsonify(station)
    
#query for the dates and temperature observations from a year from the last data point.
@app.route("/api/v1.0/tobs")
def tobs():
    
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    last_date = dt.datetime.strptime(last_date[0], '%Y-%m-%d')
           
    year_ago = last_date - dt.timedelta(days=366)
    
    tmp_date = session.query(Measurement.date,Measurement.tobs).filter(Measurement.date >= year_ago).\
                 order_by(Measurement.date).all()
    
    tobs1 = pd.DataFrame(tmp_date, columns=['temperature', 'date'])
    tobs1.set_index('date', inplace=True)
    out_tobs = tobs1.to_dict()
    
    session.close()
    return jsonify(out_tobs)


@app.route("/api/v1.0/<start>")
def start_dt(start):
    
    trip_start_date = dt.datetime.strptime(start, "%Y-%m-%d")
        
    pd_val = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
             filter(Measurement.date >= trip_start_date).all()
    minT, avgT, maxT = pd_val[0] 

    if minT is None:
        session.close()
        return jsonify({"error": f"Input date : {start} not found."})
        
        
    session.close()
    return jsonify(pd_val)
        

@app.route("/api/v1.0/<start>/<end>")
def start_end(start,end):
    
    first_date = session.query(Measurement.date).order_by(Measurement.date).first()
    first_date = dt.datetime.strptime(first_date[0], '%Y-%m-%d')
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    last_date = dt.datetime.strptime(last_date[0], '%Y-%m-%d')
    
    trip_start_date = dt.datetime.strptime(start, "%Y-%m-%d")
    trip_end_date = dt.datetime.strptime(end, "%Y-%m-%d")
    
    if trip_start_date > trip_end_date:
        
        session.close()
        return jsonify({"error": f"Start date is > than End date.Valid range is {first_date}- {last_date}"})
                
    
    pd_values = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= trip_start_date).filter(Measurement.date <= trip_end_date).all()
    minT, avgT, maxT = pd_values[0] 
    
    if minT is None: 
        session.close()
        return jsonify({"error": f"Input date : {start},{end} not found.Valid range is {first_date}- {last_date}"})
    
    session.close()
    return jsonify(pd_values)


if __name__ == '__main__':
    app.run(debug=True)
