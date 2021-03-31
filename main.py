from fastapi import FastAPI
import pytz
from datetime import datetime as dt

app = FastAPI()


def get_datetime(tz):
    try:
        k = pytz.timezone(tz)
    except pytz.exceptions.UnknownTimeZoneError:
        tmp = pytz.all_timezones
        ttt = ""
        for i in tmp:
            ttt += i + ", "
        return {"available_timezones": f"{ttt}"}
    month = dt.now(k).strftime("%B")
    day = dt.now(k).strftime("%d")
    year =  dt.now(k).strftime("%Y")
    t = dt.now(k).strftime("%H:%M:%S")
    return {"day": f"{day}", "month": f"{month}", "year": f"{year}", "time": f"{t}"}

@app.get("/info")
def get_time(tz: str = "Asia/Kolkata"):
    return get_datetime(tz)