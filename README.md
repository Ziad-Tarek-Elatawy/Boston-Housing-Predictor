# BOSTON HOUSING PREDICTION

An end-to-end Machine Learning web application deployed with **FastAPI**. This system predicts housing prices in Boston based on a subset of features using an optimized Decision Tree Regressor.

---

## 🏗️ Project Architecture & Structure

The repository is structured to cleanly separate Machine Learning Training from Production Application Serving.

```text
Boston Housing Prices/
├── data/                   # Raw Dataset
│   └── housing.csv
├── notebooks/              # Jupyter Environment & Model Training
│   ├── boston_housing.ipynb # The completed ML training notebook
│   └── visuals.py          # Helper functions for notebook visual plots
├── app/                    # Production-Ready FastAPI Deployment
│   ├── main.py             # FastAPI backend API routes and logic
│   ├── model.pkl           # The serialized optimized ML model
│   ├── templates/          # Jinja2 HTML templates
│   │   └── index.html      # The frontend UI
│   └── static/             # Static web assets
│       └── style.css       # Dynamic glassmorphism styling
├── requirements.txt        # Python dependencies for the entire project
└── README.md               # End-to-end documentation (this file)
```

---

## 🚀 Installation & Setup

1. **Clone the repository** (or navigate to the project directory):
   ```bash
   cd \"Boston Housing Prices\"
   ```

2. **Install all necessary Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *(Ensure you use a virtual environment `venv` if preferred).*

---

## 🧠 Phase 1: Model Training & Evaluation

All Research, Exploratory Data Analysis (EDA), and Model Optimization occurred logically within the Jupyter environment.

1. Navigate to the notebooks directory:
   ```bash
   cd notebooks
   ```
2. Launch Jupyter Notebook to review the answered questions, learning curves, and model complexity graphs:
   ```bash
   jupyter notebook boston_housing.ipynb
   ```
3. *Note: The optimal model (`DecisionTreeRegressor` with `max_depth` tuned) was previously serialized and saved as `app/model.pkl` for production use.*

---

## 🌐 Phase 2: Web Application (End-to-End)

The backend exposes a highly performant and asynchronous REST API serving a dynamic web frontend utilizing the trained `.pkl` model.

1. **Spin up the FastAPI server**:
   Navigate to the root directory `Boston Housing Prices` and run:
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Access the Web Interface**:
   Open a modern web browser and go to:
   👉 **http://127.0.0.1:8000**

3. **Make a Prediction**:
   - Provide the **Number of Rooms (RM)**.
   - Provide the **Neighborhood Poverty Level (LSTAT)** (%).
   - Provide the **Student-Teacher Ratio (PTRATIO)**.
   - Click **Predict Price** to ping the endpoint and receive an accurate housing valuation.
