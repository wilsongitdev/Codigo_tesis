import tkinter as tk
from tkinter import ttk


def greet():
    # The get() method is used to fetch the value of a StringVar() instance.
    # If user_name is empty, print Hello, World!
    print(f"Hello, {user_name.get() or 'World'}!")


root = tk.Tk()
root.title("Greeter")
root.geometry("400x200")
# Here we create an instances of the StringVar() class, which is to track the content of widgets
user_name = tk.StringVar()

# We define two frames to keep the input on different lines. In the next version we will switch to grid() geometry.
# Padding accepts a tuple of up to four values. Clockwise like CSS.
input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
input_frame.pack(fill="both")

name_label = ttk.Label(input_frame, text="Hola", background="blue", foreground="white")
name_label.pack(side="both",fill="x", expand=True)
# name_label = ttk.Entry(input_frame, text="Hola", background="red", foreground="white")
# name_label.pack(side="left",fill="x", expand=True)
name_entry = ttk.Entry(input_frame, textvariable=user_name)
name_entry.pack(side="right", expand=True)
name_entry.focus()

buttons = ttk.Frame(root, padding=(20, 10))
buttons.pack(fill="both")

greet_button = ttk.Button(buttons, text="Greet", command=greet)
greet_button.pack(side="left", fill="x", expand=True)
quit_button = ttk.Button(buttons, text="Quit", command=root.destroy)
quit_button.pack(side="right", fill="x", expand=True)

root.mainloop()