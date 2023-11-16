# Import the dependencies
import numpy as np
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import datetime as dt


#################################################
# Database Setup
engine = create_engine("sqlite:///hawaii.sqlite")
#################################################


# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
def get_temperature_data(start_date, end_date=None):
    # Create our session (link) from Python to the DB
    session = Session(engine)
    try:
        sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
        if not end_date:
            results = session.query(*sel).filter(Measurement.date >= start_date).all()
        else:
            results = session.query(*sel).filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
        temps = list(np.ravel(results))
        return temps
    finally:
        session.close()

#################################################
# Flask Setup
app = Flask(__name__)

# Function to calculate temperatures (DRY principle)
def calc_temps(start_date, end_date=None):
    """Return TMIN, TAVG, TMAX."""
    # If no end date is provided
    if not end_date:
        end_date = dt.datetime.now()
#################################################




#################################################
# Flask Routes
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;"
    )

@app.route("/api/v1.0/<start>")
def start(start):
    """Return TMIN, TAVG, TMAX from start date to current date."""
    temp_data = calc_temps(start)
    return jsonify(temp_data=temp_data)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    """Return TMIN, TAVG, TMAX from start date to end date."""
    temp_data = calc_temps(start, end)
    return jsonify(temp_data=temp_data)

# Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
#################################################
