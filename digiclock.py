from tkinter import *
from tkinter.ttk import *
from time import strftime

def close_window(event):
    root.destroy()

root = Tk()
root.attributes("-fullscreen", True)
root.configure(bg='black')
root.bind('<Escape>', close_window)  # Bind the 'Escape' key to close the window

root.title('Clock')

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

lbl = Label(root, font=('calibri', 120, 'bold'), background='black', foreground='white')  # Increase font size
lbl.pack(expand=True)

time()
root.mainloop()

