# College Bus Live Tracking System

Interactive Flask + JavaScript map dashboard for college buses.

## Features
- Multiple buses
- Interactive Leaflet map
- Route and driver information
- Simulated location updates every 2 seconds
- JSON API at `/api/buses`
- Responsive dashboard

## Tech Stack
Python, Flask, HTML, CSS, JavaScript, Leaflet, OpenStreetMap

## Run on Windows
```bash
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000

## Note
This is a portfolio/demo project and simulates GPS movement. For real tracking, connect an authorized GPS/location source to the backend.
