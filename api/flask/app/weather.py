import requests
from flask import request
from requests.models import parse_header_links
from app import app
from app.config import OW_URL, OW_KEY


@app.route('/api/weather', methods=['GET'])
def get_weather_now():
    """API endpoint for fetching weather data from given city.

    City can be passed in the qurey params in two different ways:
    - city    - name of the city
    - city_id - city ID from the openweathermap list
    
    Return: data JSON containing flag providing information if
    the request was successful and informations about the weather 
    in given city if request was successfu, empty dictionary otherwise.

    Example successful response:
    {
        success: True,
        weather: { 
            some info about weather...
        }
    }

    Example unsuccessful respose:
    {
        success: False,
        weather: {}
    }
    """
    QUERY_PARAMS = {
        'city': 'q',
        'city_id': 'id',
    }
    units = request.args.get('units', default='metric')

    search_type = request.args.get('search', 'city')
    param_value = request.args.get(search_type)

    params = {
        QUERY_PARAMS[search_type]: param_value,
        'units': units,
        'appid': OW_KEY
    }

    REQUEST_URL = f'{OW_URL}/weather'

    ow_response = requests.get(REQUEST_URL, params=params)

    data = {
        'success': ow_response.status_code == 200,
        'weather': {}
    }

    if ow_response.status_code == 200:
        data['weather'] = ow_response.json()

    return data
