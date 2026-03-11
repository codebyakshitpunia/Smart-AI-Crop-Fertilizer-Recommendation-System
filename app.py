from flask import Flask, request, render_template
import pickle
import numpy as np
import requests

# Initialize the Flask App
app = Flask(__name__)

# 1. Load your trained models
crop_model = pickle.load(open('crop_model.pkl', 'rb'))
fert_model = pickle.load(open('fertilizer_model.pkl', 'rb'))
soil_encoder = pickle.load(open('soil_encoder.pkl', 'rb'))
crop_encoder = pickle.load(open('crop_encoder.pkl', 'rb'))
fert_encoder = pickle.load(open('fert_encoder.pkl', 'rb'))

# Weather fetching function
def get_live_weather(city_name):
    api_key = "-----------------" # Put your OpenWeatherMap key here
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'q': city_name, 'appid': api_key, 'units': 'metric'}
    
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data['main']['temp'], data['main']['humidity']
    return None, None

# 2. Route for the Home Page (displays the HTML form)
@app.route('/')
def home():
    return render_template('index.html')

# 3. Route for processing the form when the user clicks Submit
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Grab the data typed into the HTML form
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        pH = float(request.form['ph'])
        moisture = float(request.form['moisture'])
        soil_type_text = request.form['soil_type']
        city = request.form['city']
        
        # Get live weather
        temp, humidity = get_live_weather(city)
        
        if temp is None:
            return render_template('index.html', prediction_text=f"Error: Could not find weather for {city}.")

        # Predict Crop
        crop_features = np.array([[N, P, K, temp, humidity, pH, 100.0]])
        predicted_crop = crop_model.predict(crop_features)[0]
        
        # Predict Fertilizer
        soil_num = soil_encoder.transform([soil_type_text])[0]
        crop_num = crop_encoder.transform([predicted_crop])[0]
        fert_features = np.array([[temp, humidity, moisture, soil_num, crop_num, N, K, P]])
        predicted_fert_num = fert_model.predict(fert_features)[0]
        predicted_fert_name = fert_encoder.inverse_transform([predicted_fert_num])[0]
        
        # Create the final message to send back to HTML
        final_message = f"""
        <b>Weather in {city}:</b> {temp}°C, {humidity}% humidity<br><br>
        🌱 <b>Recommended Crop:</b> {predicted_crop.upper()}<br>
        🧪 <b>Recommended Fertilizer:</b> {predicted_fert_name.upper()}
        """
        
        # Send the user back to the page, but inject the answer into {{ prediction_text }}
        return render_template('index.html', prediction_text=final_message)

# Run the local server
if __name__ == "__main__":

    app.run(debug=True)
