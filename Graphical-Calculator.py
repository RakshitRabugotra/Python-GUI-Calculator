import os
from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Calculator")
root.geometry('320x568')
root.resizable(0, 0)

main = PhotoImage(file='src\\images\\calc.png')

plus = PhotoImage(file='src\\images\\buttons\\plus-filled.png')
minus = PhotoImage(file='src\\images\\buttons\\minus-filled.png')
multiply = PhotoImage(file='src\\images\\buttons\\multiply-filled.png')
divide = PhotoImage(file='src\\images\\buttons\\divide-filled.png')
sign_change = PhotoImage(file='src\\images\\buttons\\+.- filled.png')
clear = PhotoImage(file='src\\images\\buttons\\clear-filled.png')
percent = PhotoImage(file='src\\images\\buttons\\percent-filled.png')
period = PhotoImage(file='src\\images\\buttons\\period-filled.png')
equal = PhotoImage(file='src\\images\\buttons\\equal-filled.png')

n0 = PhotoImage(file='src\\images\\buttons\\numeric\\0.png')
n1 = PhotoImage(file='src\\images\\buttons\\numeric\\1.png')
n2 = PhotoImage(file='src\\images\\buttons\\numeric\\2.png')
n3 = PhotoImage(file='src\\images\\buttons\\numeric\\3.png')
n4 = PhotoImage(file='src\\images\\buttons\\numeric\\4.png')
n5 = PhotoImage(file='src\\images\\buttons\\numeric\\5.png')
n6 = PhotoImage(file='src\\images\\buttons\\numeric\\6.png')
n7 = PhotoImage(file='src\\images\\buttons\\numeric\\7.png')
n8 = PhotoImage(file='src\\images\\buttons\\numeric\\8.png')
n9 = PhotoImage(file='src\\images\\buttons\\numeric\\9.png')

Label(root, image=main).pack()

var = StringVar()
var.set('0')

exp = ""

Label(root, text=' Made By Rakshit Rabugotra', bg='#000', borderwidth=0, font=('Rockwell', 18), fg='#fff').place(x=1, y=11)
Label(root, text='___________________________', bg='#000', borderwidth=0, font=('Rockwell', 18), fg='#fff').place(x=1, y=38)

e = Entry(root, bg='#000', borderwidth=0, relief='groove', font=('Rockwell',45), text='0', fg='#fff')
e.place(x=5, y=90)
e['textvariable'] = var

def all_clear(event=None):
	e.delete(0, END)
	e.insert(0, '0')


def num(number):
	global exp, var

	if var.get() == '0':
		var.set('')
	if exp == '0':
		exp = ''

	exp += str(number)
	var.set(var.get()+str(number))


def num_(event):
	global exp, var

	if event.char in ('+', '-', '/', '*', '.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
		number = event.char

		if var.get() == '0':
			var.set('')
		if exp == '0':
			exp = ""

		exp += str(number)
		var.set(var.get()+str(number))

	elif event.char == '%':
		Percent()


def SignChange(event):
	global exp, var

	if var.get().isnumeric():
		var.set(str(-float(var.get())))
		exp = str(var.get())
	elif len(var.get().split('-')) == 2:
		try:
			temp = float(var.get().split('-')[-1])
			var.set(str(temp))
			exp = str(temp)
		except Exception as e:
			print('ERROR: {}'.format(e))
			var.set('Error')
			exp = ""
	else:
		var.set('Error')
		exp = ""


def evaluate(event):
	global var, exp

	if exp == '' or var.get() == 'Error':
		exp = ''
		var.set('0')

	try:
		exp = str(eval(exp))
		var.set(str(exp))

	except Exception as e:
		print('ERROR: {}'.format(e))
		var.set('Error')
		exp = ""

def backspace(event):
	global var, exp

	if len(var.get()) == 0 or var.get() == '0':
		all_clear()
	else:
		try:
			temp = [i for i in exp]
			temp.pop()

			exp = ''.join(temp)
			var.set(str(exp))

			if len(var.get()) == 0:
				all_clear()

		except Exception as e:
			print('ERROR: {}'.format(e))
			var.set('Error')
			exp = ""

def Percent():
	global var, exp

	try:
		exp = str(eval(exp))
		exp = str(float(exp)/100)

		var.set(str(exp))
	except Exception as e:
		print('ERROR: {}'.format(e))
		var.set('Error')
		exp = ""


Button(root, width=38, height=38, borderwidth=0, image=clear, command=lambda: backspace(event=None)).place(x=23, y=194)
Button(root, width=34, height=34, borderwidth=0, image=sign_change, command=lambda: SignChange(event=None)).place(x=103, y=196)
Button(root, width=34, height=34, borderwidth=0, image=percent, command=Percent).place(x=180, y=195)
Button(root, width=34, height=34, borderwidth=0, image=divide, command=lambda: num(number='/')).place(x=258, y=197)

Button(root, width=34, height=34, borderwidth=0, image=n7, command=lambda: num(number=7)).place(x=25, y=273)
Button(root, width=34, height=34, borderwidth=0, image=n8, command=lambda: num(number=8)).place(x=103, y=273)
Button(root, width=34, height=34, borderwidth=0, image=n9, command=lambda: num(number=9)).place(x=180, y=273)
Button(root, width=34, height=34, borderwidth=0, image=multiply, command=lambda: num(number='*')).place(x=258, y=273)

Button(root, width=34, height=34, borderwidth=0, image=n4, command=lambda: num(number=4)).place(x=25, y=351)
Button(root, width=34, height=34, borderwidth=0, image=n5, command=lambda: num(number=5)).place(x=103, y=351)
Button(root, width=34, height=34, borderwidth=0, image=n6, command=lambda: num(number=6)).place(x=181, y=351)
Button(root, width=28, height=28, borderwidth=0, image=minus, command=lambda: num(number='-')).place(x=261, y=354)

Button(root, width=34, height=34, borderwidth=0, image=n1, command=lambda: num(number=1)).place(x=25, y=428)
Button(root, width=34, height=34, borderwidth=0, image=n2, command=lambda: num(number=2)).place(x=103, y=428)
Button(root, width=34, height=34, borderwidth=0, image=n3, command=lambda: num(number=3)).place(x=181, y=428)
Button(root, width=28, height=28, borderwidth=0, image=plus, command=lambda: num(number='+')).place(x=261, y=431)

Button(root, width=34, height=34, borderwidth=0, image=n0, command=lambda: num(number=0)).place(x=25, y=505) # 17,2
Button(root, width=20, height=20, borderwidth=0, image=period, command=lambda: num(number='.')).place(x=188, y=522)
Button(root, width=34, height=34, borderwidth=0, image=equal, command=lambda: evaluate(event=None)).place(x=257, y=507)

def press(event):
	print('Right Click')

root.bind('<Return>', evaluate)
root.bind('<Key>', num_)
root.bind('<BackSpace>', backspace)
root.bind('<Escape>', all_clear)
e.bind('<Button-3>', press)

if __name__ == '__main__':
	root.mainloop()
