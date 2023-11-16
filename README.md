# Climate Analysis and Data Exploration

## Overview
This project involves a detailed climate analysis and data exploration of a climate database using Python, SQLAlchemy ORM queries, Pandas, and Matplotlib. The analysis focuses on Honolulu, Hawaii, for planning a holiday vacation.

### Technologies Used
- Python
- SQLAlchemy ORM
- Pandas
- Numpy
- Matplotlib
- Flask

## Part 1: Climate Analysis and Data Exploration

### Precipitation Analysis
- **Objective**: Analyze the last 12 months of precipitation data.
- **Method**: 
  - Query the most recent date and calculate the date one year ago.
  - Retrieve the precipitation data for the last 12 months.
  - Load data into a Pandas DataFrame and plot using Matplotlib.

### Station Analysis
- **Objective**: Perform statistical analysis on weather stations data.
- **Method**: 
  - Determine the total number of stations.
  - Identify the most active station and calculate min, max, and average temperatures.
  - Query the last year's temperature data for this station and plot as a histogram.

## Part 2: Flask API Development

### API Design
Developed a Flask API with routes to provide climate data.

### Routes
- `/`: Home page listing all routes.
- `/api/v1.0/precipitation`: JSON representation of precipitation data.
- `/api/v1.0/stations`: JSON list of stations.
- `/api/v1.0/tobs`: Temperature observations of the most active station for the last year.
- `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`: Min, max, and average temperatures for a given date range.

### Dynamic Route Handling
- Implemented dynamic routes in Flask to handle requests for different date ranges.

## Conclusion
This project successfully demonstrates the application of Python and various libraries to perform a comprehensive climate analysis, data manipulation, visualization, and creating a web API to serve climate data.
