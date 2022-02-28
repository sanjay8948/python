import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title('Label Frame')

label_frame=ttk.LabelFrame(win,text="Enter your detail below \n "
                                    "-----------------------")
label_frame.grid(row=0,column=0,padx=50,pady=10)

labels = ['What is your name: ', 'What is your age: ', 'Gender',
          'Country: ', 'State: ', 'City: ']

for i in range(len(labels)):
    curr_label = 'label' + str(i)  # label0,label1,label2,......
    curr_label = ttk.Label(label_frame, text=labels[i])
    curr_label.grid(row=i, column=0, sticky=tk.W)

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
    curr_entrybox=ttk.Entry(label_frame,width=16,textvariable=user_info[i])
    curr_entrybox.grid(row=counter,column=1)
    counter+=1

def action():
    for i in user_info:
        print(user_info[i].get())

submit_button=ttk.Button(win,text='Submit',command=action)
submit_button.grid( row=1,columnspan=1)



for child in label_frame.winfo_children():
    child.grid_configure(padx=5,pady=5)

win.mainloop()