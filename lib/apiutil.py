import os

__name__ = 'dailyforecast'

host = 'https://api.weather.com'

def default_params():
  return {
    'apiKey': os.environ['WEATHER_API_KEY'],
    'language': 'en-US'
  }

def request_headers():
  return {
    'User-Agent': 'Request-Promise',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip'
  }
