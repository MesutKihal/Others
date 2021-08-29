from tkinter import *
import random

class App:
	def __init__(self, master = Tk()):
		self.master = master

	def settings(self):
		self.master.geometry('280x350')
		self.master.minsize(280,350)
		self.master.maxsize(280,350)
		self.master.title('TicTacToe')
		self.master.iconbitmap('icon.ico')
		self.master.configure(bg='black')

	def widgets(self):
		#Variables
		self.symbol = StringVar()
		self.onevar = StringVar()
		self.twovar = StringVar()
		self.threevar = StringVar()
		self.fourvar = StringVar()
		self.fivevar = StringVar()
		self.sixvar = StringVar()
		self.sevenvar = StringVar()
		self.eightvar = StringVar()
		self.ninevar = StringVar()
		self.rsvar = StringVar()
		self.symbol.set(random.choice(['X turn','O turn']))

		self.result = Label(textvariable = self.rsvar,fg='black',bg='coral1',font='raavi 21 bold',width=18).place(x = 0, y = 0)
		self.turn = Label(textvariable= self.symbol,fg='white',bg='cyan4', font='courier 21 bold',width=17).place(x = 0, y = 315)
		def reset_it():
			table = [self.onevar,self.twovar,self.threevar,
					 self.fourvar,self.fivevar,self.sixvar,
					 self.sevenvar,self.eightvar,self.ninevar,]
			for var in table:
				var.set('')
			self.symbol.set(random.choice(['X turn','O turn']))
			self.rsvar.set('')
		def check():
			gameover = False
			table = [str(self.onevar.get()),str(self.twovar.get()),str(self.threevar.get()),
					 str(self.fourvar.get()),str(self.fivevar.get()),str(self.sixvar.get()),
					 str(self.sevenvar.get()),str(self.eightvar.get()),str(self.ninevar.get()),]
			if not gameover and str(self.rsvar.get()) == '':
				#1st_row
				if str(self.onevar.get())+str(self.twovar.get())+str(self.threevar.get()) == 'OOO':
					self.rsvar.set('  O Victory!!')
					gameover = True
				elif str(self.onevar.get())+str(self.twovar.get())+str(self.threevar.get()) == 'XXX':
					self.rsvar.set('  X Victory!!')
					gameover = True
				#2nd_row
				if str(self.fourvar.get())+str(self.fivevar.get())+str(self.sixvar.get()) == 'OOO':
					self.rsvar.set('  O Victory!!')
					gameover = True
				elif str(self.fourvar.get())+str(self.fivevar.get())+str(self.sixvar.get()) == 'XXX':
					self.rsvar.set('  X Victory!!')
					gameover = True
				#3rd_row
				if str(self.sevenvar.get())+str(self.eightvar.get())+str(self.ninevar.get()) == 'OOO':
					self.rsvar.set('  O Victory!!')
					gameover = True
				elif str(self.sevenvar.get())+str(self.eightvar.get())+str(self.ninevar.get()) == 'XXX':
					self.rsvar.set('  X Victory!!')
					gameover = True
				#1st_column
				if str(self.onevar.get())+str(self.fourvar.get())+str(self.sevenvar.get()) == 'OOO':
					self.rsvar.set('  O Victory!!')
					gameover = True
				elif str(self.onevar.get())+str(self.fourvar.get())+str(self.sevenvar.get()) == 'XXX':
					self.rsvar.set('  X Victory!!')
					gameover = True
				#2nd_column
				if str(self.twovar.get())+str(self.fivevar.get())+str(self.eightvar.get()) == 'OOO':
					self.rsvar.set('  O Victory!!')
					gameover = True
				elif str(self.twovar.get())+str(self.fivevar.get())+str(self.eightvar.get()) == 'XXX':
					self.rsvar.set('  X Victory!!')
					gameover = True
				#3rd_column
				if str(self.threevar.get())+str(self.sixvar.get())+str(self.ninevar.get()) == 'OOO':
					self.rsvar.set('  O Victory!!')
					gameover = True
				elif str(self.threevar.get())+str(self.sixvar.get())+str(self.ninevar.get()) == 'XXX':
					self.rsvar.set('  X Victory!!')
					gameover = True
				#1st_diagnol
				if str(self.onevar.get())+str(self.fivevar.get())+str(self.ninevar.get()) == 'OOO':
					self.rsvar.set('  O Victory!!')
					gameover = True
				elif str(self.onevar.get())+str(self.fivevar.get())+str(self.ninevar.get()) == 'XXX':
					self.rsvar.set('  X Victory!!')
					gameover = True
				#2nd_diagnol
				if str(self.threevar.get())+str(self.fivevar.get())+str(self.sevenvar.get()) == 'OOO':
					self.rsvar.set('  O Victory!!')
					gameover = True
				elif str(self.threevar.get())+str(self.fivevar.get())+str(self.sevenvar.get()) == 'XXX':
					self.rsvar.set('  X Victory!!')
					gameover = True
			if all(txt for txt in table if txt == '') and not gameover and str(self.rsvar.get()) == '':
				self.rsvar.set('Draw')

		def change_var(txtvar):
			if str(txtvar.get()) == '':
				txtvar.set(f'{str(self.symbol.get())[0]}')
				if str(self.symbol.get()) == 'X turn':
					self.symbol.set('O turn')
				else:
					self.symbol.set('X turn')
		#Widgets
		self.reset = Button(text='⟳',fg='white',bg='black',font='rod 24',command=reset_it).place(x=0,y=0)
		#1st_row
		self.one = Button(textvariable=self.onevar,bg='lavender',fg='black', font='raavi 20 bold',width=5,command=lambda :(change_var(self.onevar),check())).place(x=10,y=60)
		self.two = Button(textvariable=self.twovar,bg='lavender',fg='black', font='raavi 20 bold',width=5,command=lambda :(change_var(self.twovar),check())).place(x=100,y=60)
		self.three = Button(textvariable=self.threevar,bg='lavender',fg='black', font='raavi 20 bold',width=5,command=lambda :(change_var(self.threevar),check())).place(x=190,y=60)
		#2nd_row
		self.four = Button(textvariable=self.fourvar,bg='lavender',fg='black', font='raavi 20 bold',width=5,command=lambda :(change_var(self.fourvar),check())).place(x=10,y=145)
		self.five = Button(textvariable=self.fivevar,bg='lavender',fg='black', font='raavi 20 bold',width=5,command=lambda :(change_var(self.fivevar),check())).place(x=100,y=145)
		self.six = Button(textvariable=self.sixvar,bg='lavender',fg='black', font='raavi 20 bold',width=5,command=lambda :(change_var(self.sixvar),check())).place(x=190,y=145)
		#3rd_row
		self.seven = Button(textvariable=self.sevenvar,bg='lavender',fg='black', font='raavi 20 bold',width=5,command=lambda :(change_var(self.sevenvar),check())).place(x=10,y=230)
		self.eight = Button(textvariable=self.eightvar,bg='lavender',fg='black', font='raavi 20 bold',width=5,command=lambda :(change_var(self.eightvar),check())).place(x=100,y=230)
		self.nine = Button(textvariable=self.ninevar,bg='lavender',fg='black', font='raavi 20 bold',width=5,command=lambda :(change_var(self.ninevar),check())).place(x=190,y=230)
ttt = App()
ttt.settings()
ttt.widgets()
mainloop()