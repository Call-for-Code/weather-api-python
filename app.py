import os, requests, time, schedule
import lib.globalweathernotificationheadlines
import lib.weatheralertsdetail
import lib.dailyforecast
import lib.tropicalforecastprojectedpath
import lib.severeweatherpowerdisruptionindex

HOST = 'https://api.weather.com'

defaultParams = {
  'qs': {
    'apiKey': os.environ['WEATHER_API_KEY'],
    'format': 'json',
    'language': 'en-US'
  },
  'headers': {
    'User-Agent': 'Request-Promise',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip'
  },
  'json': True # parse the response as JSON
}

def handleFail(err):
  # API call failed...
  print('Status code: %d' % (err.status_code) )

def callGlobalWeatherNotificationHeadlines(lat, lon):
  url = HOST + lib.globalweathernotificationheadlines.API
  options = defaultParams
  options['qs']['geocode'] = ( '%f,%f' % (lat, lon) )

  r = requests.get( url, params=options['qs'], headers=options['headers'] )
  if r.status_code == 200:
    detailKeys = lib.globalweathernotificationheadlines.handleResponse( r.json() )
    if detailKeys and len(detailKeys) > 0:
      for detailKey in detailKeys:
        print('Detail key: '+detailKey)
        callWeatherAlertsDetail(detailKey)
  else:
    handleFail(r)

def callWeatherAlertsDetail(detailKey):
  url = HOST + lib.weatheralertsdetail.API
  options = defaultParams
  options['qs']['alertId'] = detailKey

  r = requests.get( url, params=options['qs'], headers=options['headers'] )
  if r.status_code == 200:
    lib.weatheralertsdetail.handleResponse( r.json() )
  else:
    handleFail(r)

def callTropicalForecastProjectedPath(basin='AL', units='m', nautical='true', source='all'):
  url = HOST + lib.tropicalforecastprojectedpath.API
  options = defaultParams
  options['qs']['units'] = units
  options['qs']['basin'] = basin
  options['qs']['nautical'] = nautical
  options['qs']['source'] = source

  r = requests.get( url, params=options['qs'], headers=options['headers'] )
  print(r.url)
  if r.status_code == 200:
    lib.tropicalforecastprojectedpath.handleResponse( r.json() )
  else:
    handleFail(r)

def callDailyForecast(lat, lon, units = 'm'):
  url = HOST + lib.dailyforecast.API
  options = defaultParams
  options['qs']['geocode'] = ( '%f,%f' % (lat, lon) )
  options['qs']['units'] = units

  r = requests.get( url, params=options['qs'], headers=options['headers'] )
  if r.status_code == 200:
    lib.dailyforecast.handleResponse( r.json() )
  else:
    handleFail(r)

def callSevereWeatherPowerDisruption(lat, lon):
  url = HOST + lib.severeweatherpowerdisruptionindex.API
  options = defaultParams
  options['qs']['geocode'] = ( '%f,%f' % (lat, lon) )

  r = requests.get( url, params=options['qs'], headers=options['headers'] )
  if r.status_code == 200:
    lib.severeweatherpowerdisruptionindex.handleResponse( r.json() )
  else:
    handleFail(r)

# Comment out the sample lat/lons you don't want to use or put in your own
# Hawaii
lat = 33.40
lon = -83.42
# Punta Cana, DR
# lat = 18.57001
# lon = -68.36907
# # Boston, MA
# lat = 42.3600
# lon = -71.06536
# # Raleigh, NC
# lat = 35.843686
# lon = -78.78548
# # Los Angeles, CA
# lat = 34.040873
# lon = -118.482745
# # New York, NY
# lat = 40.742089
# lon = -73.987908
# # Jakarta, IN
# lat = -5.7759349
# lon = 106.1161341

# Here's an example of setting up a job to look for weather
# headlines every 10 minutes. You can set up as many of these
# jobs as you like and query different geographies.
def job():
  callGlobalWeatherNotificationHeadlines(lat, lon)

schedule.every(10).minutes.do( job )
while True:
  schedule.run_pending()
  time.sleep(100)
# callGlobalWeatherNotificationHeadlines(lat, lon)
# callDailyForecast(lat, lon)
# callSevereWeatherPowerDisruption(lat, lon)
# callTropicalForecastProjectedPath(basin='EP')