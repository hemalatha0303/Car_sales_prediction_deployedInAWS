<div align="center">

<img src="./assets/logo.jpg" alt="Project Logo" width="200">

# 🚗 Car Purchase Amount Prediction AI  예측

**A machine learning-powered web application that predicts the potential purchase amount of a car based on customer data using a Linear Regression model.**

<p>
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/Deployed%20on-AWS-orange?style=for-the-badge&logo=amazon-aws" alt="AWS">
</p>

</div>

---

## 🌟 Project Overview & Screenshots

This project tackles the problem of predicting how much a customer is likely to spend on a car. It uses a customer's age, gender, annual salary, and credit card debt to train a Linear Regression model. The final model is deployed as a web application using Flask, containerized with Docker, and hosted on an AWS EC2 instance.

### Web Application Interface
*This is the main page where users can input customer data.*
<div align="center">
  <img src="./assets/page1.png" alt="Application User Interface" width="80%">
</div>

### Prediction Results
*After submitting the data, the application shows the predicted purchase amount.*
<div align="center">
  <img src="./assets/page3.png" alt="Prediction Output Example" width="80%">
</div>

---

## ✨ Core Features

* **User-Friendly Web Form:** An intuitive interface for inputting customer details.
* **Real-Time Prediction:** The backend Flask server provides instant predictions using the trained model.
* **Containerized & Portable:** The entire application is packaged in a Docker container for easy deployment.
* **Cloud-Ready:** Deployed on an AWS EC2 instance for public accessibility.
* **Data-Driven Model:** The model is trained on a real-world dataset of customer financial data.

---

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| **Backend** | Python, Flask |
| **Machine Learning** | Scikit-learn, Pandas, NumPy |
| **Frontend**| HTML, CSS (as part of the Flask template) |
| **Containerization** | Docker |
| **Cloud Deployment** | AWS EC2 |

---

## 🤖 Machine Learning Workflow

The model was developed and trained in the `model.ipynb` Jupyter Notebook.

1.  **Data Loading & Exploration:** The `customer_data_linear_regression.csv` dataset was loaded into a Pandas DataFrame. Initial analysis was performed to understand the relationships between features.
2.  **Data Preprocessing:** Features were selected, and the data was split into training and testing sets. Categorical features like 'Gender' were handled appropriately.
3.  **Model Training:** A **Linear Regression** model from Scikit-learn was trained on the preprocessed data to predict `Car Purchase Amount`.
4.  **Model Evaluation:** The model's performance was evaluated on the test set. Key metrics like R-squared score and Mean Absolute Error were analyzed.
5.  **Model Serialization:** The final trained model was saved to `model.pkl` using joblib for use in the Flask application.

---

## 🚀 Getting Started Locally

### 1. **Clone the Repository**
```bash
git clone https://github.com/hemalatha0303/Car_sales_prediction_deployedInAWS.git
cd [YOUR-REPO-NAME]
```

### 2. **Set Up a Virtual Environment**
```bash
# Create and activate the environment
python -m venv venv
source venv/bin/activate  # On Windows: `.\venv\Scripts\activate`
```

### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4. **Run the Flask App**
```bash
python app.py
```
> 🎉 Your application is now running at **http://127.0.0.1:5000**!

---

## 🐳 Running with Docker

This application is fully containerized. To run it using Docker, follow these steps:

### 1. **Build the Docker Image**
```bash
docker build -t car-prediction-app .
```

### 2. **Run the Docker Container**
```bash
docker run -p 5000:5000 car-prediction-app
```
> The application will be accessible at **http://localhost:5000**.

---

## ☁️ Cloud Deployment on AWS EC2

This application was deployed to the cloud using the following steps:
1.  **Launch an EC2 Instance:** An Amazon Linux or Ubuntu instance was provisioned.
2.  **Configure Security Group:** The security group was configured to allow incoming traffic on port 80 (HTTP) and port 22 (SSH).
3.  **Install Docker:** Docker was installed on the EC2 instance.
4.  **Transfer Files:** The project files (including `app.py`, `Dockerfile`, `model.pkl`, etc.) were securely transferred to the instance.
5.  **Build & Run Container:** The Docker image was built and run on the EC2 instance, exposing the application to the internet.
