from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import random
import datetime

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Simulated flight route (Doha -> Brisbane)
FLIGHT_PATH = [
    (25.276987, 51.520008, 10000),  # Doha (Starting point)
    (20.0, 60.0, 30000),            # Over the Indian Ocean
    (10.0, 100.0, 35000),           # Mid-point
    (-10.0, 130.0, 34000),          # Near Australia
    (-27.470125, 153.021072, 5000)  # Brisbane (Landing)
]

def generate_fake_flight():
    flight_number = f"QR{random.randint(100, 999)}"
    departure_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=random.randint(30, 300))
    arrival_time = departure_time + datetime.timedelta(hours=14)

    return {
        "flight_number": flight_number,
        "departure": "Doha, Qatar (DOH)",
        "arrival": "Brisbane, Australia (BNE)",
        "departure_time": departure_time.strftime("%Y-%m-%d %H:%M:%S UTC"),
        "arrival_time": arrival_time.strftime("%Y-%m-%d %H:%M:%S UTC"),
        "status": "Incoming",
        "route": FLIGHT_PATH
    }

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/flight/")
async def get_flight():
    return generate_fake_flight()
