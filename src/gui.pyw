from tkinter import *
from tkinter import ttk  
from tkinter.colorchooser import askcolor 
from tdge import *
from tkinter.ttk import Radiobutton
from tkinter import filedialog

def new_object():
	icn = Label(tab2, text="Name of the object", font=("Arial Bold", 10))
	icn.place(x=8, y=20)

	size = Label(tab2, text="Size", font=("Arial Bold", 10))
	size.place(x=43, y=70)

	aw = Label(tab2, text="a", font=("Arial Bold", 10))
	aw.place(x=29, y=110)

	global a
	a = Entry(tab2, width=3)
	a.place(x=25, y=95)

	bw = Label(tab2, text="b", font=("Arial Bold", 10))
	bw.place(x=59, y=110)

	global b
	b = Entry(tab2, width=3)
	b.place(x=55, y=95)

	cw = Label(tab2, text="c", font=("Arial Bold", 10))
	cw.place(x=89, y=110)

	global c
	c = Entry(tab2, width=3)
	c.place(x=85, y=95)

	nameOO = Entry(tab2, width=15)
	nameOO.place(x=18, y=45)

	typeCUBE = Radiobutton(tab1, text='Color bg', value=1, command=typechuz)  
	typeCUBE.place(x=20, y=200)

def resizable3():
	pass

def color_bg():
	global true
	true = "image"
	global result
	result = askcolor(title = "Choose color")
	print(result[1])

def image_bg():
	global true
	true = "picture"
	global file
	file = filedialog.askopenfilename()

def clicked():
	name = title.get()
	height = hei.get()
	width = wid.get()
	global game
	txt = Entry(window, width=10)
	game = Game(resizable=True if resizable3 else False, movement=True, height=int(height), width=int(width), title=(name))
	if true == "image":
		display.set_background(game, background_type="color", color=list(hex_to_rgb(result[1])))
		if new_object:
			pass
		else:
			pass
	elif true == "picture":
		display.set_background(game, background_type="image", image_path=file)
		if new_object:
			pass
		else:
			pass

window = Tk()  
window.title("3D Game Engine")  
window.geometry('500x350')

tab_control = ttk.Notebook(window)  

tab1 = ttk.Frame(tab_control)  
tab2 = ttk.Frame(tab_control) 

tab_control.add(tab1, text='Window')  
tab_control.add(tab2, text='Objects') 

name = Label(tab1, text="3D Game Engine", font=("Arial Bold", 30))
name.place(x=50, y=5)

color = Radiobutton(tab1, text='Color bg', value=1, command=color_bg)  
color.place(x=20, y=200)

image = Radiobutton(tab1, text='Picture bg', value=2, command=image_bg) 
image.place(x=20, y=220)

titletext = Label(tab1, text="Project title", font=("Arial Bold", 10))
titletext.place(x=22, y=62)

title = Entry(tab1, width=15)  
title.place(x=10, y=85)

resizable_btn = Radiobutton(tab1, text='Resizible', value=3, command=resizable3) 
resizable_btn.place(x=20, y=260)

wid = Entry(tab1, width=8)  
wid.place(x=12, y=166.5)

widtext = Label(tab1, text="width", font=("Arial Bold", 10))
widtext.place(x=67, y=165)


hei = Entry(tab1, width=8)
hei.place(x=12, y=141.5)

heitext = Label(tab1, text="height", font=("Arial Bold", 10))
heitext.place(x=67, y=140)

btn = Button(tab1, text="Start", command=clicked)  
btn.place(x=210, y=280)


btnNC = Button(tab2, text="New Object", command=new_object)
btnNC.place(x=190, y=280)


lbl12 = Label(tab1, text="Window size", font=("Arial Bold", 10))
lbl12.place(x=17, y=115)

txt = Entry(tab1, width=10, state='disabled')

tab_control.pack(expand=1, fill='both')

window.mainloop()