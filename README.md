## End to end Machine Learning Project
## 📘 Student Exam Performance Predictor

This is a complete **end-to-end machine learning project** built using Python. The project predicts a student's **math score** based on attributes like gender, ethnicity, parental education, lunch type, and test preparation. It includes model training, data transformation, deployment with Flask, and a web UI.

---

### 🔧 Tech Stack

* **Language**: Python 3.8
* **Libraries**: pandas, numpy, scikit-learn, dill, xgboost, catboost, Flask
* **Frontend**: HTML + Bootstrap
* **Logging**: Python logging module
* **ML Workflow**: Manual pipeline with modular scripts

---

### 📁 Project Structure

```
ML_Project/
├── app.py                  # Flask app entry point
├── templates/
│   └── index.html          # Web interface for user input
├── artifacts/
│   ├── train.csv           # Training dataset
│   ├── test.csv            # Testing dataset
│   └── preprocessor.pkl    # Serialized preprocessing object
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── utils.py            # Utility for saving pickle files
│   ├── logger.py           # Logger setup
│   └── exception.py        # Custom exception class
├── requirements.txt        # List of required packages
└── pyproject.toml or setup.py   # Packaging (optional)
```

---

### 🚀 How to Run

#### 1. Clone the Repo

```bash
git clone https://github.com/your-username/ML_Project.git
cd ML_Project
```

#### 2. Create & Activate Environment

```bash
conda create -n ml_env python=3.8 -y
conda activate ml_env
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Run the Project

```bash
python app.py
```

Then open your browser and go to:
📍 `http://127.0.0.1:5000/` or `http://localhost:5000/`

---

### 🧐 How It Works

* **Data Ingestion**: Reads raw CSV file and splits into train/test.
* **Data Transformation**: Preprocessing with pipelines (imputing, encoding, scaling).
* **Model Training**: Trains models and saves best one.
* **Web Interface**: HTML form lets users enter new data and get predictions.

---

### ✅ Features

* Clean modular code
* Logging & error handling
* HTML form interface
* Easily extendable with new models

---

### 📌 Future Improvements

* Add unit testing (pytest)
* Store configs in YAML/.env
* Use MLflow for model tracking
* Dockerize the app for production

---

### 🙇‍♂️ Author

**Manoj Kumar**
*Data enthusiast with a passion for machine learning and data pipelines.*
