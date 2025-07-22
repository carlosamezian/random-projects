from tkinter import *
from typing import Match
"""My version of a calculator
"""

root = Tk()
root.title("Calulator")

entry1 = Entry(root, width=35, borderwidth=5)
entry1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(num):
    """
    This adds numbers from buttons.
    """
    # entry1.delete(0, END)
    temp = entry1.get()
    entry1.delete(0, END)
    entry1.insert(0, str(temp) + str(num))


def button_clear():
    """
    This clears the screen.
    """
    entry1.delete(0, END)


def button_add():
    """
    This adds the inputs
    """
    first_num = entry1.get()
    global first_number
    global math
    math = "addition"
    first_number = int(first_num)
    entry1.delete(0, END)


def button_equal():
    """
    This combines both numbers to give a total.
    """
    second_num = entry1.get()
    entry1.delete(0, END)

    if math == "addition":
        entry1.insert(0, first_number + int(second_num))
    if math == "subtract":
        entry1.insert(0, first_number + int(second_num))
    if math == "multiply":
        entry1.insert(0, first_number * int(second_num))
    if math == "divide":
        entry1.insert(0, first_number / int(second_num))


def button_subtract():
    """
    This subtracts the buttons
    """
    first_num = entry1.get()
    global first_number
    global math
    math = "substract"
    first_number = int(first_num)
    entry1.delete(0, END)


def button_multiply():
    """
    Multiplication part.
    """
    first_num = entry1.get()
    global first_number
    global math
    math = "multiply"
    first_number = int(first_num)
    entry1.delete(0, END)


def button_divide():
    """
    Division part.
    """
    first_num = entry1.get()
    global first_number
    global math
    math = "divide"
    first_number = int(first_num)
    entry1.delete(0, END)


# Creating the buttons
butt1 = Button(root, text="1", padx=40, pady=20,
               bg="white", command=lambda: button_click(1))
butt2 = Button(root, text="2", padx=40, pady=20,
               bg="white", command=lambda: button_click(2))
butt3 = Button(root, text="3", padx=40, pady=20,
               bg="white", command=lambda: button_click(3))
butt4 = Button(root, text="4", padx=40, pady=20,
               bg="white", command=lambda: button_click(4))
butt5 = Button(root, text="5", padx=40, pady=20,
               bg="white", command=lambda: button_click(5))
butt5 = Button(root, text="5", padx=40, pady=20,
               bg="white", command=lambda: button_click(5))
butt6 = Button(root, text="6", padx=40, pady=20,
               bg="white", command=lambda: button_click(6))
butt7 = Button(root, text="7", padx=40, pady=20,
               bg="white", command=lambda: button_click(7))
butt8 = Button(root, text="8", padx=40, pady=20,
               bg="white", command=lambda: button_click(8))
butt9 = Button(root, text="9", padx=40, pady=20,
               bg="white", command=lambda: button_click(9))
butt0 = Button(root, text="0", padx=40, pady=20,
               bg="white", command=lambda: button_click(0))
add_button = Button(root, text="+", padx=39, pady=20,
                    bg="white", command=button_add)
equal_button = Button(root, text="=", padx=91, pady=20,
                      bg="white", command=button_equal)
clear_button = Button(root, text="CE", padx=80, pady=20,
                      bg="white", command=button_clear)
subtract_button = Button(root, text="-", padx=41, pady=20,
                         bg="white", command=button_subtract)
multiply_button = Button(root, text="*", padx=40, pady=20,
                         bg="white", command=button_multiply)
divide_button = Button(root, text="/", padx=41, pady=20,
                       bg="white", command=button_divide)


# Putting buttons on the screen
butt1.grid(row=3, column=0)
butt2.grid(row=3, column=1)
butt3.grid(row=3, column=2)

butt4.grid(row=2, column=0)
butt5.grid(row=2, column=1)
butt6.grid(row=2, column=2)

butt7.grid(row=1, column=0)
butt8.grid(row=1, column=1)
butt9.grid(row=1, column=2)

butt0.grid(row=4, column=0)
clear_button.grid(row=4, column=1, columnspan=2)

add_button.grid(row=5, column=0)
equal_button.grid(row=5, column=1, columnspan=2)
subtract_button.grid(row=6, column=0)
multiply_button.grid(row=6, column=1)
divide_button.grid(row=6, column=2)

# The main loop for the GUI
root.mainloop()
