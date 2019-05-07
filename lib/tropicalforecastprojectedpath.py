# Tropical -Forecast - Projected Path
#
# - https://weather.com/swagger-docs/ui/sun/v2/SUNv2TropicalForecastProjectedPathSourceAndBasinOnly.json
#
# The Tropical Forecast - Projected Path API provides the ability query the single
# projected path per active storm. Active storm - any storm that has reported in the
# last 168 hours. One can query by basin or selected source.
#
# Base URL: api.weather.com/v2
# Endpoint: /tropical/projectedpath

__name__ = 'tropicalforecastprojectedpath'

from lib.apiutil import host, default_params

def request_options (basin = 'AL', units = 'm', nautical = True, source = 'all'):
  u = units if units in ['e', 'm', 'h', 's'] else 'm'

  url = host + '/v2/tropical/projectedpath'

  params = default_params()
  params['units'] = u
  params['basin'] = basin
  params['nautical'] = 'true' if nautical else 'false'
  params['source'] = source
  params['format'] = 'json'

  return url, params

def handle_response (res):
  if res and res['advisoryinfo']:
    print('tropical-forecast-projected-path: returned {} advisory info'.format(len(res['advisoryinfo'])))

    for storm in res['advisoryinfo']:
      # the storm's storm_name, projectedpath, and projectedpath.heading objects are probably of interest
      print('tropical-forecast-projected-path: Advisoory for storm "{}" by "{}"'.format(storm['storm_name'], storm['source']))
      print('tropical-forecast-projected-path: {} - {}'.format(storm['storm_name'], storm['projectedpath']))
  else:
    print('tropical-forecast-projected-path: No advisory info available')

