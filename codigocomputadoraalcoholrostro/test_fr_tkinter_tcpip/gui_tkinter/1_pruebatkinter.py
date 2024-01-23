import tkinter as tk # tk is a set of editable widgets
from tkinter import ttk

def click():
    print("Hola mundo")

root = tk.Tk() #tk object is the main windows of the application

label=ttk.Label(root, text="Nombre: ",padding=(0, 10))
label.pack(side="left", padx= (0, 10))

button1 = ttk.Button(root, text="Acción", command=click)
button1.pack(side="left",fill="both", expand=True) #expand- ask the window for more space


button2 = ttk.Button(root, text="Salir", command=root.destroy)
button2.pack(side="left")
root.mainloop()

