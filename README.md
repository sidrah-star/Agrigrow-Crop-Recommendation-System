# 🌾 Crop Recommendation System

This is a Machine Learning-based web application that recommends the most suitable crop to cultivate based on environmental conditions such as nitrogen, phosphorus, potassium levels in the soil, temperature, humidity, pH, and rainfall.

🔗 **GitHub Repository**: [Crop Recommendation System](https://github.com/Ishant-Bansal/Crop-Recomandation_System.git)

---

## 📌 Features

- Predicts the best crop to grow based on environmental data 🌱
- Easy-to-use frontend with form inputs for various parameters 🖥️
- Backend built using Python & Flask 🐍
- Trained using a real-world agricultural dataset 📊

---

## 🚀 Technologies Used

| Component   | Technology          |
|-------------|----------------------|
| Frontend    | HTML, CSS, JavaScript |
| Backend     | Python (Flask)        |
| Model       | Scikit-learn (RandomForestClassifier) |
| Dataset     | Kaggle/NITI Aayog or similar sources |
| Deployment  | (Optional: can be added here if deployed) |

---

## 📁 Project Structure

```
Crop-Recomandation_System/
├── static/
│   ├── images
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   └── result.html
├── crop_recommendation_model.pkl
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ishant-Bansal/Crop-Recomandation_System.git
   cd Crop-Recomandation_System
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://127.0.0.1:5000/
   ```

---

## 🧠 Machine Learning Model

- Algorithm: Random Forest Classifier
- Accuracy: ~98% on test data
- Input Features:
  - Nitrogen (N)
  - Phosphorus (P)
  - Potassium (K)
  - Temperature
  - Humidity
  - pH
  - Rainfall
- Output: Recommended Crop 🌿

---

## 📸 Screenshots

<img width="1920" height="1485" alt="image" src="https://github.com/user-attachments/assets/128cc9ed-5875-4125-b65a-9290602032c0" />

---

## 👨‍💻 Author

- **Ishant Bansal**
- GitHub: [@Ishant-Bansal](https://github.com/Ishant-Bansal)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 📞 Contact

For questions or feedback, feel free to reach out via GitHub or email.


