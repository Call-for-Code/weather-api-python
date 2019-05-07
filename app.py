import os, requests, time, schedule

import lib.weatheralertheadlines as alert_headlines
import lib.weatheralertdetails as alert_details
import lib.dailyforecast as daily_forecast
import lib.tropicalforecastprojectedpath as tropical_forecast
import lib.severeweatherpowerdisruptionindex as power_disruption

from lib.apiutil import request_headers

def handleFail(err):
  # API call failed...
  print('Status code: %d' % (err.status_code) )

def callWeatherAlertHeadlines(lat, lon):
  url, params = alert_headlines.request_options(lat, lon)
  headers = request_headers()

  r = requests.get(url, params=params, headers=headers)
  if r.status_code == 200:
    detailKeys = alert_headlines.handle_response(r.json())
    if detailKeys and len(detailKeys) > 0:
      for detailKey in detailKeys:
        print('Detail key: '+detailKey)
        callWeatherAlertDetails(detailKey)
  else:
    handleFail(r)

def callWeatherAlertDetails(detailKey):
  url, params = alert_details.request_options(detailKey)
  headers = request_headers()

  r = requests.get(url, params=params, headers=headers)
  if r.status_code == 200:
    alert_details.handle_response(r.json())
  else:
    handleFail(r)

def callTropicalForecastProjectedPath(basin='AL', units='m', nautical=True, source='all'):
  url, params = tropical_forecast.request_options(basin, units, nautical, source)
  headers = request_headers()

  r = requests.get(url, params=params, headers=headers)
  if r.status_code == 200:
    tropical_forecast.handle_response(r.json())
  else:
    handleFail(r)

def callDailyForecast(lat, lon, units = 'm'):
  url, params = daily_forecast.request_options(lat, lon)
  headers = request_headers()

  r = requests.get(url, params=params, headers=headers)
  if r.status_code == 200:
    daily_forecast.handle_response(r.json())
  else:
    handleFail(r)

def callSevereWeatherPowerDisruption(lat, lon):
  url, params = power_disruption.request_options(lat, lon)
  headers =request_headers()

  r = requests.get(url, params=params, headers=headers)
  if r.status_code == 200:
    power_disruption.handle_response(r.json())
  else:
    handleFail(r)


loc = {
  'boston': { 'lat': '42.3600', 'lon': '-71.06536' }, # Boston, MA, United States
  'raleigh': { 'lat': '35.843686', 'lon': '-78.78548' }, # Raleigh, NC, United States
  'losangeles': { 'lat': '34.040873', 'lon': '-118.482745' }, # Los Angeles, CA, United States
  'lakecity': { 'lat': '44.4494119', 'lon': '-92.2668435' }, # Lake CIty, MN, United States
  'newyork': { 'lat': '40.742089', 'lon': '-73.987908' }, # New York, NY, United States
  'hawaii': { 'lat': '33.40', 'lon': '-83.42' }, # Hawaii, United States
  'puntacana': { 'lat': '18.57001', 'lon': '-68.36907' }, # Punta Cana, Dominican Republic
  'jakarta': { 'lat': '-5.7759349', 'lon': '106.1161341' } # Jakarta, Indonesia
}


########################
# Make a single API call
########################

callDailyForecast(loc['raleigh']['lat'], loc['raleigh']['lon'])
# callWeatherAlertHeadlines(loc['lakecity']['lat'], loc['lakecity']['lon'])
# callSevereWeatherPowerDisruption(loc['jakarta']['lat'], loc['jakarta']['lon'])
# callTropicalForecastProjectedPath()
# callWeatherAlertDetails('06439e88-320a-3722-ae90-097484ff2277')


########################
# Setting up a job to look for weather alert headlines every 10 minutes
########################

def job():
  callWeatherAlertHeadlines(loc['lakecity']['lat'], loc['lakecity']['lon'])

schedule.every(10).minutes.do(job)

while True:
  schedule.run_pending()
  time.sleep(100)
