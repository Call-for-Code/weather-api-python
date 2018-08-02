# from: https://callforcode.weather.com/doc/v2-tropical-forecast-projected-path-source-and-basin-only/
#
# Tropical -Forecast - Projected Path (v2) - The Tropical Forecast -
# Projected Path API provides the ability query the single projected
# path per active storm. Active storm - any storm that has reported in
# the last 168 hours. One can query by basin or selected source.

__name__ = 'tropicalforecastprojectedpath'

API = '/v2/tropical/projectedpath'
msgheader = 'tropical-forecast-projected-path-source-and-basin-only'

def handleResponse(res):
  if res and res['advisoryinfo']:
    print( '%s: returned %d advisory(s)' % (msgheader, len(res['advisoryinfo'])) )

    for storm in res['advisoryinfo']:
      # the storm's storm_name, projectedpath, and projectedpath.heading objects are probably of interest
      print('')
      print( '%s: %s' % (msgheader, storm['storm_name']) )
      for i,path in enumerate(storm['projectedpath']):
        print( '%s: Path: %d' % (msgheader, i) )
        print( '%s: Type: %s' % (msgheader, path['storm_type']) )
        print( '%s: Direction: %s%s' % (msgheader, path['heading']['storm_dir'],path['heading']['storm_dir_cardinal']) )
        print( '%s: Speed: %d' % (msgheader, path['heading']['storm_spd']) )
  else:
    print('%s: No index available')
