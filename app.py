import os
from flask import Flask, render_template
import requests
from datetime import datetime
import pdfkit

app = Flask(__name__)

#API_KEY = os.environ.get ("OWM_API_KEY")
API_KEY = "00c687ee7093ec9ed2f6586d340f74ba"  # <-- your actual API key here
if not API_KEY:
    raise RuntimeError ("Set the OWM API_KET first.")

locations = {
    "Lake District National Park": (54.4609, -3.0886),
    "Corfe Castle": (50.6395, -2.0566),
    "The Cotswolds": (51.8330, -1.8433),
    "Cambridge": (52.2053, 0.1218),
    "Bristol": (51.4545, -2.5879),
    "Oxford": (51.7520, -1.2577),
    "Norwich": (52.6309, 1.2974),
    "Stonehenge": (51.1789, -1.8262),
    "Watergate Bay": (50.4429, -5.0553),
    "Birmingham": (52.4862, -1.8904)
}

def get_weather(lat, lon):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"lat": lat, "lon": lon, "appid": API_KEY, "units": "metric"}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()

@app.route("/")
def index():
    weather_data = []
    for name, (lat, lon) in locations.items():
        try:
            data = get_weather(lat,lon)
            weather_data.append({
                "location": name,
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"].title(),
                "humidity": data["main"]["humidity"],
                "lat": lat,
                "lon":lon               
                
            })
        except Exception as e:
            weather_data.append({
                "location": name,
                "temperature": "_",
                "description":  f"Error: {e}",
                "humidity": "_",
                "lat": lat,
                "lon":lon
            })

    generated_at = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    return render_template("index.html", weather=weather_data, generated_at=generated_at)

if __name__ == "__main__":
    app.run(debug=True)
    
@app.route("/download_pdf")
def download_pdf():
    path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_url("http://127.0.0.1:5000/", "weather_report.pdf", configuration=config)
    return send_file("weather_report.pdf", as_attachment=True)


print("API_KEY:", API_KEY)
API_KEY = os.environ.get("OWM_API_KEY")