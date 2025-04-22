# House Price Prediction

This project provides a user interface for predicting house prices based on size (sqft), number of bedrooms, and number of bathrooms using a pre-trained machine learning model. The model is trained using scikit-learn and is saved as a `.pkl` file, which is loaded into the application for predictions.

## Features

- **User-friendly Interface**: Built using Tkinter for easy interaction.
- **Text-to-Speech Integration**: Uses pyttsx3 to read out the predicted house price.
- **Live Date and Time**: Displays current date and time in the application.
- **Prediction Model**: The model predicts house prices based on input features (size, bedrooms, bathrooms).


## 🔍 How the ML Model Works

This application uses a **Supervised Machine Learning model** to predict house prices.

### ⚙️ Model Details:

- **Model Type**: Decision Tree Regressor
- **Library**: `scikit-learn`
- **Training Data**: A CSV file containing:
  - Size of house (in sqft)
  - Number of bedrooms
  - Number of bathrooms
  - Target: House price

### 🧾 Steps Involved:

1. Data was preprocessed and cleaned using `pandas`
2. Model was trained using:
   ```python
   from sklearn.tree import DecisionTreeRegressor
   model = DecisionTreeRegressor()
   model.fit(X_train, y_train)
## Requirements

To run this project, you'll need to install the following dependencies:

- **Python 3.12** or higher
- **Tkinter** (Usually comes with Python)
- **scikit-learn**: For the machine learning model
- **joblib**: For loading the saved model
- **pyttsx3**: For text-to-speech functionality
- **Pillow**: For image handling

### Install Dependencies

You can install the required packages using `pip`:

```bash
pip install -r requirements.txt
numpy==1.26.0
scikit-learn
pyttsx3
joblib
Pillow
```
## How to Use
Run the Application:
Open terminal/command prompt and run house_price.py.

Enter Inputs:
Provide house size, number of bedrooms, and bathrooms.

Click "Predict":
The predicted house price will be displayed and read aloud using Text-to-Speech.

# 📁 Folder Structure

house_price_project/
├── house_price.py
├── house_price_model.pkl
├── icon.ico
├── icon.jpg
├── house.jpeg
├── README.md
## Download Inno Setup here:
[![Download Setup](https://img.shields.io/badge/DOWNLOAD-SETUP-brightgreen?style=for-the-badge)](https://github.com/Priyanshu-Gupta-git/House-Price-Prediction/releases/tag/house_price_Prediction)

# 👑 Credits & License
### 📞 Contact

Made with Python & Tkinter And ML 🐍
Free to use and modify under the MIT License
Author: PRIYANSHU GUPTA
  Priyanshu Gupta
🧑‍💻 B.Tech CSE Student | GitHub : https://github.com/Priyanshu-Gupta-git
Linkedln link: https://www.linkedin.com/feed/?trk=guest_homepage-basic_google-one-tap-submit

