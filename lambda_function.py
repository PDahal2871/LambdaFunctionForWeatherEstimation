import json
import logging
from pyowm.owm import OWM  #Used to get data from the weather api

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def lambda_handler(event, context):
    #TODO implement
    logger.debug(event)
    city = event["currentIntent"]["slots"]["City"];
    owm = OWM('068b6ba70ba098c7ef600f077f63ce08') #API key
    mngr = owm.weather_manager()
    weather = mngr.weather_at_place(city).weather
    temp_dict_celsius = weather.temperature('celsius')

    sunrise_date = weather.sunrise_time(timeformat='date')
    sunrset_date = weather.sunset_time(timeformat='date')

    answer = "The weather of "+ city+ " is " + weather.detailed_status + " with " + str(temp_dict_celsius['temp']) + " C as average temperature. The sun rose at around "+ str(sunrise_date) + " and is expected to set at around " + str(sunrset_date);

    return {
        "sessionAttributes": event["sessionAttributes"],
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": answer
            }
        }
    }


