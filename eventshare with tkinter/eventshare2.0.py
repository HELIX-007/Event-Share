from tkinter import*
from tkinter.ttk import*
import time

window=Tk()
window.geometry('800x600')
logo=PhotoImage(file='logo.png')
Label(window,text='',image=logo).pack(pady=120)

Lbar=Progressbar(window,orient = HORIZONTAL,length=300,mode='determinate')

def loading():
    for i in range(0,310,10):
        
        Lbar['value']=i
        window.update_idletasks()
        time.sleep(0.3)
        Lbar.place(x=260,y=300)
    
Button(window,text='Go!',width=5,command=loading).place(x=500,y=250)

mainloop()
