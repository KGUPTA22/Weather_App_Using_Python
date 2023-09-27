from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("WEATHER APP")
root.geometry("800x550")
root.resizable(False,False)

def Getweather():
    try:
        city = textfield.get()


        geolocator = Nominatim(user_agent="geopiExercises")
        location = geolocator.geocode(city)
        object = TimezoneFinder()
        result = object.timezone_at(lng=location.longitude, lat = location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text = "CURRENT WEATHER")

        #weather
        api ="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=8be2cdb00a1a1dcbaec4d35db1b2b74a"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp =int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text = (temp,"°"))
        c.config(text = (condition,"|","FEELS","LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry")


#search box
Searchimg = PhotoImage(file = "search.png")
myimage = Label(image = Searchimg)
myimage.place(x = 20 , y = 20)

textfield = Entry(root,justify= "center", width = 18 , font = "cambria 22 bold",bg = '#404040',border = 0 , fg = "white")
textfield.place(x =50, y = 41)
textfield.focus()

Searchicon = PhotoImage(file = "search_icon.png")
myimageicon = Button(image = Searchicon,cursor = "hand2",borderwidth = 0,bg = "#404040",command = Getweather)
myimageicon.place(x=390, y = 33)

#logo
Logoimg = PhotoImage(file = "logo.png")
logo = Label(image = Logoimg)
logo.place(x = 140,y = 140)

#Bottombox
bottomimg = PhotoImage(file = "box.png")
bottom = Label(image= bottomimg)
bottom.pack(padx = 5, pady = 5, side = BOTTOM)

#TIME
name = Label(root, font= "Lucida 13 bold")
name.place(x = 25 , y = 100)
clock = Label(root,font= "Times 20")
clock.place(x = 30, y = 130)

#labels
label1 = Label(root, text = "WIND", font="Lucida 13 bold", fg = "white", bg = "#1ab5ef")
label1.place(x = 80,y = 453)
label2 = Label(root, text = "HUMIDITY", font="Lucida 13 bold", fg = "white", bg = "#1ab5ef")
label2.place(x = 230,y = 453)
label3 = Label(root, text = "DESCRIPTION", font="Lucida 13 bold", fg = "white", bg = "#1ab5ef")
label3.place(x = 410,y = 453)
label4 = Label(root, text = "PRESSURE", font="Lucida 13 bold", fg = "white", bg = "#1ab5ef")
label4.place(x = 630,y = 453)

t = Label(font = "arail 50 bold", fg ="#ee666d")
t.place(x = 390,y = 200)
c= Label(font= "arial 13 bold")
c.place(x =390, y =280)

w = Label(text = ".....",font="arial 17 bold",bg = "#1ab5ef")
w.place(x = 80, y = 480)
h = Label(text = ".....",font="arial 17 bold",bg = "#1ab5ef")
h.place(x = 247, y = 480)
d = Label(text = ".....",font="arial 17 bold",bg = "#1ab5ef")
d.place(x = 422, y = 480)
p = Label(text = ".....",font="arial 17 bold",bg = "#1ab5ef")
p.place(x = 657, y = 480)



root.mainloop()
