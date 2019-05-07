# Severe Weather Power Disruption Index 15 Day
#
# - https://weather.com/swagger-docs/ui/sun/v2/SUNv2SevereWeatherPowerDisruptionIndex.json
#
# The Power Disruption index provides indices indicating the potential for power
# disruptions due to weather.
#
# Base URL: api.weather.com/v2
# Endpoint: /indices/powerDisruption/daypart/15day

__name__ = 'severeweatherpowerdisruptionindex'

from lib.apiutil import host, default_params

def request_options (lat, lon):
  url = host + '/v2/indices/powerDisruption/daypart/15day'
  
  params = default_params()
  params['geocode'] = '{lat},{lon}'.format(lat=lat, lon=lon)
  params['format'] = 'json'

  return url, params

def handle_response (res):
  if res and res['powerDisruptionIndex12hour']:
    p = res['powerDisruptionIndex12hour']
    for i, disruptIndex in enumerate(p['powerDisruptionIndex']):
      print('severe-weather-power-disruption-index: {}: {}'.format(disruptIndex, p['powerDisruptionCategory'][i]))
  else:
    print('severe-weather-power-disruption-index: no power distruption info returned')
