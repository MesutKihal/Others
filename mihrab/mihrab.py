
import tkinter as tk
from tkinter import ttk
import datetime
from hijri_converter import convert
import time as tm
import subprocess
import requests
import json
import aladhan
import re
import calendar
import pygame

class App(tk.Frame):
    def __init__(self, master = tk.Tk()):
        self.master = master
        self.bgImg = tk.PhotoImage(file=r"assets/bg.png")
        self.onImage = tk.PhotoImage(file=r"assets/audio.png").subsample(15, 15)
        self.offImage = tk.PhotoImage(file=r"assets/mute.png").subsample(15, 15)
        self.clockGif = tk.PhotoImage(file=r"assets/clock.gif").subsample(6, 6)
        self.mapImg = tk.PhotoImage(file=r"assets/map.png").subsample(2, 2)
        self.icon = tk.PhotoImage(file=r"assets/icon.png")
        self.adhanAudio = "assets/adhan1.mp3"
        self.audioBool = True
        self.audioPlay = False
        self.nextPrayer = None


    def settings(self):
        self.master.minsize(1190, 700)
        self.master.maxsize(1190, 700)
        self.master.title("Mirhab Salat Reminder")
        self.master.iconphoto(False, self.icon)

    def widgets(self):
        pygame.mixer.init()
        prayerTimes = ["--:--", "--:--", "--:--", "--:--", "--:--"]
        prayerNames = ["Fajr", "Duhr", "Asr", "Maghreb", "Isha'a"]
        def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
            points = [x1+radius, y1,
                      x1+radius, y1,
                      x2-radius, y1,
                      x2-radius, y1,
                      x2, y1,
                      x2, y1+radius,
                      x2, y1+radius,
                      x2, y2-radius,
                      x2, y2-radius,
                      x2, y2,
                      x2-radius, y2,
                      x2-radius, y2,
                      x1+radius, y2,
                      x1+radius, y2,
                      x1, y2,
                      x1, y2-radius,
                      x1, y2-radius,
                      x1, y1+radius,
                      x1, y1+radius,
                      x1, y1]

            return self.canvas.create_polygon(points, **kwargs, smooth=True)

        def AudioOnOff():
            if self.audioBool:
                self.audioOff.configure(image=self.offImage)
                self.audioBool = False
                pygame.mixer.music.stop()
            else:
                self.audioOff.configure(image=self.onImage)
                self.audioBool = True
            return

        def PlayAudio():
            if self.audioBool:
                pygame.mixer.music.load(self.adhanAudio)
                pygame.mixer.music.play()

        def UpdateTime():
            # Get current time
            current_time = tm.strftime('%H:%M:%S')
            current_date = str(datetime.datetime.now())[:10]
            formatted_date = datetime.datetime.strptime(current_date, '%Y-%m-%d')
            
            # Convert time to Hijri
            hijri_date = convert.Gregorian.fromdate(formatted_date).to_hijri()
            # Update their respective labels
            self.timeLbl.config(text=current_time)
            self.DateLbl.config(text=f"""{hijri_date} / {current_date}""")
            # Get the next prayer
            minDiff = None
            operator = ""
            prayerName = ""
            fg = "red"
            i = 0
            for prayer in prayerTimes:
                current = datetime.datetime.strptime(current_time, "%H:%M:%S")
                prayer = datetime.datetime.strptime(prayer, "%H:%M:%S")
                diff = abs(current - prayer)
                if not minDiff:
                    prayerName = prayerNames[i]
                    minDiff = diff
                else:
                    if diff < minDiff:
                        prayerName = prayerNames[i]
                        minDiff = diff
                if current >= prayer:
                    fg = "black"
                    operator = "+"
                    if diff == datetime.timedelta(seconds=2) and operator == "+":
                        self.audioPlay = True
                        PlayAudio()
                if current < prayer:
                    operator = "-"
                    if diff < datetime.timedelta(seconds=1800):
                        fg = "red"
                i += 1
            self.DiffLbl.config(text=f"{operator} {minDiff}", fg=fg)
            self.prayerLbl.config(text=f"{prayerName}")
            self.master.after(1000, UpdateTime)

        def Locate():
            # Get location info from IP
            result = subprocess.run("curl ipinfo.io", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout
            current_date = str(datetime.datetime.now())[:10]
            loc = json.loads(result)["loc"].split(",")
            city = json.loads(result)["city"]
            location = aladhan.Coordinates(float(loc[0]), float(loc[1]))
            client = aladhan.Client(location)
            self.canvas.create_text(450, 100, font="simplex_iv25 36 bold", fill="white", text=f"{city}")
            # Get adhan timings based on the coordinates
            timings = [str(adhan) for adhan in client.get_today_times()]
            timePattern = re.compile(r"[0-9]{1}[0-9]{1}:[0-9]{1}[0-9]{1}")
            pPattern = re.compile(r"[A-Z]{1}[A-Z]{1}")
            Ps = re.findall(pPattern, "".join(timings))
            timings = re.findall(timePattern, "".join(timings))
            # Update Calendar
            cal = calendar.TextCalendar()
            self.calnderLabel = tk.Label(self.master, bg="#fff", font="simplex_iv25 10", text=cal.formatmonth(int(current_date[:4]), int(current_date[5:7]))).place(x=350, y=520)
            # Drawing the timings to the screen
            axis = [150, 380, 610, 840, 1070]
            for i in range(len(axis)):
                time_obj = datetime.datetime.strptime(f"{timings[i]} {Ps[i]}", '%I:%M %p')
                time_24h = time_obj.strftime('%H:%M')
                prayerTimes[i] = time_24h+":00"
                self.canvas.create_text(axis[i], 280, font="rockwell 30 bold", fill="black", text=f"{time_24h}")
            

        self.canvas = tk.Canvas(self.master, width=1190, height=700)
        self.canvas.place(x=0, y=0)
        self.canvas.create_image(960, 560, image=self.bgImg)
        self.canvas.create_image(200, 80, image=self.mapImg)
        # Fajr
        round_rectangle(50, 200, 250, 400, radius=20, fill="#dde")
        self.canvas.create_text(150, 230, font="simplex_iv25 18 bold", fill="black", text="Fajr")
        self.canvas.create_text(150, 330, font="rockwell 20 bold", fill="black", text="AM")
        # Duhr
        round_rectangle(280, 200, 480, 400, radius=20, fill="#dde")
        self.canvas.create_text(380, 230, font="simplex_iv25 18 bold", fill="black", text="Duhr")
        self.canvas.create_text(380, 330, font="rockwell 20 bold", fill="black", text="AM")
        # Asr
        round_rectangle(510, 200, 710, 400, radius=20, fill="#dde")
        self.canvas.create_text(610, 230, font="simplex_iv25 18 bold", fill="black", text="Asr")
        self.canvas.create_text(610, 330, font="rockwell 20 bold", fill="black", text="PM")
        # Maghreb
        round_rectangle(740, 200, 940, 400, radius=20, fill="#dde")
        self.canvas.create_text(840, 230, font="simplex_iv25 18 bold", fill="black", text="Maghreb")
        self.canvas.create_text(840, 330, font="rockwell 20 bold", fill="black", text="PM")
        # Isha'a
        round_rectangle(970, 200, 1170, 400, radius=20, fill="#dde")
        self.canvas.create_text(1070, 230, font="simplex_iv25 18 bold", fill="black", text="Isha'a")
        self.canvas.create_text(1070, 330, font="rockwell 20 bold", fill="black", text="PM")

        round_rectangle(50, 450, 1140, 680, radius=20, fill="#dde")
        self.canvas.create_text(1000, 525, font="simplex_iv25 15 bold", fill="black", text="Audio")
        self.audioOff = tk.Button(self.master, image=self.onImage)
        self.audioOff.configure(command=AudioOnOff)
        self.audioOff.place(x = 1050, y = 500)
        
        # Time
        round_rectangle(70, 480, 250, 670, radius=20, fill="#fff")
        self.canvas.create_text(160, 520, font="simplex_iv25 20 bold", fill="black", text="Time")
        self.timeLbl = tk.Label(self.master, font="simplex_iv25 20", fg="black", bg="#fff", text="--:--")
        self.timeLbl.place(x=90, y=540)
        self.canvas.create_image(150, 620, image=self.clockGif)
        # Calendar
        round_rectangle(300, 480, 600, 670, radius=20, fill="#fff")
        self.canvas.create_text(450, 500, font="simplex_iv25 20 bold", fill="black", text="Calendar")
        # Date
        self.canvas.create_text(785, 520, font="simplex_iv25 20 bold", fill="black", text="Date")
        self.DateLbl = tk.Label(self.master, font="simplex_iv25 16", fg="black", bg="#dde")
        self.DateLbl.place(x=620, y=550)
        self.prayerLbl = tk.Label(self.master, font="simplex_iv25 20 bold", fg="black", bg="#dde")
        self.DiffLbl = tk.Label(self.master, font="rockwell 16 bold", fg="red", bg="#dde")
        self.prayerLbl.place(x=770, y=600)
        self.DiffLbl.place(x=770, y=640)
        Locate()
        UpdateTime()
        

        
        
if __name__ == "__main__":
    mihrab = App()
    mihrab.settings()
    mihrab.widgets()
    tk.mainloop()
    
    
    
        
