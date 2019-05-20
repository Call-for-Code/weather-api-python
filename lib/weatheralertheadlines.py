# Weather Alerts - Headlines
#
# - https://weather.com/swagger-docs/ui/sun/v1/sunV1AlertsWeatherAlertHeadlines.json
#
# The Weather Alert Headlines API provides weather watches, warnings, statements and
# advisories issued by the NWS (National Weather Service), Environment Canada and
# MeteoAlarm. These weather alerts can provide crucial life-saving information.
# Weather alerts can be complicated and do not always follow consistent standards,
# format and rules. The Weather Channel (TWC) strives to ensure that the information
# is consistent from all of the different sources but the content is subject to
# change whenever there is an update from the authoritative source.
#
# The Weather Alert Headline API returns active weather alert headlines related to
# Severe Thunderstorms, Tornadoes, Earthquakes, Floods, etc . This API also returns
# non-weather alerts such as Child Abduction Emergency and Law Enforcement Warnings.
# The Alert Headlines API also provides a key value found in the attribute to access
# the alert details in the Alert Details API.
#
# Base URL: api.weather.com/v1
# Endpoint: /geocode/{latitude}/{longitude}/alerts.json

__name__ = 'weatheralertheadlines'

from lib.apiutil import host, default_params

def request_options (lat, lon):
  url = host + '/v1/geocode/{lat}/{lon}/alerts.json'.format(lat=lat, lon=lon)

  params = default_params()

  return url, params

def handle_response (res):
  details = []

  if res and res['alerts']:
    # loop through alerts
    for alert in res['alerts']:
      # check fields to decide if this alert is important to you.
      print(alert)

      if alert['severity_cd'] <= 3 and alert['certainty_cd'] <= 3 and alert['urgency_cd'] <= 3:
        details.append(alert['detail_key'])

    print('weather-alert-headlines: returning {} alert(s) meeting threshold out of {} total'.format(len(details), len(res['alerts'])))
  else:
    print('weather-alert-headlines: No alerts in area')

  # return the detail_key(s) for alerts you deemed important
  return details
