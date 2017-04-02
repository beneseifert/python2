import tkinter
import tkinter.messagebox as messagebox

top = tkinter.Tk()

def hello_callback():
    messagebox.showinfo("Hello Python", "Hello World")

B = tkinter.Button(top, text="Hello", command = hello_callback)

B.pack()

top.mainloop()