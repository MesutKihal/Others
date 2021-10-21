import pyautogui
import time
import tkinter as tk

class App:
    def __init__(self):
        self.master = tk.Tk()

    def settings(self):
        self.master.title("cmd bot")
        self.master.minsize(300, 300)
        self.master.maxsize(300, 300)

    def widgets(self):
        def bot(command):
            pyautogui.keyDown("winleft")
            time.sleep(1)
            pyautogui.keyUp("winleft")
            time.sleep(5)
            pyautogui.typewrite("cmd")
            time.sleep(5)
            pyautogui.keyDown("Enter")
            time.sleep(1)
            pyautogui.keyUp("Enter")
            time.sleep(5)
            pyautogui.typewrite(command)
            pyautogui.keyDown("Enter")
            time.sleep(1)
            pyautogui.keyUp("Enter")
        self.cmdVar = tk.StringVar()
        self.lbl = tk.Label(self.master, font="coourier 12", text="Enter your command").place(x=20, y=50)
        self.cmdEntry = tk.Entry(self.master, textvariable=self.cmdVar, relief="ridge", font="verdana 12", width=20).place(x=20, y=100)
        self.btn = tk.Button(self.master, text="Start", font="courier 10 bold", bg="orange", command=lambda : bot(self.cmdVar.get())).place(x=80, y=180)

if __name__ == '__main__':
    my_bot = App()
    my_bot.settings()
    my_bot.widgets()
    tk.mainloop()
