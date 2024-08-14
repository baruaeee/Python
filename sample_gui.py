from tkinter import *
window = Tk()

window.title("WVis")
window.geometry('350x200')

lbl = Label(window, text = "Asset Data", font=("Arial Bold", 15))
lbl.grid(column=0, row=0)

txt = Entry(window, width = 10)
txt.grid(column=2, row=3)

def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text=res)

btn = Button(window, text = "Add", command=clicked)
## btn = Button(window, text = "Add", state = 'disabled')
btn.grid(column=3, row=3)

window.mainloop()