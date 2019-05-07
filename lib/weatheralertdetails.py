# Weather Alert - Details
#
# - https://weather.com/swagger-docs/ui/sun/v1/sunV1AlertsWeatherAlertDetails.json
#
# The Weather Alert Details API provides weather watches, warnings, statements and
# advisories issued by the NWS (National Weather Service), Environment Canada and
# MeteoAlarm. These weather alerts can provide crucial life-saving information.
# Weather alerts can be complicated and do not always follow consistent standards,
# format and rules. The Weather Channel (TWC) strives to ensure that the information
# is consistent from all of the different sources but the content is subject to
# change whenever there is an update from the authoritative source. The Weather Alert
# Headlines API returns active weather alert headlines related to Severe
# Thunderstorms, Tornadoes, Earthquakes, Floods, etc . This API also returns
# non-weather alerts such as Child Abduction Emergency and Law Enforcement Warnings.
# The Alert Headlines API also provides a key value found in the attribute to access
# the alert details in the Alert Details API. Your application should first call the
# Weather Alert Headlines API and use the value found in the attribute to request the
# detailed information found in the Weather Alert Details API.
#
# Base URL: api.weather.com/v1
# Endpoint: /alert/{detailKey}/details.json

__name__ = 'weatheralertdetails'

from lib.apiutil import host, default_params

def request_options (detail_key):
  url = host + '/v1/alert/{key}/details.json'.format(key=detail_key)

  params = default_params()

  return url, params

def handle_response (res):
  if res and res['alertDetail']:
    alert = res['alertDetail']
    # Main thing here that is not in the alert headline is the alert['texts'] array
    print('weather-alerts-detail: {}'.format(alert['headline_text']))

    if alert['texts']:
      for text in alert['texts']:
        print(text['language_cd'])
        print(text['instruction'])
        print(text['overview'])
        print(text['description'])
    else:
      print('weather-alerts-detail: No alert text available')
  else:
    print('weather-alerts-detail: No alert detail available')
