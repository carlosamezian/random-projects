from tkinter import *
'''
In this program I'll be working with Tkinter.
'''


#Base for GUI
root = Tk()

#############
#Creating label widget and packing it to display on screeen.

# labelwid1 = Label(root, text="Hello World")
# labelwid1.pack()
    
#############
# Using .grid()

# labelwid1 = Label(root, text="Hellow World")
# labelwid2 = Label(root, text="This is a random sentence.")

# labelwid1.grid(row=0, column=0)
# labelwid2.grid(row=2, column=23)

#############
#Working with Button()
#state=DISABLED
#fg= and bg= changes color

# def clicker():
#     mylabel = Label(root, text="Clicked Button!")
#     mylabel.pack()
    
# myButtonwid1 = Button(root, text="Button 1", padx=5, pady=10, fg="lightblue", bg="cyan",command=clicker)
# myButtonwid1.pack()

#############
#Input Boxes

entrywid1 =  Entry(root, bg="lightblue", width=50, fg="black", borderwidth=3)
entrywid1.pack()
entrywid1.insert(0, "Enter text:    ")
def clicker():
    label1 = Label(root, text=entrywid1.get())
    label1.pack()

myButtonwid1 = Button(root, text="Enter", command=clicker)
myButtonwid1.pack()



#############

root.mainloop()
