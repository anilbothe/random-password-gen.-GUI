# main logic
# 
import random
import string
import tkinter as tk
from typing_extensions import IntVar
 
 
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("300x200")
pass_size=tk.IntVar()

myname = tk.Label(text="Developed by,\nSatyajit giram")
myname.place(x=200,y=150)
text = tk.Label(text="")

def submit():
    global text
    text.destroy()
    password_length=pass_size.get()    
    password = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation, k=int(password_length)))
    text = tk.Label(text=f"Password is: {password}")
    text.place(x=10,y=90)
    pass_size.set("")
    


passw_label = tk.Label(root, text = 'number', font = ('calibre',10,'bold'))
passw_entry=tk.Entry(root, textvariable=pass_size, font = ('calibre',10,'normal'))
sub_btn=tk.Button(root,text = 'Generate', command = submit)
  
passw_label.grid(row=1,column=2)
passw_entry.grid(row=1,column=3)
sub_btn.grid(row=2,column=3)

root.mainloop()