from tkinter import *
# "import Image
# import PIL
import login

root = Tk()
#test = Tk()
#path = "venv/images/vaquitas.jpg"
#le_img = Image(path)
#img = PhotoImage(le_img)
#my_canvas = Canvas(test,bg="blue", height=300, width=300)
#background_label = Label(test, image = img)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)
#my_canvas.place()

login.create_login(root)
root.mainloop()
#test.mainloop()