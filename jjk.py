from tkinter import  *
window = Tk()
window.geometry('800x500')
names = Frame()
names.pack(fill='x')
window.configure(bg='black')
hero_name = Label(names,text="Hero", font=('',15))
hero_name.pack(side=LEFT, pady=10, padx=10)
hero_live = Label(names, text="00", font=('', 15))  # Match background for a consistent look
hero_live.pack(side=LEFT, pady=10)


villain_name = Label(names, text="Villain", font=('',15))
villain_name.pack(side=RIGHT, padx=60, pady=10)
villain_name = Label(names, text="00", font=('',15))
villain_name.place(x=750, y=10)

window.mainloop()