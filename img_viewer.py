from os import stat
from tkinter import *
# Needed to add images.
from PIL import ImageTk, Image

root = Tk()
root.title("This Title")
# Use .ico to change app icon.
root.iconbitmap("Icon.ico")
# This step to convert the iamage.
my_image1 = ImageTk.PhotoImage(Image.open("sample/pepeglasses.png"))
my_image2 = ImageTk.PhotoImage(Image.open("sample/PepeHands.png"))
my_image3 = ImageTk.PhotoImage(Image.open("sample/PepeHappy.png"))
my_image4 = ImageTk.PhotoImage(Image.open("sample/pepeHug.png"))
my_image5 = ImageTk.PhotoImage(Image.open("sample/pepehype.png"))
my_image6 = ImageTk.PhotoImage(Image.open("sample/PepeKMS.png"))
my_image7 = ImageTk.PhotoImage(Image.open("sample/pepeOK.png"))

img_list = [my_image1, my_image2, my_image3, my_image4, my_image5, my_image6, my_image7]

#Creating Forward and Back buttons
def forward(img_num):
    global img_label
    global forward_button
    global back_button
    
    img_label.grid_forget()
    img_label = Label(image=img_list[img_num-1])
    img_label.grid(row=0, column=0, columnspan=3)
    forward_button = Button(root, text=">>Forward>>", command=lambda: forward(img_num + 1))
    back_button = Button(root, text="<<Back<<", command=lambda: back(img_num-1))
    
    if img_num == len(img_list):
        forward_button = Button(root, text=">>Forward>>", state=DISABLED)
    
    back_button.grid(row=1, column=0)
    forward_button.grid(row=1, column=2)

def back(img_num):
    global img_label
    global forward_button
    global back_button
    
    img_label.grid_forget()
    img_label = Label(image=img_list[img_num-1])
    img_label.grid(row=0, column=0, columnspan=3)
    forward_button = Button(root, text=">>Forward>>", command=lambda: forward(img_num + 1))
    back_button = Button(root, text="<<Back<<", command=lambda: back(img_num-1))
    
    if img_num == 1:
        back_button = Button(root, text="<<Back<<", command=back, state=DISABLED)
    
    back_button.grid(row=1, column=0)
    forward_button.grid(row=1, column=2)

# Displaying the image.
img_label = Label(image=my_image1)
img_label.grid(row=0, column=0, columnspan=3)

back_button = Button(root, text="<<Back<<", command=back, state=DISABLED)
forward_button = Button(root, text=">>Forward>>", command=lambda: forward(2))
quit_button = Button(root, text="Quit", command=root.quit)

back_button.grid(row=1, column=0)
quit_button.grid(row=1, column=1)
forward_button.grid(row=1, column=2)

root.mainloop()
