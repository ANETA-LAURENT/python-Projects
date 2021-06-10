# With an use of Weather API ,country-converter 0.7.3 I've build an app to show current weather in
# specific city entered by input.
from typing import Text
import requests
import base64
import country_converter as coco
import tkinter as tk
from pprint import pprint
from datetime import datetime

api_key = '197114120126a5a6ed2aa93ee517a5ae'

# tkinter app
root = tk.Tk()

root.title("Weather city search")
root.geometry("600x500+50+50")
root.attributes("-topmost", 1)
root.configure(bg="white")

canvas1 = tk.Canvas(root, width=400, height=400, relief="raised")
canvas1.pack(expand=1)
label1 = tk.Label(root, text=("Enter city name"))
label1.config(font=("helvetica", 16))
label1.configure(bg="white")
canvas1.create_window(200, 35, window=label1)
canvas1.configure(bg="white")

entry1 = tk.Entry(root, bd=4, width=15)
entry1.config(font=("helvetica", 12))
canvas1.create_window(200, 100, window=entry1)


''' def get_icon_data():
    city_name = entry1.get()
    result = forecast(city_name)
    z = result["weather"]
    weather_icon = z[0]["icon"]

    url2 = 'http://openweathermap.org/img/wn/{icon}.png'.format(
        icon=weather_icon)
    response = requests.get(url2)
    p = response.json()
    return p '''


# function to search weather forecast by city name with api openweathermap


def forecast(city_name):
    url = 'http://api.openweathermap.org/data/2.5/weather?' + \
        "appid=" + api_key + "&q=" + city_name
    response = requests.get(url)
    x = response.json()
    return x


def check_weather():
    city_name = entry1.get()
    result = forecast(city_name)
    converter = coco.CountryConverter()

    if result["cod"] != "404":
        # search for temperature( which is converted from original Kevin into Celcius), humidity and  atmosphericpressure
        y = result["main"]
        current_temperature_kev = y["temp"]
        current_temperature_c = int(current_temperature_kev - 273.15)
        felt_temperature_kev = y['feels_like']
        felt_temperature_c = int(felt_temperature_kev - 273.15)
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]

    # use package country converter to convert iso country code ex. UA into official name of the country
        iso3_codes = result['sys']
        country = iso3_codes['country']
        country_official_name = converter.convert(
            names=country, to='name_official')
# show type of the weather
        z = result["weather"]
        weather_description = z[0]["description"]
        weather_icon = z[0]['icon']
        timestamp = result["dt"]
        dt_object = datetime.fromtimestamp(timestamp)
        text_to_print = "In " + city_name.upper() + " (in " + country_official_name + ") \n" + "current temperature is " + str(current_temperature_c) + "°C and felt air temperature " + \
            str(felt_temperature_c) + "°C\n the atmospheric pressure is " + str(current_pressure) + \
            "hPa,\n humidity " + str(current_humidity) + \
            "% and\n there are(is): " + weather_description + \
            ".\nTime of data collection: " + \
            str(dt_object)
        label3 = tk.Label(
            root, text=text_to_print, font=("Furura", 11))
        canvas1.create_window(200, 260, window=label3)
        label3.configure(bg="white")

    else:
        label3 = tk.Label(
            root, text="Sorry but we didn't found " + city_name + " as a city name.", font=("Roboto", 11))
        canvas1.create_window(200, 270, window=label3)
        label3.configure(bg="white")


def clear():

    canvas1.delete(5, "end")  # delate label3
    canvas1.delete(6, "end")  # delate label3 of else
    entry1.delete(0, 'end')
    return None


button1 = tk.Button(
    text="Find",
    command=check_weather,
    bg="brown",
    fg="white",
    activebackground="tomato",
    font=("helvetica", 12, "bold"),
)
canvas1.create_window(160, 180, window=button1)

button2 = tk.Button(
    text="Clear",
    command=clear,
    bg="black",
    fg="white",
    font=("helvetica", 12, "bold"),
)
canvas1.create_window(250, 180, window=button2)

root.mainloop()
