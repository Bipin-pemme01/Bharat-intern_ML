# 🏡 House Price Prediction Web App

A simple machine learning web application that predicts house prices based on features like area, bedrooms, bathrooms, stories, and parking availability.

---

## 🚀 Project Overview

This project demonstrates how to:
- Train a Linear Regression model using housing data.
- Save and load models with `pickle`.
- Build an interactive frontend using **Streamlit**.
- Make real-time predictions based on user input.

---

## 🧾 Files in This Project

| File Name             | Description |
|-----------------------|-------------|
| `Houseprice_prediction.ipynb` | Jupyter notebook with initial data exploration and model testing |
| `train_model.py`      | Script to preprocess data, train the Linear Regression model, and save it as `model.pkl` |
| `model.pkl`           | Trained model file saved using `pickle` |
| `Housing.csv`         | Dataset containing housing features and prices |
| `app.py`              | Streamlit app that loads the model and provides a UI for price prediction |

---

## 🧠 Features Used for Prediction

- `area` (in square feet)
- `bedrooms`
- `bathrooms`
- `stories`
- `parking`

---
### 🖥️ App UI
![Streamlit UI](https://raw.githubusercontent.com/Bipin-pemme01/py03/main/ML/Linear_reg/HousePricePrediction/screenshot_app.png)



## ▶️ How to Run the App

### 1. Clone the repository or download the files:
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
