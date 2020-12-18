import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image

todayWeatherUrl = "https://weather.com/weather/today/l/edaeb599b4628b2e6fb320cbc657a02a651ee03805c8f4ac54528a6804304ec7"

master = Tk()
master.title("Weather App")
master.config(bg="white")

img = Image.open("C:/Users/Windows PC/PycharmProjects/learningPython/PartlyCloudy.png")
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)

print("Here Is The Weather Forecast:")


def getWeather():
    page = requests.get(todayWeatherUrl)
    soup = BeautifulSoup(page.content, "html.parser")

    location = soup.find('h1', class_="CurrentConditions--location--1Ayv3").text
    location_label.config(text=location)

    current_temperature = soup.find('span', class_="CurrentConditions--tempValue--3KcTQ").text
    current_temperature_label.config(text=current_temperature)
    current_temperature_label.after(60000, getWeather)

    current_conditions = soup.find('div', class_="CurrentConditions--phraseValue--2xXSr").text
    current_conditions_label.config(text=current_conditions)

    tomorrow_temperature = soup.find('span', class_="CurrentConditions--tempValue--3KcTQ").text
    tomorrow_temperature_label.config(text=tomorrow_temperature)

    spans = soup.find_all('span', attrs={'data-testid': 'TemperatureValue'})
    for span in spans:
        print(span.string)

    tomorrow_conditions = soup.find('div', class_="CurrentConditions--phraseValue--2xXSr").text
    tomorrow_conditions_label.config(text=tomorrow_conditions)

    master.update()


location_label = Label(master, font=("Calibri bold", 50), bg="white")
location_label.grid(row=0, sticky="N", padx=50)

current_temperature_label = Label(master, font=("Calibri bold", 70), bg="white")
current_temperature_label.grid(row=1, sticky="W", padx=40)

today_picture = Label(master, image=img, bg="white").grid(row=1, sticky="E")

current_conditions_label = Label(master, font=("Calabri bold", 15), bg="white")
current_conditions_label.grid(row=2, sticky="W", padx=40)

tomorrow_temperature_label = Label(master, font=("Calibri bold", 70), bg="white")
tomorrow_temperature_label.grid(row=3, sticky="W", padx=40)

tomorrow_picture = Label(master, image=img, bg="white").grid(row=3, sticky="E")

tomorrow_conditions_label = Label(master, font=("Calabri bold", 15), bg="white")
tomorrow_conditions_label.grid(row=4, sticky="W", padx=40)

getWeather()
master.mainloop()
