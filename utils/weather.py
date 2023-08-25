import requests
from database.config import API_KEY
import datetime as dt
import time

class DaylightInfo:
    def __init__(self, response):
        self.sunrise = response["sys"]["sunrise"]
        self.sunset = response["sys"]["sunset"]
        self.timezone = response["timezone"]

    def timezone_adjust_sunrise(self):
        adjusted_sunrise = dt.datetime.utcfromtimestamp(self.sunrise + self.timezone)
        return adjusted_sunrise
    
    def timezone_adjust_sunset(self):
        adjusted_sunset = dt.datetime.utcfromtimestamp(self.sunset + self.timezone)
        return adjusted_sunset
    
    def calculate_daylight_time(self):
        daylight = self.timezone_adjust_sunset() - self.timezone_adjust_sunrise()
        return daylight
    
    def format_sunrise(self):
        formated_sunrise = self.timezone_adjust_sunrise().strftime('%H:%M:%S')
        return formated_sunrise
    
    def format_sunset(self):
        formated_sunset = self.timezone_adjust_sunset().strftime('%H:%M:%S')
        return formated_sunset
    
    def format_daylight(self):
        formated_daylight = time.strftime("%H:%M:%S", time.gmtime(self.calculate_daylight_time().seconds))
        return formated_daylight
    
    def get_advice_by_daylight_time(self):
        daylight_time = self.calculate_daylight_time()
        if daylight_time < dt.timedelta(minutes=480):
            return "The days are short and most plants will be dormant. Consider using a grow light for 6 hours, to keep them growing."
        elif dt.timedelta(minutes=480) <= daylight_time < dt.timedelta(minutes=600):
            return "The days are quite short and most plants will be dormant. Consider using a grow light for 4 hours to keep them growing."
        elif dt.timedelta(minutes=600) <= daylight_time < dt.timedelta(minutes=720):
            return "If there hasn't been much sun lately, consider treating your plants to a couple of hours of grow light."
        else:
            return "Plenty of natural light! Keep your light loving plants near the window."
            

class WeatherInfo:
    def __init__(self, response):
        self.type = response["weather"][0]["main"]
        self.details = response["weather"][0]["description"]
        self.temp = response["main"]["temp"]
        self.temp_min = response["main"]["temp_min"]
        self.temp_max = response["main"]["temp_max"]
        self.humidity = response["main"]["humidity"]

    
    def get_advice_by_weather_type(self):
        if self.type == "Thunderstorm":
            return "Keep indoors plants away from the windows to avoid drafts. Bring your outdoors plants inside or cover to protect from damage."
        elif self.type == "Rain":
            if self.details in ["light rain", "moderate rain", "light intensity shower rain"]:
                return "You can skip watering your outdoors plants for a few days. Consider using a grow light for indoor plants that enjoy full sun."
            else:
                return "Heavy rain might damage your outdoors plants. Consider bringing them inside or covering to protect from damage."
        elif self.type == "Drizzle":
            return "You can skip watering your outdoors plants for a few days. Consider using a grow light for indoor plants that enjoy full sun."
        elif self.type == "Snow":
            return "Keep your plants away from windows and consider using a grow light."
        elif self.type == "Clear":
            return "Plants that thrive in full sun will be happy! Place the ones that prefer low-light away from the window."
        elif self.type == "Clouds":
            if self.details == "few clouds":
                return "Plants that thrive in full sun and partial shade will be happy! Place the ones that prefer low-light away from the window."
            elif self.details in ["scattered clouds", "broken clouds"]:
                return "Plants that thrive in partial shade and bright indirect light will be happy! Consider using a grow light for the ones that need full sun."
            else: 
                return "Plants that thrive in low-light will be happy! Consider using a grow light for the ones that need a bit more sun."
        else:
            return "No advice available"
        
    def get_advice_by_temp(self):
        if self.temp < 5:
            return "it's very cold outside, keep your plants away from the windows. Watch for curling and browning leaves."
        elif 5 <= self.temp < 15:
            return "it's a bit chilly outside, make sure to keep your room temperature above 15C."
        elif 15 <= self.temp < 24:
            return "Most plants will be happy in this temperature."
        elif 24 <= self.temp < 30:
            return "it's very hot outside, keep your plants in the shade, mist them often and water more frequently. Watch for wilting and yellowing leaves."
        else:
            return "it's quite hot, mist your plants to help them retain moisture. Watch for wilting and yellowing leaves."
    
    def get_advice_by_humidity(self):
        if self.humidity > 80:
            return "Plenty of moisture in the air, water your plants less frequently!"
        elif 60 < self.humidity < 80:
            return "perfect for most houseplants!"
        elif 40 < self.humidity < 60:
            return "Mist your plants to help them retain moisture."
        else:
            return "It's very dry. Mist your plants often and water more frequently."    


def get_weather_data(city):
    open_weather = "http://api.openweathermap.org/data/2.5/weather?"
    url = open_weather + "&q=" + city + "&appid=" + API_KEY + "&units=metric"
    try:
        response = requests.get(url).json()
        return response
    except ConnectionError:
        "Something went wrong: Unable to process request" 




