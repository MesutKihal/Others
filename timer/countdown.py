
import datetime as dt
import tkinter as tk
import time

root = tk.Tk()
root.maxsize(300, 150)
root.minsize(300, 150)
root.title("TIMER")
root.configure(bg="orange")
sec = tk.StringVar()
seconds = tk.StringVar()
entry = tk.Entry(root, textvariable=sec, font="verdana 16 bold", relief="sunken", width=15).place(x=0, y=2)
def countdown():
     secs = int(sec.get())
     for s in range(secs+1):
          seconds.set(dt.timedelta(seconds=secs-s))
          time.sleep(1)
          root.update_idletasks()
label = tk.Label(root, textvariable=seconds, font="verdana 30 bold", bg="orange", fg="black").place(x=30, y=70)
button = tk.Button(root, text="start", font="verdana 12 bold", bg="black", fg="white", command=countdown).place(x=240, y=0)
tk.mainloop()
