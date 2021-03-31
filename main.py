from fastapi import FastAPI
import pytz
from datetime import datetime as dt
from fastapi.responses import HTMLResponse

tags_metadata = [
    {
        "name": "info",
        "description": "GET Date and Time.",
    },
    {
        "name": "homepage",
        "description": "Landing Page."
    }
]

app = FastAPI(
    title="DateTimeAPI",
    description="Just a sample API I made in the process of learning FastAPI xD",
    version="0.0.1",
    openapi_tags=tags_metadata
)

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

@app.get("/info", tags=["info"])
def get_time(tz: str = "Asia/Kolkata"):
    return get_datetime(tz)

@app.get("/", response_class=HTMLResponse, tags=["homepage"])
def root():
    msg = """
    <html>
        <head>
            <title>HomePage - DateTimeAPI</title>
        </head>
        <body>
            <h1>WELCOME!</h1>
            Please GET <code>/info</code> for more. </br>
            GET <code>/info?tz=</code> for all available time zones.</br></br>
            Join <a href="https://t.me/BotzHub">@BotzHub</a> for more :)
        </body>
    </html>
"""
    return msg