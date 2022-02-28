#1.for loop
import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title('Loop')

#create labels

labels=['What is your name: ','What is your age: ','Gender',
        'Country: ','State: ','City: ']

for i in range(len(labels)):
    curr_label='label'+str(i)   #label0,label1,label2,......
    curr_label = ttk.Label(win, text=labels[i])
    curr_label.grid(row=i, column=0, sticky=tk.W,padx=5,pady=5)

                                             #padding--padx,pady
#create entrybox
name_var=tk.StringVar()
user_info={
    'name'   :tk.StringVar(),
    'age'    :tk.StringVar(),
    'gender' :tk.StringVar(),
    'country':tk.StringVar(),
    'state'  :tk.StringVar(),
    'city'   :tk.StringVar()
          }

counter=0
for i in user_info:
    curr_entrybox='entry'+i   #entryname
    curr_entrybox=ttk.Entry(win,width=16,textvariable=user_info[i])
    curr_entrybox.grid(row=counter,column=1,padx=5,pady=5)
    counter+=1

#submit button
def action():
    for i in user_info:
        print(user_info[i].get())

submit_button=ttk.Button(win,text='Submit',command=action)
submit_button.grid(row=6,columnspan=2)



win.mainloop()