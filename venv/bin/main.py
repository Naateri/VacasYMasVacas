from tkinter import *
#from PIL import ImageTk, Image
#import Image, ImageTk
#import PIL
import login

root = Tk()
path = "/home/nateri/PycharmProjects/VacasYMasVacas/venv/images/vaquitas.jpg"
img = PhotoImage(path)
my_canvas = Canvas(root,bg="blue", height=300, width=300)
background_label = Label(root, image = img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
my_canvas.place()

login.create_login(root)
root.mainloop()