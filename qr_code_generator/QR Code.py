import tkinter as tk
import qrcode


class App:
    def __init__(self, master=tk.Tk()):
        self.master = master

    def settings(self):
        self.master.minsize(315, 180)
        self.master.maxsize(315, 180)
        self.master.title('QR code generator')
        self.master.configure(bg="gray90")

    def widgets(self):
        text_to_encode = tk.StringVar()
        img_name = tk.StringVar()
        ext = tk.StringVar()
        self.txt_lbl = tk.Label(self.master, font="arial 14 bold", text="Text to encode", fg="black", bg="gray90").place(x=10, y=0)
        self.txt_entry = tk.Entry(self.master, font="courier 14", textvariable=text_to_encode, width=26).place(x=10, y=30)
        self.img_lbl = tk.Label(self.master, font="arial 14 bold", text="Image output name", fg="black", bg="gray90").place(x=10, y=60)
        self.img_entry = tk.Entry(self.master, font="courier 14", textvariable=img_name, width=20).place(x=10, y=90)
        self.ext_entry = tk.Entry(self.master, font="courier 14", textvariable=ext, width=5).place(x=240, y=90)
        ext.set(".jpg")
        def encode():
            qr = qrcode.make(text_to_encode.get())
            qr.save(f"{img_name.get()}{ext.get()}")
            
        self.encode_btn = tk.Button(self.master, text="Generate", font="courier 14 bold", fg="white", bg="purple3", command=encode).place(x=125,y=140)

qr_app = App()
qr_app.settings()
qr_app.widgets()
tk.mainloop()

