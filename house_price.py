import pandas as pd
import os
import sys
import joblib
from tkinter import * 
from PIL import Image, ImageTk
from datetime import datetime
import pyttsx3


base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))


model_path = os.path.join(base_path, 'house_price_model.pkl')
icon_path = os.path.join(base_path, 'icon.ico')
main_bg_path = os.path.join(base_path, 'house.jpeg')
second_icon_path = os.path.join(base_path, 'icon.ico')
second_bg_path = os.path.join(base_path, 'icon.jpg')


model = joblib.load(model_path)


root = Tk()
root.title("House Price Prediction")
root.geometry("1200x800+100+0") 
root.resizable(False, False)
root.iconbitmap(icon_path)

main_bg_img = Image.open(main_bg_path)  
main_bg_img = main_bg_img.resize((1200, 800)) 
main_bg = ImageTk.PhotoImage(main_bg_img)

main_label = Label(root, image=main_bg)
main_label.place(x=0, y=0, relwidth=1, relheight=1)

Label(root, text="Welcome To House Price Prediction", font=("Goudy Stout", 24), bg="skyblue", fg="black", relief="sunken").place(x=0, y=10)

def open_second_window():
    second_window = Toplevel(root)
    second_window.title("House Price Prediction")
    second_window.iconbitmap(second_icon_path)
    second_window.geometry("1200x800+100+0") 
    second_window.resizable(False, False)

    image = Image.open(second_bg_path)  
    image = image.resize((1200, 800)) 
    bg = ImageTk.PhotoImage(image)
    second_window.bg_image = bg 

    bg_label = Label(second_window, image=bg)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    date_label = Label(second_window, text="", font=("Helvetica", 20), fg="skyblue", bg="black")
    date_label.place(x=10, y=10)

    time_label = Label(second_window, text="", font=("Helvetica", 24), fg="skyblue", bg="black")
    time_label.place(x=10, y=50)

    def update_time():
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%d-%m-%Y")
        time_label.config(text="Time: " + current_time)
        date_label.config(text="Date: " + current_date)
        second_window.after(1000, update_time)

    update_time()

    Label(second_window, text="Size (sqft):", font=("Copperplate Gothic Bold", 18),bd=2, relief="solid", bg="silver").place(x=400, y=10)
    size_entry = Entry(second_window,bd=5, relief="solid", font=("Copperplate Gothic Bold", 18))
    size_entry.place(x=580, y=10)

    Label(second_window, text="Bedrooms:", font=("Copperplate Gothic Bold", 18),bd=2, relief="solid", bg="silver").place(x=400, y=50)
    beds_entry = Entry(second_window,bd=5, relief="solid", font=("Copperplate Gothic Bold", 18))
    beds_entry.place(x=580, y=50)

    Label(second_window, text="Bathrooms:", font=("Copperplate Gothic Bold", 18), bg="silver",bd=2, relief="solid").place(x=400, y=90)
    baths_entry = Entry(second_window,bd=5, relief="solid",font=("Copperplate Gothic Bold", 18))
    baths_entry.place(x=580, y=90)

    result_label = Label(second_window, bd=2, relief="sunken",text="", font=("Goudy Stout", 25), bg="gold", fg="black")
    result_label.place(x=20, y=200)

    def predict_price():
        try:
            size = float(size_entry.get())
            beds = int(beds_entry.get())
            baths = int(baths_entry.get())
            input_data = pd.DataFrame([[size, beds, baths]], columns=['size', 'beds', 'baths'])
            predicted_price = model.predict(input_data)
            result_label.config(text=f"Predicted Price: ₹{predicted_price[0]:,.2f}")
            engine = pyttsx3.init()
            price_text = f"Predicted price is {predicted_price[0]:,.2f} rupees"
            engine.say(price_text)
            engine.runAndWait()

        except Exception as e:
            result_label.config(text="Error ! Please Enter correct values")
            engine = pyttsx3.init()
            engine.say("Error hai! Please enter correct values")
            engine.runAndWait()

    Button(second_window, text="Predict",  font=("Copperplate Gothic Bold", 20,"bold"), bg="brown", fg="white", command=predict_price).place(x=550, y=130)

root.after(4000, open_second_window)
root.mainloop()
