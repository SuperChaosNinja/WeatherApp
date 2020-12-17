import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image

url = "https://weather.com/weather/today/l/edaeb599b4628b2e6fb320cbc657a02a651ee03805c8f4ac54528a6804304ec7"

master = Tk()
master.title("Weather App")
master.config(bg="white")

img = Image.open("C:/Users/Windows PC/PycharmProjects/learningPython/PartlyCloudy.png")
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)

def getWeather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find('h1', class_="CurrentConditions--location--1Ayv3").text
    temperature = soup.find('span', class_="CurrentConditions--tempValue--3KcTQ").text
    weatherprediction = soup.find('div', class_="CurrentConditions--phraseValue--2xXSr").text


    locationLabel.config(text=location)
    temperatureLabel.config(text=temperature)
    weatherPredictionLabel.config(text=weatherprediction)
    temperatureLabel.after(60000, getWeather)
    master.update()
    print(location)
    print(temperature)
    print(weatherprediction)
locationLabel = Label(master, font=("Calibri bold", 50), bg="white")
locationLabel.grid(row=0, sticky="N", padx=100)
temperatureLabel = Label(master, font=("Calibri bold", 70), bg="white")
temperatureLabel.grid(row=1, sticky="W", padx=40)
Label(master, image=img, bg="white").grid(row=1, sticky="E")
weatherPredictionLabel = Label(master, font=("Calabri bold", 15), bg="white")
weatherPredictionLabel.grid(row=2,sticky="W", padx=40)
getWeather()
master.mainloop()