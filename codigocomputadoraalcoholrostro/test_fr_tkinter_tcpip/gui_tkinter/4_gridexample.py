from tkinter import ttk
import tkinter as tk
from windows import improveimagequality


def greet():
    # The get() method is used to fetch the value of a StringVar() instance.
    # If user_name is empty, print Hello, World!
    print(f"Hello, {user_name.get() or 'World'}!")

improveimagequality()
root = tk.Tk()
root.title("Greeter")
root.columnconfigure(0, weight=1)
# Here we create an instances of the StringVar() class, which is to track the content of widgets
user_name = tk.StringVar()

# We define two frames to keep the input on different lines. In the next version we will switch to grid() geometry.
# Padding accepts a tuple of up to four values. Clockwise like CSS.
#   first grid - (0, 0)

input_frame = ttk.Frame(root, padding=(20, 20, 20, 10))
input_frame.columnconfigure(0, weight=1)
input_frame.columnconfigure(1, weight=1)
input_frame.grid(row=0, column=0, sticky="EW")

name_label = ttk.Label(input_frame, text="Hola", background="blue", foreground="white")
name_label.grid(row=0, column=0, sticky="EW")
name_entry = ttk.Entry(input_frame, textvariable=user_name)
name_entry.grid(row=0, column=1, sticky="EW")
name_entry.focus()

#   second grid - (1, 0)
buttons = ttk.Frame(root, padding=(20, 0, 20, 10))
buttons.grid(row=1, column=0, sticky="EW")
buttons.columnconfigure(0, weight=1)
buttons.columnconfigure(1, weight=1)

greet_button = ttk.Button(buttons, text="Greet", command=greet)
greet_button.grid(row=0, column=0)

quit_button = ttk.Button(buttons, text="Quit", command=root.destroy)
quit_button.grid(row=0, column=1)


root.mainloop()