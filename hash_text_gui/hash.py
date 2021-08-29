from tkinter import *
from tkinter import ttk
import hashlib

class App(Frame):
    def __init__(self ,master = Tk()):
        self.master = master
    
    def settings(self):
        self.master.minsize(380,220)
        self.master.maxsize(380,220)
        self.master.title('Hash Text')
        self.master.iconbitmap('icon.ico')
        self.master.configure(bg='steelblue3')
    def widgets(self):
        self.plain = StringVar()
        self.hash_type = StringVar()
        self.hashed = StringVar()

        def hash_text():
            result = ''
            if self.hash_type.get() == 'SHA1':
                result = hashlib.sha1(b'f"{self.plain.get()}"')
            elif self.hash_type.get() == 'SHA224':
                result = hashlib.sha224(b'f"{self.plain.get()}"')
            elif self.hash_type.get() == 'SHA512':
                result = hashlib.sha512(b'f"{self.plain.get()}"')
            elif self.hash_type.get() == 'MD5':
                result = hashlib.md5(b'f"{self.plain.get()}"')
                
            self.hashed.set(result.hexdigest())
        self.plain_label = Label(text='Plain Text: ',font='verdana 15 bold',relief='flat').place(x=10, y=20)
        self.plain_entry = Entry(font='courier 18 bold',width=15,textvariable=self.plain).place(x=150, y=20)

        self.hash_btn = Button(text='Hash',font='simsun 15 bold',bg='royalblue', fg='white',command=hash_text).place(x=250, y=70)
        self.hash_type.set('MD5')
        self.cbox = ttk.Combobox(values=["SHA1","SHA224","SHA512","MD5"],
                                 font='simsun 13 bold',textvariable=self.hash_type).place(x=10,y=80)
        self.hashed_entry = Entry(font='courier 18 bold',width=25,textvariable=self.hashed).place(x=10, y=130)
        
app = App()
app.settings()
app.widgets()
mainloop()
