from app import app
from app.weather import get_weather_now

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)