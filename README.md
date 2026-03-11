# Smart AI Crop & Fertilizer Recommendation System

An end-to-end Machine Learning web application designed to help farmers make data-driven decisions by combining soil chemistry with real-time environmental data.

---

## Key Features

- **Real-Time Data Integration:** Uses the OpenWeatherMap API to fetch live temperature and humidity based on the user's city, ensuring recommendations are relevant to current conditions.

- **Dual-Model Pipeline:** Implements a two-stage prediction system where the recommended crop (Model A) is used as an input feature for the fertilizer recommendation (Model B).

- **Full-Stack Implementation:** Built with a Python Flask backend and a custom HTML5/CSS3 frontend to demonstrate client-server architecture.

- **Robust Error Handling:** Features custom logic to handle Label Mismatch and Out-of-Vocabulary (OOV) issues between disparate datasets.

---

## Tech Stack

- **Languages:** Python, HTML5, CSS3  
- **Machine Learning:** Scikit-Learn (Random Forest), Pandas, NumPy  
- **Web Framework:** Flask  
- **APIs:** OpenWeatherMap REST API  
- **Tools:** Pickle (Model Serialization), Label Encoding  

---

## How It Works

1. **Input:** User enters Nitrogen (N), Phosphorous (P), Potassium (K), pH, and Moisture levels.

2. **API Call:** The system fetches live weather data for the specified city.

3. **Crop Prediction:** A Random Forest model analyzes soil and weather to suggest the ideal crop.

4. **Fertilizer Prediction:** A secondary model recommends the specific fertilizer needed for that crop-soil combination.

5. **Output:** The UI displays the results instantly with a modern, responsive design.

---

## Model Performance

- **Crop Recommendation Model:** ~99% Accuracy  
- **Fertilizer Recommendation Model:** ~98% Accuracy  

---

## Project Highlights

- Combines **Machine Learning + Web Development + API Integration**
- Demonstrates **end-to-end ML deployment using Flask**
- Uses **real-time environmental data for smarter predictions**
- Built with a **clean and responsive user interface**

---

## Installation & Setup

Note: put your API yourself in app.py

```bash
git clone https://github.com/codebyakshitpunia/Smart-AI-Crop-Fertilizer-Recommendation-System.git
cd Smart-AI-Crop-Fertilizer-Recommendation-System
pip install -r requirements.txt
python app.py
