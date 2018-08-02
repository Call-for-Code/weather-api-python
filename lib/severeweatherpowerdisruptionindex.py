# from: https://callforcode.weather.com/doc/v2-severe-weather-power-disruption-index/
#
# Severe Weather Power Disruption Index 15 Day (v2) - The Power
# Disruption index provides indices indicating the potential for
# power disruptions due to weather.

__name__ = 'severeweatherpowerdisruptionindex'

API = '/v2/indices/powerDisruption/daypart/15day'

def handleResponse(res):
  if res and res['powerDisruptionIndex12hour']:
    p = res['powerDisruptionIndex12hour']
    for i, disruptIndex in enumerate(p['powerDisruptionIndex']):
      print('severe-weather-power-disruption-index: %s: %s' % (disruptIndex, p['powerDisruptionCategory'][i]))
  else:
    print('severe-weather-power-disruption-index: no power distruption info returned')
