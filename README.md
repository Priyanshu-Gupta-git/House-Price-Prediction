# House Price Prediction

This project provides a user interface for predicting house prices based on size (sqft), number of bedrooms, and number of bathrooms using a pre-trained machine learning model. The model is trained using scikit-learn and is saved as a `.pkl` file, which is loaded into the application for predictions.

## Features

- **User-friendly Interface**: Built using Tkinter for easy interaction.
- **Text-to-Speech Integration**: Uses pyttsx3 to read out the predicted house price.
- **Live Date and Time**: Displays current date and time in the application.
- **Prediction Model**: The model predicts house prices based on input features (size, bedrooms, bathrooms).

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


