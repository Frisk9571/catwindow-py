
# Import tkinter (GUI maker)
from tkinter import *

# Import PIL(low) 
from PIL import ImageTk, Image

# Import HTTP(S) lib
import requests
 
# create root window
root = Tk()
 
# root window title and dimension
root.title("cat")
# Set geometry (widthxheight)
root.geometry('400x400')

#adding a label to the root window
label = Label(root, text = "")
label.pack(side=BOTTOM)
[]

catpath = "res/images.png"
response = requests.get("https://cataas.com/cat")
if response.status_code == 200:
    # save cat
    with open("res/downloaded.jpeg", "wb") as f:
        f.write(response.content)
    catpath = "res/downloaded.jpeg"

# use catpath as your file name
cat = Image.open(catpath).resize((250,250))
initcat = ImageTk.PhotoImage(cat)
importcat = Label(image=initcat)

# function to display text when
# button is clicked
def clicked():
    label.configure(text = "cat my beloved")
    importcat.place(relx=0.5, rely=0.5, anchor=CENTER)

 
# button get
button = Button(root, text = "click to cat" ,
             fg = "black", command=clicked)


# place buttons
button.place(relx=0.5, rely=0.05, anchor=CENTER)
label.place(relx=0.5, rely=0.95, anchor=CENTER)
 
 
# all widgets will be here
# Execute Tkinter
root.mainloop()