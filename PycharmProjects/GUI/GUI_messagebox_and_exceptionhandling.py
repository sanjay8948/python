import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box


win=tk.Tk()


#label Frame
label_frame=ttk.LabelFrame(win,text='Contact detail ')
label_frame.grid(row=0,columnspan=1,padx=50,pady=10)

#labels
name_label=ttk.Label(label_frame,text='Enter your name: ',font=('Helvetica',14))
age_label=ttk.Label(label_frame,text='Enter your age: ',font=('Helvetica',14))

#entry box variable
name_var=tk.StringVar()
age_var=tk.StringVar()

#entry boxes
name_entrybox=ttk.Entry(label_frame,width=16,textvariable=name_var)
age_entrybox=ttk.Entry(label_frame,width=16,textvariable=age_var)

#grid
name_label.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
age_label.grid(row=0,column=1,padx=5,pady=5,sticky=tk.W)
name_entrybox.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)
age_entrybox.grid(row=1,column=1,padx=5,pady=5,sticky=tk.W)

name_entrybox.focus()

def submit():
    #m_box.showinfo('Title', 'contents of this message box')
    #m_box.showwarning('Title', 'contents of this message box')
    #m_box.showerror('Title', 'contents of this message box')

    name=name_var.get()
    age=age_var.get()
    if name=='' or age=='':
        m_box.showerror('Error','Please fill both name and error')
    else:
        try:
            age=int(age)
        except ValueError:
            m_box.showerror('Error','Only digits are allowed')
        else:
            if age < 18:
                m_box.showwarning('Warning','You are not 18+ \n Visit this content on your own risk')
            print(f'{name}:{age}')




submit_button=ttk.Button(win,text='Submit',command=submit)
submit_button.grid(row=2,columnspan=1)


win.mainloop()






