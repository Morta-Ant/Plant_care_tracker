from unittest import TestCase
import datetime
from utils.weather import WeatherInfo, DaylightInfo

class TestWeatherInfo(TestCase):

    def test_get_advice_by_weather_known_type(self):

        response = {
            "weather":[{"main":"Rain", "description":"light rain"}],
            "main":{"temp":17, "humidity":60}
        }

        weather_info = WeatherInfo(response)
        expected = "You can skip watering your outdoors plants for a few days. Consider using a grow light for indoor plants that enjoy full sun."
        actual = weather_info.get_advice_by_weather_type()
        self.assertEqual(expected, actual)

    def test_get_advice_by_weather_unknown_type(self):

        response = {
            "weather":[{"main":"Tornado", "description":"spinning air cone"}],
            "main":{"temp":17, "humidity":60}
        }

        weather_info = WeatherInfo(response)
        expected = "No advice available"
        actual = weather_info.get_advice_by_weather_type()
        self.assertEqual(expected, actual)

class TestDaylightInfo(TestCase):

    def test_calculate_daylight_time(self):
        response = {"sys":{"sunrise": 1661780400, "sunset":1661823600}, "timezone":0}
        daylight_info = DaylightInfo(response)
        expected = datetime.timedelta(seconds = 43200)
        actual = daylight_info.calculate_daylight_time()
        self.assertEqual(expected, actual)

    def test_format_daylight_time(self):
        response = {"sys":{"sunrise": 1661780400, "sunset":1661823600}, "timezone":0}
        daylight_info = DaylightInfo(response)
        expected = "12:00:00"
        actual = daylight_info.format_daylight()
        self.assertEqual(expected, actual)
