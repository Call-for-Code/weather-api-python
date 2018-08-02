# from: https://callforcode.weather.com/doc/v3-daily-forecast/
# 
# Daily Forecast (v3) - The Daily Forecast API is sourced from the
# The Weather Company Forecast system. This TWC API returns weather
# forecasts starting current day. Your content licensing agreement
# with TWC determines the number of days returned in the API response
# and is constrained by the API Key that is provided to your company.
# Please refer to the Data Elements section later in this document for
# more details.

__name__ = 'dailyforecast'

# API = /v3/wx/forecast/daily/{days}day
# API = '/v3/wx/forecast/daily/10day'
# API = '/v3/wx/forecast/daily/7day'
# API = '/v3/wx/forecast/daily/5day'
API = '/v3/wx/forecast/daily/3day'

def handleResponse(res):
  if res and res['dayOfWeek']:
    days = res['dayOfWeek']
    print('daily-forecast: returned %d-day forecast' % (len(days)))

    # each entry in the response object is an array with
    # entries in the array applying to the day of the week
    # (i.e., res['dayOfWeek']) matched by the index
    for index, day in enumerate(days):
      maxtemp = str(res['temperatureMax'][index]) if res['temperatureMax'][index] else 'n/a'
      mintemp = str(res['temperatureMin'][index]) if res['temperatureMin'][index] else 'n/a'
      print ('daily-forecast: %s - High of %s, Low of %s' % (day, maxtemp, mintemp) )
      print ('daily-forecast: %s - %s' % (day, res['narrative'][index]) )

    # additional entries include (but not limited to):
    # moonPhase, sunriseTimeLocal, daypart['precipChance'], daypart['windDirection'], etc
  else:
    print('daily-forecast: daily forecast returned')
