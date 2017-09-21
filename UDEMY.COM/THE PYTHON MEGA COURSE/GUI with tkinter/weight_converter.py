from tkinter import *


def kg_to_imperial():
    weight = float(e1_value.get())
    grams = weight * 1000
    pounds = weight * 2.20462
    ounces = weight * 35.274
    t1.insert(END, grams)
    t2.insert(END, pounds)
    t3.insert(END, ounces)




window = Tk()

# Labels
l1 = Label(window, text="{0:4^}".format("Kg"))
l1.grid(row=0, column=0)

l2 = Label(window, text="Grams")
l2.grid(row=1, column=0)

l3 = Label(window, text="Pounds")
l3.grid(row=1, column=1)

l4 = Label(window, text="Ounces")
l4.grid(row=1, column=2)

# Entries

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

# Buttons

b1 = Button(window, text="Convert", command=kg_to_imperial)
b1.grid(row=0, column=2)

# Text fields

# grams
t_width = 9
t1 = Text(window, height=1, width=t_width)
t1.grid(row=2, column=0)

# pounds
t2 = Text(window, height=1, width=t_width)
t2.grid(row=2, column=1)

# ounces
t3 = Text(window, height=1, width=t_width)
t3.grid(row=2, column=2)



window.mainloop()