#import modules
import random
from tkinter import messagebox
from tkinter import *

#password generator function
def generate_password():
 try:
   repeat = int(repeat_entry.get())
   length = int(length_entry.get())
 except:
   messagebox.showerror(message="Please key in the required inputs")
   return
 #Check if user allows repetition of characters
 if repeat == 1:
   password = random.sample(character_string,length)
 else:
   password = random.choices(character_string,k=length)
#return value is a list, convert to sting using join()
   password=''.join(password)

#declare a string variable*
 password_v = StringVar()
 password="Created password: " +str(password)

#assign the password to the declared string variable
 password_v.set(password)

#create a read-only box to view the output; position using place()
 password_label = Entry(password_gen, bd=0, bg="grat85", textvariable=password_v, state="readonly")
 password_label.place(x=10, y=140, height=50, width=320)

#define a string containing letters, numers, and symbols
 character_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

#define the UI
 password_gen = Tk()
 password_gen.geopetry("350x200")
 password_gen.title("Password Generator")

#application title
 title_label = Label(password_gen, text="Password Generator", font=('Ubuntu Mono',12))
 title_label.pack()

#read length
 length_label = Label(password_gen, text="Enter length of password: ")
 length_label.place(x=20, y=30)
 length_entry = Entry(password_gen, width=3)
 length_entry.place(x=190, y=30)

#read repetition
 repeat_label = Label(password_gen, text="Repetition? 1: no repetition, 2: otherwise: ")
 repeat_label.place(x=20,y=60)
 repeat_entry = Entry(password_gen, width=3)
 repeat_entry.place(x=300,y=60)

#generate password!
 password_button = Button(password_gen, text="Generate a new password!", command=generate_password)
 password_button.place(x=100, y=100)

#exit and close the app
 password_gen.mainloop()
