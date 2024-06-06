import azure.functions as func
import logging
from datetime import datetime
from zoneinfo import ZoneInfo

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger1")
def http_trigger1(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Set the timezone to Toronto
    toronto_tz = ZoneInfo("America/Toronto")
    
    # Get current time in Toronto
    toronto_time = datetime.now(toronto_tz).strftime('%Y-%m-%d %H:%M:%S')

    # Return the current time in Toronto
    return func.HttpResponse(f"The current time in Toronto, Canada is: {toronto_time}", status_code=200)

