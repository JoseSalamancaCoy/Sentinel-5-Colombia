from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date

api = SentinelAPI(user='s5pguest', password='s5pguest', api_url='https://s5phub.copernicus.eu/dhus')
footprint =  geojson_to_wkt(read_geojson('~/Dropbox/daniel/sentinel_5_colombia/maps/colombia_area.geojson'))
products = api.query(area = footprint, date = "[20191231 TO NOW]", platformname='Sentinel-5p')

# downloading products
api.download_all(products, directory_path="~/Dropbox/daniel/sentinel_5_colombia/products/202001_20200313")
