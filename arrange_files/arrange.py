from tkinter import *
from tkinter import filedialog
import os
import pickle

class App:
   def __init__(self, master = Tk()):
      self.master = master

   def settings(self):
      self.master.minsize(520,360)
      self.master.maxsize(520,360)
      self.master.title('Arrange Files')
      self.master.iconbitmap('icon.ico')
   def widgets(self):
      self.path = StringVar()
      self.result = StringVar()
      self.com = StringVar()
      self.doc = StringVar()
      self.aud = StringVar()
      self.pro = StringVar()
      self.vid = StringVar()
      self.img = StringVar()
      self.data = pickle.load(open('formats.dat', 'rb'))
      self.com.set(self.data[0])
      self.doc.set(self.data[1])
      self.aud.set(self.data[2])
      self.pro.set(self.data[3])
      self.vid.set(self.data[4])
      self.img.set(self.data[5])
      self.path.set(str(os.environ.get("USERPROFILE")))
      self.result.set('')
      def arrange():
         self.result.set('')
         n_files = 0
         try:
            assert str(self.path.get()) != ''
         except AssertionError:
            self.path.set(str(os.environ.get("USERPROFILE")))
         os.chdir(str(self.path.get()))
         for f in os.listdir(str(self.path.get())):
            #Compressed
            for ext in ['.'+ext for ext in str(self.com.get()).split(',')]:
               if os.path.splitext(f)[1] == ext:
                  try:
                     os.rename(os.path.basename(f), f'Compressed\\{os.path.basename(f)}')
                  except FileNotFoundError:
                       os.mkdir('Compressed')
                  n_files += 1
            #Documents
            for ext in ['.'+ext for ext in str(self.doc.get()).split(',')]:
               if os.path.splitext(f)[1] == ext:
                  try:
                     os.rename(os.path.basename(f), f'Documents\\{os.path.basename(f)}')
                  except FileNotFoundError:
                     os.mkdir('Documents')
                  n_files += 1
            #Music
            for ext in ['.'+ext for ext in str(self.aud.get()).split(',')]:
               if os.path.splitext(f)[1] == ext:
                  try:
                     os.rename(os.path.basename(f), f'Music\\{os.path.basename(f)}')
                  except FileNotFoundError:
                      os.mkdir('Music')
                  n_files += 1
            #Programs
            for ext in ['.'+ext for ext in str(self.pro.get()).split(',')]:
               if os.path.splitext(f)[1] == ext:
                  try:
                     os.rename(os.path.basename(f), f'Programs\\{os.path.basename(f)}')
                  except FileNotFoundError:
                     os.mkdir('Programs')
                  n_files += 1
            #Video
            for ext in ['.'+ext for ext in str(self.vid.get()).split(',')]:
               if os.path.splitext(f)[1] == ext:
                  try:
                     os.rename(os.path.basename(f), f'Video\\{os.path.basename(f)}')
                  except FileNotFoundError:
                     os.mkdir('Video')
                  n_files += 1
            #Images
            for ext in ['.'+ext for ext in str(self.img.get()).split(',')]:
               if os.path.splitext(f)[1] == ext:
                  try:
                     os.rename(os.path.basename(f), f'Pictures\\{os.path.basename(f)}')
                  except FileNotFoundError:
                     os.mkdir('Pictures')
                  n_files += 1            
         self.result.set(f'{n_files} files moved.')
      def change_path():
         folder = filedialog.askdirectory()
         if os.path.splitext(folder)[0] == '':
            self.path.set(str(os.environ.get("USERPROFILE")))
         else:
            self.path.set(os.path.splitext(folder)[0])
      def add_format(var,x_,y_):
         self.e['textvariable'] = var
         self.e.place(x=x_,y=y_)
         self.save.place(x=490,y=y_)
      def remove():
         os.chdir(os.path.dirname(os.path.realpath(__file__)))
         pickle.dump([str(self.com.get()),str(self.doc.get()),str(self.aud.get()),str(self.pro.get()),str(self.vid.get()),str(self.img.get())],open('formats.dat', 'wb'))
         self.e.place_forget()
         self.save.place_forget()
      self.cl = Label(textvariable=self.com,bg='grey85',fg='black',font='newcourier 16',anchor='w',width=26).place(x=10,y=120)
      self.dl = Label(textvariable=self.doc,bg='grey85',fg='black',font='newcourier 16',anchor='w',width=26).place(x=10,y=160)
      self.al = Label(textvariable=self.aud,bg='grey85',fg='black',font='newcourier 16',anchor='w',width=26).place(x=10,y=200)
      self.pl = Label(textvariable=self.pro,bg='grey85',fg='black',font='newcourier 16',anchor='w',width=26).place(x=10,y=240)
      self.vl = Label(textvariable=self.vid,bg='grey85',fg='black',font='newcourier 16',anchor='w',width=26).place(x=10,y=280)
      self.il = Label(textvariable=self.img,bg='grey85',fg='black',font='newcourier 16',anchor='w',width=26).place(x=10,y=320)
      self.cl2 = Label(text='Compressed',bg='grey85',fg='black',font='newcourier 16',anchor='w',width=12).place(x=340,y=120)
      self.dl2 = Label(text='Documents',bg='grey85',fg='black',font='newcourier 16',anchor='w',width=12).place(x=340,y=160)
      self.al2 = Label(text='Music',bg='grey85',fg='black',font='newcourier 16',anchor='w',width=12).place(x=340,y=200)
      self.pl2 = Label(text='Programs',bg='grey85',fg='black',font='newcourier 16',anchor='w',width=12).place(x=340,y=240)
      self.vl2 = Label(text='Video',bg='grey85',fg='black',font='newcourier 16',anchor='w',width=12).place(x=340,y=280)
      self.il2 = Label(text='Pictures',bg='grey85',fg='black',font='newcourier 16',anchor='w',width=12).place(x=340,y=320)
      self.title = Label(text='Please select the directory with the files you want to arrange.',fg='black',font='newcourier 10 bold',anchor='w').place(x=10,y=10)
      self.epath = Entry(textvariable=self.path,fg='white',bg='steelblue3',relief='sunken',font='Platino 16 bold',width=30).place(x=10,y=40)
      self.rst = Label(textvariable=self.result,bg='grey85',fg='black',font='newcourier 19',anchor='w',width=26).place(x=10,y=70)
      self.chbtn = Button(text = '▼', bg='cyan3', fg='white',font='Platino 10 bold',command=change_path).place(x=380,y=40)
      self.arbtn = Button(text = 'Arrange', bg='cyan3', fg='white',font='Platino 13 bold',command=arrange).place(x=410,y=70)
      self.cbtn = Button(text = '▼', bg='cyan3', fg='white',font='Platino 10 bold',command=lambda : add_format(self.com,10,120)).place(x=490,y=120)
      self.dbtn = Button(text = '▼', bg='cyan3', fg='white',font='Platino 10 bold',command=lambda : add_format(self.doc,10,160)).place(x=490,y=160)
      self.abtn = Button(text = '▼', bg='cyan3', fg='white',font='Platino 10 bold',command=lambda : add_format(self.aud,10,200)).place(x=490,y=200)
      self.pbtn = Button(text = '▼', bg='cyan3', fg='white',font='Platino 10 bold',command=lambda : add_format(self.pro,10,240)).place(x=490,y=240)
      self.vbtn = Button(text = '▼', bg='cyan3', fg='white',font='Platino 10 bold',command=lambda : add_format(self.vid,10,280)).place(x=490,y=280)
      self.ibtn = Button(text = '▼', bg='cyan3', fg='white',font='Platino 10 bold',command=lambda : add_format(self.img,10,320)).place(x=490,y=320)
      self.e = Entry(textvariable=None,fg='white',bg='steelblue3',relief='sunken',font='newcourier 16 bold',width=40)
      self.save = Button(text = '◄', bg='cyan3', fg='white',font='Platino 10 bold',command=remove)
arng_f = App()
arng_f.settings()
arng_f.widgets()
mainloop()
