from tkinter import *

root=Tk()
root.geometry('450x300')
#root.maxsize(500,300)
#root.minsize(500,300)
root.title('Form Tkinter ')

frame=Frame(root)
frame.pack()



# Heading Label
Label(frame,text='Form Tkinter', pady=20 , font=" nexa 11 bold", fg='blue').grid(row=0, column=0, columnspan=2)

# text label and enter Point
Label(frame, text='User Name ', ).grid(row=1,column=0, pady=5)
Entry(frame).grid(row=1,column=1, pady=5)
# pass label and enter point

Label(frame, text='Password ', ).grid(row=2,column=0)
Entry(frame).grid(row=2,column=1)
Checkbutton(frame,text='I agree all Terms and Conditions ').grid( columnspan=2, pady=20)
Button(frame, text='Submit',padx=20).grid( pady=30,columnspan=2)

# footer Label

Label(root,text="Power By CNPI NooB Progrrammer",pady=10, fg='white' , bg='black').pack  ( fill=X)

root.mainloop()