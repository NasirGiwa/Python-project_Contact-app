from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('500x500')
window.title('contact app')
window.config(bg='#223441')
window.resizable(width=True, height=True)

img = PhotoImage(file=r"C:\Users\Admin\Downloads/Luffy-PNG-Free-Download.png")
img_label = Label(window, image=img)
img_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = Frame(window, bg="#C2DFFF")
frame.pack(pady=10, padx=10)

button_frame = Frame(window)
button_frame.pack(pady=20)

listframe= Frame(window)
listframe.pack(pady=20)

name = Label(frame, text="contact name", bg="#8EEBEC")
name.pack()

entry=Entry(frame,width=30,font="calibri 14",bg="#C2DFFF")
entry.pack()

contactnumber = Label(frame, text="contact number",bg="#8EEBEC")
contactnumber.pack(pady=20)

contact_entry=Entry(frame,width=30,font="calibri 14",bg="#C2DFFF")
contact_entry.pack()

def newcontact():
    contact =entry.get()
    contact_number=contact_entry.get()
    contacts[contact]=contact_number
    error= contacts[contact] = contact_number
    if error != "":
        lb.insert(END,contact+" : "+contacts[contact])
        entry.delete(0,"end")
        contact_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "ERR Please enter a valid contact ")

def deletecontact():
    lb.delete(ANCHOR)

addcontact_button= Button(button_frame,text="Add contact",font=('times 14'),bg='#00BFFF',padx=20,pady=10,command=newcontact)
addcontact_button.pack(fill=BOTH, expand=True, side=LEFT)

delete_contact= Button(button_frame,text="Delete contact",font=('times 14'),bg='#2B65EC',padx=20,pady=10,command=deletecontact)
delete_contact.pack(fill=BOTH, expand=True ,side=RIGHT)

lb = Listbox(
    listframe,bg="#3BB9FF",
    width=30,
    height=10,
    font=('Times', 18),
    bd=5,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#56A5EC',
    activestyle="none",

)
lb.pack(side=LEFT, fill=BOTH)

sb = Scrollbar(listframe)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)


contacts={

}


window.mainloop()
