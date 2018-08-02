# from: https://callforcode.weather.com/doc/v3-weather-alerts-detail/
# 
# Weather Alerts Detail (v3) - The Weather Alert Details API provides
# the details for a single requested event for weather watches,
# warnings, statements and advisories issued by the NWS (National
# Weather Service), Environment Canada and MeteoAlarm. These weather
# alerts can provide crucial life-saving information. Weather alerts
# can be complicated and do not always follow consistent standards,
# format and rules. The Weather Company (TWC) strives to ensure tha
#  the information is consistent from all of the different sources but
# the content is subject to change whenever there is an update from
# the authoritative source.
# 
# The Weather Alert Details API returns additional details related to
# Severe Thunderstorms, Tornadoes, Earthquakes, Floods, etc . This API
# also returns non-weather alerts such as Child Abduction Emergency
# and Law Enforcement Warnings.
__name__ = 'weatheralertsdetail'

API = '/v3/alerts/detail'

def handleResponse(res):
  if res and res['alertDetail']:
    alert = res['alertDetail']
    # Main thing here that is not in the alert headline is the alert['texts'] array
    print( 'weather-alerts-detail: ' + alert['headlineText'] )

    if alert['texts']:
      for text in alert['texts']:
        print(text['languageCode'])
        print(text['instruction'])
        print(text['overview'])
        print(text['description'])
    else:
      print('weather-alerts-detail: No alert text available')

  else:
    print('weather-alerts-detail: No alert detail available')
