from geopy.geocoders import Bing
import os

def set_proxy():
    proxy_addr = 'http://{user}:{passwd}@{address}:{port}'.format(
        user='USER', passwd='SENHA', 
        address='PROXY', port=int('8080'))
    os.environ['http_proxy'] = proxy_addr
    os.environ['https_proxy'] = proxy_addr

def unset_proxy():
    os.environ.pop('http_proxy')
    os.environ.pop('https_proxy')

set_proxy()


geolocator = Bing('CHAVE BING')
end = {
        'addressLine': 'RUA XYZ NUMERO', 
        'locality': 'Porto Alegre', 
        'countryRegion' : 'Rio Grande Do Sul', 
        'adminDistrict': 'Cristal'
    }
location = geolocator.geocode(end,exactly_one=True, user_location=None, culture='BR', include_neighborhood=None, include_country_code=False)

print('latitude:', location.raw)