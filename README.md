---

# 🌦️ England Travel Weather App

A web-based application built with **Python and Flask** that retrieves **real-time weather data** for a travel blogger’s itinerary across England. The app integrates with an external weather API to display current conditions for multiple destinations using latitude and longitude.

---

## 📌 Project Overview

This project was developed as part of a coursework assignment to demonstrate:

* API integration in a real-world business scenario
* Use of HTTP requests and JSON data
* Backend and frontend web development using Python and Flask

The application supports a travel website by providing up-to-date weather information that can be used alongside travel blog posts.

---

## 🧭 Itinerary Locations

The application retrieves weather data for the following locations in England:

* Lake District National Park
* Corfe Castle
* The Cotswolds
* Cambridge
* Bristol
* Oxford
* Norwich
* Stonehenge
* Watergate Bay
* Birmingham

Each location is queried using its **latitude and longitude coordinates**.

---

## 🛠️ Technologies Used

* **Python 3**
* **Flask** (web framework)
* **Requests** (HTTP requests)
* **OpenWeatherMap API**
* **HTML & CSS**
* **JSON**

---

## ⚙️ Features

* Retrieves **live weather data** from an external API
* Displays:

  * Temperature (°C)
  * Weather description
  * Humidity
* Clean, card-based web interface
* Easily extendable (e.g. maps, icons, user input)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/england-travel-weather-app.git
cd england-travel-weather-app
```

### 2. Install Dependencies

```bash
pip install flask requests
```

### 3. Get an API Key

* Sign up at **OpenWeatherMap**
* Generate a free API key

### 4. Add Your API Key

In `app.py`, replace:

```python
API_KEY = "YOUR_API_KEY_HERE"
```

---

## ▶️ Running the Application

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 📁 Project Structure

```
.
├── app.py
├── templates
│   └── index.html
├── README.md
```

---

## 🧪 Example API Response (Excerpt)

```json
{
  "main": {
    "temp": 15.2,
    "humidity": 78
  },
  "weather": [
    {
      "description": "overcast clouds"
    }
  ]
}
```

---

## 📈 Future Improvements

* Interactive map (Leaflet.js or Google Maps)
* Weather icons
* User-selected destinations
* Error handling and API response validation
* Caching to reduce API calls

---

## 🧠 Learning Outcomes

Through this project, I gained hands-on experience with:

* API-driven application development
* HTTP communication and JSON parsing
* Flask routing and templating
* Structuring and documenting a Python project
* Connecting backend logic with frontend presentation

---

## 🙌 Acknowledgements

* OpenWeatherMap API
* Flask documentation

---