import zoneinfo
from fastapi import FastAPI
from datetime import datetime


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello David"}

country_timezones = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima",
}

@app.get("/time/{iso_code}")
async def time(iso_code: str):
    if iso_code not in country_timezones:
        return {"error": "Country not found"}
    iso = iso_code.upper()
    timezone_str = country_timezones.get(iso)
    tz = zoneinfo.ZoneInfo(timezone_str)
    return {"time": datetime.now(tz)}