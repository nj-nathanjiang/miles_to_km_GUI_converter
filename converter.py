from tkinter import *


def calculate():
    num_kilometers = round(float(miles_entry.get()) * 1.609)
    km_label.config(text=num_kilometers)


screen = Tk()
screen.title("Mile to Km Converter")

invisible_label_0_0 = Label(text="")
invisible_label_0_0.grid(column=0, row=0)

miles_entry = Entry(width=5)
miles_entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

km_label = Label(text="0")
km_label.grid(column=1, row=1)

km_sign = Label(text="Km")
km_sign.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)
screen.mainloop()
