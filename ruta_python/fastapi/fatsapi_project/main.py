import zoneinfo
from datetime import datetime

from fastapi import FastAPI
from models import Customer, Invoce, Transaccion


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

@app.post("/customers/")
async def create_customer(customer_data: Customer):
    return customer_data

@app.post("/transactions/")
async def create_transaction(transaction_data: Customer):
    return transaction_data

@app.post("/invoices/")
async def create_customer(invoice_data: Invoce):
    return invoice_data