from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class App(Frame):
    def __init__(self ,master = Tk()):
        self.master = master
        
        
    def settings(self):
        self.master.geometry('400x300')
        self.master.minsize(400,300)
        self.master.maxsize(400,300)
        self.master.title('Base Converter')
        self.master.iconbitmap('converter.ico')
        self.master.configure(bg='black')
    def widgets(self):
        #Variables
        self.ste = StringVar()
        self.nde = StringVar()
        self.stevar = StringVar()
        self.ndevar = StringVar()
        #Widget_Functions
        def helpinfo():
            messagebox.showinfo('Help','This program cannot convert numbers over:\n\n   999999 - (Decimal)\n   FFFFF - (Hexadecimal)\n   3777777 - (Octal)\n   11111111111111111111 - (Binary)')
        def convert():
            array = []
            if self.stevar.get() == 'Decimal' and self.ndevar.get() == 'Binary':
                try:
                    assert self.ste.get().isdigit() == True
                    n = int(self.ste.get())
                    t = 524288
                    while 1 <= t:
                        if  n // t > 0:
                            temp = t * (n // t)
                            array.append('1')
                            n -= temp
                        else:
                            array.append('0')
                        t = t / 2
                except AssertionError:
                    messagebox.showerror("Error", "Wrong Format")
            if self.stevar.get() == 'Binary' and self.ndevar.get() == 'Decimal':
                try:
                    assert self.ste.get().isdigit() == True
                    n = str(self.ste.get())
                    r = 0
                    base = 2
                    size = len(n)
                    count = 0
                    while count < size:
                        try:
                            assert n[-(count+1)] == '0' or n[-(count+1)] == '1'
                            r += int(n[-(count+1)]) * base**count
                            count += 1
                        except AssertionError:
                            messagebox.showerror("Error", "Wrong Format")
                            break
                    array.append(str(r))
                except AssertionError:
                    messagebox.showerror("Error", "Wrong Format")

            if self.stevar.get() == 'Decimal' and self.ndevar.get() == 'Hexadecimal':
                try:
                    assert self.ste.get().isdigit() == True
                    n = int(self.ste.get())
                    t = 65536
                    hexa_table = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:'A',
                                  11:'B',12:'C',13:'D',14:'E',15:'F'}
                    while t >= 1:
                        array.append(str(hexa_table.get(n//t)))
                        n -= t * (n//t)
                        t = t // 16
                except AssertionError:
                    messagebox.showerror("Error", "Wrong Format")
            if self.stevar.get() == 'Hexadecimal' and self.ndevar.get() == 'Decimal':
                try:
                    n = str(self.ste.get())
                    base = 16
                    size = len(n)
                    count = 0
                    hexa_table = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,
                                  'B':11,'C':12,'D':13,'E':14,'F':15}
                    while count < size:
                        array.append(int(hexa_table.get(n[-(count+1)])) * base**count)
                        count += 1
                    
                    array = [str(sum(array))]
                except TypeError:
                    messagebox.showerror("Error", "Wrong Format")
            if self.stevar.get() == 'Decimal' and self.ndevar.get() == 'Octal':
                try:
                    assert self.ste.get().isdigit() == True
                    n = int(self.ste.get())
                    t = 2097152
                    while t >= 1:
                        array.append(str(n//t))
                        n -= t * (n//t)
                        t = t // 8
                except AssertionError:
                    messagebox.showerror("Error", "Wrong Format")
            if self.stevar.get() == 'Octal' and self.ndevar.get() == 'Decimal':
                try:
                    assert self.ste.get().isdigit() == True
                    n = str(self.ste.get())
                    base = 8
                    size = len(n)
                    count = 0
                    while count < size:
                        array.append(int(n[-(count+1)]) * base**count)
                        count += 1
                    
                    array = [str(sum(array))]
                except AssertionError:
                    messagebox.showerror("Error", "Wrong Format")
            if self.stevar.get() == 'Binary' and self.ndevar.get() == 'Hexadecimal':
                try:
                    assert self.ste.get().isdigit() == True
                    n = str(self.ste.get())
                    r = 0
                    base = 2
                    size = len(n)
                    count = 0
                    while count < size:
                        try:
                            assert n[-(count+1)] == '0' or n[-(count+1)] == '1'
                            r += int(n[-(count+1)]) * base**count
                            count += 1
                        except AssertionError:
                            messagebox.showerror("Error", "Wrong Format")
                            break
                    n = r
                    t = 65536
                    hexa_table = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:'A',
                                  11:'B',12:'C',13:'D',14:'E',15:'F'}
                    while t >= 1:
                        array.append(str(hexa_table.get(n//t)))
                        n -= t * (n//t)
                        t = t // 16
                except AssertionError:
                    messagebox.showerror("Error", "Wrong Format")
            if self.stevar.get() == 'Hexadecimal' and self.ndevar.get() == 'Binary':
                try:
                    n = str(self.ste.get())
                    base = 16
                    size = len(n)
                    count = 0
                    hexa_table = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,
                                  'B':11,'C':12,'D':13,'E':14,'F':15}
                    while count < size:
                        array.append(int(hexa_table.get(n[-(count+1)])) * base**count)
                        count += 1
                    
                    n = sum(array)
                    t = 524288
                    array = []
                    while 1 <= t:
                        if  n // t > 0:
                            temp = t * (n // t)
                            array.append('1')
                            n -= temp
                        else:
                            array.append('0')
                        t = t / 2
                except TypeError:
                    messagebox.showerror("Error", "Wrong Format")
            if self.stevar.get() == 'Binary' and self.ndevar.get() == 'Octal':
                try:
                    assert self.ste.get().isdigit() == True
                    n = str(self.ste.get())
                    r = 0
                    base = 2
                    size = len(n)
                    count = 0
                    while count < size:
                        try:
                            assert n[-(count+1)] == '0' or n[-(count+1)] == '1'
                            r += int(n[-(count+1)]) * base**count
                            count += 1
                        except AssertionError:
                            messagebox.showerror("Error", "Wrong Format")
                            break
                    n = r
                    t = 2097152
                    while t >= 1:
                        array.append(str(n//t))
                        n -= t * (n//t)
                        t = t // 8
                except AssertionError:
                    messagebox.showerror("Error", "Wrong Format")
            if self.stevar.get() == 'Octal' and self.ndevar.get() == 'Binary':
                try:
                    assert self.ste.get().isdigit() == True
                    n = str(self.ste.get())
                    base = 8
                    size = len(n)
                    count = 0
                    while count < size:
                        array.append(int(n[-(count+1)]) * base**count)
                        count += 1
                    
                    n = sum(array)
                    t = 524288
                    array = []
                    while 1 <= t:
                        if  n // t > 0:
                            temp = t * (n // t)
                            array.append('1')
                            n -= temp
                        else:
                            array.append('0')
                        t = t / 2
                except AssertionError:
                    messagebox.showerror("Error", "Wrong Format")
            if self.stevar.get() == 'Hexadecimal' and self.ndevar.get() == 'Octal':
                try:
                    n = str(self.ste.get())
                    base = 16
                    size = len(n)
                    count = 0
                    hexa_table = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,
                                  'B':11,'C':12,'D':13,'E':14,'F':15,'G':16}
                    while count < size:
                        array.append(int(hexa_table.get(n[-(count+1)])) * base**count)
                        count += 1
                    
                    n = sum(array)
                    t = 2097152
                    array = []
                    while t >= 1:
                        array.append(str(n//t))
                        n -= t * (n//t)
                        t = t // 8
                except TypeError:
                    messagebox.showerror("Error", "Wrong Format")
                    
            if self.stevar.get() == 'Octal' and self.ndevar.get() == 'Hexadecimal':
                try:
                    assert self.ste.get().isdigit() == True
                    n = str(self.ste.get())
                    base = 8
                    size = len(n)
                    count = 0
                    while count < size:
                        array.append(int(n[-(count+1)]) * base**count)
                        count += 1
                        
                    n = sum(array)
                    t = 65536
                    array = []
                    hexa_table = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:'A',
                                  11:'B',12:'C',13:'D',14:'E',15:'F',16:'G'}
                    while t >= 1:
                        array.append(str(hexa_table.get(n//t)))
                        n -= t * (n//t)
                        t = t // 16
                except AssertionError:
                    messagebox.showerror("Error", "Wrong Format")
                    
            self.nde.set(''.join(array))
            if len(str(self.nde.get())) > 18:self.b.place(x=335,y=170)
            else:self.b.place_forget()

            if self.stevar.get() == self.ndevar.get():
                if self.ste.get() == 'Hexadecimal':
                    try:
                        self.nde.set(str(self.ste.get()))
                    except TypeError:
                        messagebox.showerror("Error", "Wrong Format")
                else:
                    try:
                        assert self.ste.get().isdigit() == True
                        self.nde.set(str(self.ste.get()))
                    except AssertionError:
                        messagebox.showerror("Error", "Wrong Format")

        def reset():
            if len(str(self.nde.get())) > 18:self.b.place_forget()
            self.ste.set('')
            self.nde.set('')
        #Widgets
        self.cnvtImg = PhotoImage(file=r'convert.png')
        self.rstImg = PhotoImage(file=r'reset.png')
        self.stcbox = ttk.Combobox(self.master,
                                 values=[
                                     "Decimal", 
                                     "Binary",
                                     "Hexadecimal",
                                     "Octal"],
                                     textvariable=self.stevar).place(x=30,y=30)
        self.stevar.set('Binary') #Default Value 1st ComboBox
        self.ndcbox = ttk.Combobox(self.master,
                                 values=[
                                 "Decimal", 
                                 "Binary",
                                 "Hexadecimal",
                                 "Octal"],
                                 textvariable=self.ndevar).place(x=30,y=175)
        self.ndevar.set('Decimal') #Default Value 2nd ComboBox
        self.b = Label(self.master,text='==>',font='rod 12 bold',bg='red')
        self.entry = Entry(self.master,bg='white',relief='groove',font='Verdana 32',width= 7,textvariable=self.ste).place(x=10, y=60)
        self.convertBtn = Button(self.master, image=self.cnvtImg,command=convert).place(x=30,y=120)
        self.resetBtn = Button(self.master, image=self.rstImg,command=reset).place(x=210,y=65)
        self.result = Entry(self.master,font='Verdana 24',bg='white',width=18,textvariable=self.nde).place(x=10,y=200)
        self.help = Button(self.master,text='¡',font='Rod 12 bold',fg='white',bg='blue',command=helpinfo).place(x=360,y=20)

app = App()
app.settings()
app.widgets()
mainloop()
