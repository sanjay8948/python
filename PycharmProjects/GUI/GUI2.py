import tkinter as tk
from tkinter import ttk   #hum kewal tk se bhi kar sakte h but ttk me butan,etc ki degine achchhi h so .
from csv import DictWriter
import os
win=tk.Tk()
win.title('GUI')   #for change title-->by default it's Tk

#create labels
#name_label=ttk.Label(win,text='Enter your name:').pack()
name_label=ttk.Label(win,text='Enter your name: ')
name_label.grid(row=0,column=0)

email_label=ttk.Label(win,text='Enter your email: ')
email_label.grid(row=1,column=0,sticky=tk.W)

age_label=ttk.Label(win,text='Enter your age: ')
age_label.grid(row=2,column=0,sticky=tk.W)

gender_label=ttk.Label(win,text='Select your gender: ')
gender_label.grid(row=3,column=0,sticky=tk.W)


#create entry box
name_var=tk.StringVar()    #user jo type karega use store darne ke liye variable.
name_entrybox=ttk.Entry(win,width=16,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()

email_var=tk.StringVar()    #user jo type karega use store darne ke liye variable.
email_entrybox=ttk.Entry(win,width=16,textvariable=email_var)
email_entrybox.grid(row=1,column=1)

age_var=tk.StringVar()    #user jo type karega use store darne ke liye variable.
age_entrybox=ttk.Entry(win,width=16,textvariable=age_var)
age_entrybox.grid(row=2,column=1)

#create combo box

gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(win,width=14,textvariable=gender_var,state='readonly')
gender_combobox['values']=('--select values--','Male','Female','Others')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)

#create radio button

usertype=tk.StringVar()
radiobutton1=ttk.Radiobutton(win,text='Student',value='Student',variable=usertype)
radiobutton1.grid(row=4,column=0)

radiobutton2=ttk.Radiobutton(win,text='Teacher',value='Teacher',variable=usertype)
radiobutton2.grid(row=4,column=1)

#create check button

checkbutton_var=tk.IntVar()
checkbutton=ttk.Checkbutton(win,text='Check if u want to subscribe our newsletter',variable=checkbutton_var)
checkbutton.grid(row=5,columnspan=3)

#create button

#def action():
#    user_name=name_var.get()
#    user_age=age_var.get()
#    user_email=email_var.get()
#
#    user_gender=gender_var.get()
#    user_type=usertype.get()
#    if checkbutton_var.get()==0:
#        subscribed='No'
#    else:
#        subscribed='Yes'
#    print(user_gender,user_type,subscribed)

#    with open('file.txt','a') as f:
#        f.write(f'{user_name},{user_age},{user_email},{user_gender},{user_type},{subscribed},\n')

#    name_entrybox.delete(0,tk.END)
#    age_entrybox.delete(0, tk.END)
#    email_entrybox.delete(0, tk.END)
    #name_label.configure(foreground='Blue')
    #name_label.configure(background='Blue')


#write in csv file

def action():
    user_name=name_var.get()
    user_age=age_var.get()
    user_email=email_var.get()
    user_type=usertype.get()
    user_gender=gender_var.get()
    if checkbutton_var.get()==0:
        subscribed='No'
    else:
        subscribed='Yes'

# write in csv file

    with open('file.csv','a',newline='') as f:
        dict_writer=DictWriter(f,fieldnames=['User Name','User Email Address','User Age',
                    'User Gender','User Type','Subscribed'])
        if os.stat('file.csv').st_size==0:
            dict_writer.writeheader()
        dict_writer.writerow({
            'User Name':user_name,
            'User Email Address':user_email,
            'User Age':user_age,
            'User Gender':user_gender,
            'User Type':user_type,
            'Subscribed':subscribed
        })

    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)
    name_label.configure(foreground='Blue')


submit_button=ttk.Button(win,text='Submit',command=action)
submit_button.grid(row=6,column=0)

win.mainloop()




