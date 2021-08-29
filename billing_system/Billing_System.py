import tkinter as tk
import pickle
import json


def BillingMenu():

    class App:
        def __init__(self, master=tk.Tk()):
            self.master = master
            self.bg = tk.PhotoImage(file = r'background.png')
            
        def settings(self):
            self.master.maxsize(768, 520)
            self.master.minsize(768, 520)
            self.master.title('Billing System')

        def menu_widgets(self):
            IdVar = tk.StringVar()
            TitleVar = tk.StringVar()
            TypeVar = tk.StringVar()
            DescripVar = tk.StringVar()
            PriceVar = tk.StringVar()
            BillVar = tk.StringVar()
            with open('bill.dat', 'wb') as f:
                pickle.dump([], f)
            
            self.BgLabel = tk.Label(self.master, image = self.bg)
            self.BgLabel.pack()

            self.BillFrame = tk.Frame(self.master)
            self.ListBill = tk.Listbox(self.BillFrame, font='Rockwell 14', width=30)
            self.scrollbar = tk.Scrollbar(self.BillFrame, orient='vertical',command=self.ListBill.yview)
            self.ListBill.config(yscrollcommand=self.scrollbar.set)
            
            self.IdLabel = tk.Label(self.master, font='Arial 12 bold', text='Product ID')
            self.IdEntry = tk.Entry(self.master, font='courier 14 bold', textvariable=IdVar)
            self.TitleLabel = tk.Label(self.master, font='Arial 12 bold', text='Title')
            self.TitleEntry = tk.Entry(self.master, font='courier 14 bold', state='readonly', textvariable=TitleVar)
            self.TypeLabel = tk.Label(self.master, font='Arial 12 bold', text='Type')
            self.TypeEntry = tk.Entry(self.master, font='courier 14 bold', state='readonly', textvariable=TypeVar)
            self.DescripLabel = tk.Label(self.master, font='Arial 12 bold', text='Description')
            self.DescripEntry = tk.Entry(self.master, font='courier 14 bold', state='readonly', textvariable=DescripVar)
            self.PriceLabel = tk.Label(self.master, font='Arial 12 bold', text='Price')
            self.PriceEntry = tk.Entry(self.master, font='courier 14 bold', state='readonly', textvariable=PriceVar)
            self.BillEntry = tk.Entry(self.master, width=7, font='courier 12', textvariable=BillVar)
            self.TotalLabel = tk.Label(self.master, font='Arial 12 bold', text='Total')
            def search_cmd():
                with open('products.json', 'r') as f:
                    json_str = ''.join(f.readlines())
                    json_dat = json.loads(json_str)
                    
                for item in json_dat:
                    if item['id'] == IdVar.get():
                        TitleVar.set(item['title'])
                        TypeVar.set(item['type'])
                        DescripVar.set(item['description'])
                        PriceVar.set(item['price'])
                            
            self.SearchBtn = tk.Button(self.master, bg='dodger blue', fg='white', font='Rockwell 12 bold', text='Search', command=search_cmd)

            def purchase():
                try:
                    with open('bill.dat', 'rb') as f:
                        arr = pickle.load(f)
                        arr.append(float(PriceVar.get()[:-2]))
                    with open('bill.dat', 'wb') as f:
                        pickle.dump(arr, f)
                except ValueError:
                    pass
                self.ListBill.insert(tk.END, f'{PriceVar.get()}   {TitleVar.get()}')

            def calc():
                with open('bill.dat', 'rb') as f:
                    arr = pickle.load(f)
                BillVar.set('{:.2f}'.format(sum(arr)))

            def clear():
                with open('bill.dat', 'wb') as f:
                    pickle.dump([], f)
                BillVar.set('')
                self.ListBill.delete(0,'end')
                
            self.PurchaseBtn = tk.Button(self.master, bg='dodger blue', fg='white', font='Rockwell 12 bold', text='Purchase', command=purchase)
            self.CalcBtn = tk.Button(self.master, bg='dodger blue', fg='white', font='Rockwell 12 bold', text='Calculate', command=calc)
            self.Clear = tk.Button(self.master, bg='dodger blue', fg='white', font='Rockwell 12 bold', text='C', command=clear)

            AdminName = tk.StringVar()
            AdminPassword = tk.StringVar()
            self.NameLabel = tk.Label(self.master, font='Rockwell 12 bold', text='Admin Name')
            self.NameLabel.place(x=250, y=150)
            self.NameEntry = tk.Entry(self.master, font='Rockwell 14', textvariable=AdminName)
            self.NameEntry.place(x=250, y=175)
            self.PassLabel = tk.Label(self.master, font='Rockwell 12 bold', text='Password')
            self.PassLabel.place(x=250, y=215)
            self.PassEntry = tk.Entry(self.master, font='Rockwell 14', textvariable=AdminPassword, show='*')
            self.PassEntry.place(x=250, y=245)
            self.LogInBtn = tk.Button(self.master, bg='dodger blue', fg='white', font='Rockwell 12 bold', text='Log In')
            def LogIn_Exit():
                with open('admin.dat', 'rb') as f:
                    log_in_data = pickle.load(f)
                    
                if AdminName.get() == log_in_data[0] and AdminPassword.get() == log_in_data[1]:
                    self.BillFrame.place(x=420, y=150)
                    self.ListBill.pack(side = 'left',fill = 'y' )
                    self.scrollbar.pack(side="right", fill="y")
                    self.IdLabel.place(x=50, y=120)
                    self.IdEntry.place(x=50,y=150)
                    self.TitleLabel.place(x=50, y=180)
                    self.TitleEntry.place(x=50,y=210)
                    self.TypeLabel.place(x=50, y=240)
                    self.TypeEntry.place(x=50,y=270)
                    self.DescripLabel.place(x=50, y=300)
                    self.DescripEntry.place(x=50,y=330)
                    self.PriceLabel.place(x=50, y=360)
                    self.PriceEntry.place(x=50,y=390)
                    self.BillEntry.place(x=550, y=380)
                    self.TotalLabel.place(x=420, y=380)
                    self.SearchBtn.place(x=290, y=145)
                    self.PurchaseBtn.place(x=150,y=420)
                    self.CalcBtn.place(x=480,y=420)
                    self.Clear.place(x=600,y=420)
                    self.LogInBtn.destroy()
                    self.NameLabel.destroy()
                    self.NameEntry.destroy()
                    self.PassLabel.destroy()
                    self.PassEntry.destroy()
            self.LogInBtn = tk.Button(self.master, bg='dodger blue', fg='white', font='Rockwell 12 bold', text='Log In', command= lambda : (LogIn_Exit()))
            self.LogInBtn.place(x=320, y=280)
            
    menu = App()
    menu.settings()
    menu.menu_widgets()
    tk.mainloop()

BillingMenu()
