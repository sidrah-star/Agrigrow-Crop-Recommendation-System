import pandas as pd
import joblib
from flask import Flask, render_template, request, url_for

app = Flask(__name__)
model = joblib.load('farmer_model.joblib')

search_history = []

label_map = {
    1: 'rice',
    2: 'maize',
    3: 'chickpea',
    4: 'kidneybeans',
    5: 'pigeonpeas',
    6: 'mothbeans',
    7: 'mungbean',
    8: 'blackgram',
    9: 'lentil',
    10: 'pomegranate',
    11: 'banana',
    12: 'mango',
    13: 'grapes',
    14: 'watermelon',
    15: 'muskmelon',
    16: 'apple',
    17: 'orange',
    18: 'papaya',
    19: 'coconut',
    20: 'cotton',
    21: 'jute',
    22: 'coffee'
}

# Map crop names to image filenames (add your own images in static/images/)
crop_images = {
    'rice': 'rice.jpg',
    'maize': 'maize.jpg',
    'chickpea': 'chickpea.jpg',
    'kidneybeans': 'kidneybeans.jpg',
    'pigeonpeas': 'pigeonpeas.jpg',
    'mothbeans': 'mothbeans.jpg',
    'mungbean': 'mungbean.jpg',
    'blackgram': 'blackgram.jpg',
    'lentil': 'lentil.jpg',
    'pomegranate': 'pomegranate.jpg',
    'banana': 'banana.jpg',
    'mango': 'mango.jpg',
    'grapes': 'grapes.jpg',
    'watermelon': 'watermelon.jpg',
    'muskmelon': 'muskmelon.jpg',
    'apple': 'apple.jpg',
    'orange': 'orange.jpg',
    'papaya': 'papaya.jpg',
    'coconut': 'coconut.jpg',
    'cotton': 'cotton.jpg',
    'jute': 'jute.jpg',
    'coffee': 'coffee.jpg',
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/project', methods=['GET', 'POST'])
def project():
    if request.method == 'POST':
        n = float(request.form.get('nitrogen', 0.0))
        p = float(request.form.get('phosphorus', 0.0))
        k = float(request.form.get('potassium', 0.0))
        temp = float(request.form.get('temperature', 0.0))
        humidity = float(request.form.get('humidity', 0.0))
        ph = float(request.form.get('ph', 0.0))
        rainfall = float(request.form.get('rainfall', 0.0))
        data = [[n, p, k, temp, humidity, ph, rainfall]]
        prediction = model.predict(data)[0]
        predicted_crop = label_map.get(int(prediction), f"Unknown ({prediction})")
        crop_image_file = crop_images.get(predicted_crop, 'default_crop.jpg')
        crop_image_url = url_for('static', filename=f'images/{crop_image_file}')
        return render_template(
            'result.html',
            crop_name=predicted_crop,
            crop_image=crop_image_url,
            details={
                'soil_type': 'Sandy Loam', # Assuming a default value for soil_type
                'ph': ph,
                'temperature': temp,
                # aur bhi jo details chahiye
            }
        )
    else:
        return render_template('project.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
        