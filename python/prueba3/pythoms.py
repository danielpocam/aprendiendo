from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry("1000x800")
frm = ttk.Frame(root, borderwidth=2, relief=SUNKEN)
frm.pack(side=TOP, fill="x")

frm.picture=PhotoImage(file=r"C:\Users\danie\Pictures\mapa 2.png")
frm.label = Label(frm, image=frm.picture)
frm.label.pack()
#frm.picture=PhotoImage(file=r"C:\Users\danie\OneDrive\Imágenes\Álbum de cámara\WIN_20220921_20_47_36_Pro.jpg")
#ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
