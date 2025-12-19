# 🌾 Crop Recommendation System (Production-Deployed ML App)

A **production-ready Machine Learning web application** that recommends the most suitable crop based on soil nutrients and regional information. This project goes beyond model training and demonstrates **end-to-end ML system design**, including API development, frontend integration, secure configuration, and cloud deployment.

🔗 **Live Demo**: [https://crop-recommendation-zd7v.onrender.com](https://crop-recommendation-zd7v.onrender.com)
🔗 **GitHub Repository**: [https://github.com/animesh-kh/Crop](https://github.com/animesh-kh/Crop)

---

## 🚀 Why this project matters

Most ML projects stop at Jupyter notebooks. This project focuses on **real-world ML engineering**, showing how a trained model can be served reliably in production.

Key highlights:

* End-to-end ML pipeline (input → preprocessing → model → prediction)
* REST API built with FastAPI
* Secure handling of API keys using environment variables
* Cloud deployment with cold-start considerations
* Clean separation of concerns (models, schemas, utilities)

---

## 🧠 Problem Statement

Farmers often lack easy access to data-driven recommendations for choosing crops based on soil health and regional context. This system takes key soil parameters and location details to recommend a suitable crop, acting as a **decision-support tool** rather than a black-box prediction.

---

## 🛠️ Tech Stack

### Machine Learning

* Scikit-learn
* NumPy, Pandas
* Model serialization with Joblib

### Backend

* FastAPI
* Pydantic (data validation)
* Uvicorn (ASGI server)

### Frontend

* HTML, CSS
* Fetch API for client–server communication

### Deployment & DevOps

* Render (cloud deployment)
* GitHub (version control)
* Environment variables for secrets management

---

## 🧩 Project Architecture

```
User (Browser)
   ↓
Frontend (HTML/CSS)
   ↓  JSON Request
FastAPI Backend
   ↓
Preprocessor (joblib)
   ↓
ML Model (scikit-learn)
   ↓
Prediction Response
```

---

## 📂 Project Structure

```
Crop/
│
├── main.py              # FastAPI app and routes
├── schemas.py           # Pydantic request/response schemas
├── utils.py             # Model loading and helper functions
├── requirements.txt     # Python dependencies
│
├── models/
│   ├── crop_model.pkl
│   └── preprocessor.pkl
│
├── templates/
│   └── index.html       # Frontend UI
│
└── static/
    └── style.css        # Styling
```

---

## ⚙️ How it works

1. User enters soil nutrients (N, P, K, pH) and location details
2. Input is validated using Pydantic schemas
3. Preprocessor transforms raw input into model-ready features
4. Trained ML model generates a crop recommendation
5. Result is returned via API and displayed on the UI

---

## 🔐 Environment Variables

This project uses environment variables for sensitive information.

Example:

```bash
GROQ_API_KEY=your_api_key_here
```



---

## ▶️ Run Locally

```bash
# Clone the repository
git clone https://github.com/animesh-kh/Crop.git
cd Crop

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python main.py
```

Open: `http://localhost:8000`

---

## ☁️ Deployment

The application is deployed on **Render** using:

```bash
uvicorn main:app --host 0.0.0.0 --port 10000
```

On the free tier, the service may **spin down after inactivity** and take ~30–50 seconds to wake up.

---

## 🧪 Example API Request

```json
{
  "state": "Uttar Pradesh",
  "district": "Kanpur",
  "N": 90,
  "P": 42,
  "K": 43,
  "pH": 6.5
}
```

---

## 🎯 Future Improvements

* Return top-3 crop recommendations with confidence scores
* Add model explainability (feature importance)
* Add logging and monitoring
* Containerize using Docker

---

## 🧑‍💻 Author

**Animesh Khare**
B.Tech Computer Science 
