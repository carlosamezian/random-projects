from tkinter import *
# Needed to add images.
from PIL import ImageTk, Image

root = Tk()
root.title("This Title")
# Use .ico to change app icon.
root.iconbitmap("Icon.ico")
# This step to convert the iamage.
my_image = ImageTk.PhotoImage(Image.open("Icon2.png"))
# Displaying the image.
img = Label(image=my_image)
img.pack()

quit_button = Button(root, text="Quit", command=root.quit)
quit_button.pack()
root.mainloop()
