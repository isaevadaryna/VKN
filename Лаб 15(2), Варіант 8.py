from tkinter import *
root = Tk()
root.geometry('300x300')
root['bg'] = 'grey'
#frame
frame = Frame(root, bg='black')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)
def btn_click():
    num = int(a.get())
    num2 = int(b.get())
    num2 = num2 + num
    num3 = num2 /2
    txt.insert(0.0, ("\nCума: ",num2))
    txt.insert(0.0, ("Середне арифметичне: ", num3))
#event
a = StringVar()
b =StringVar()
mas = Entry(frame,width=37,textvariable=a, bg='white')
mas1 = Entry(frame,width=37,textvariable=b, bg='white')
btn = Button(frame, text='Розрахувати', bg= 'white', command=btn_click)
global txt
txt = Text(frame, width=25, height=9, wrap=WORD)
mas.pack(pady=3)
mas1.pack()
btn.pack(pady=3)
txt.pack(pady=3)

root.mainloop()