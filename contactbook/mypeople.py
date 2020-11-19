from tkinter import *
from tkinter import messagebox
from addpeople import AddPeople
from updatepeople import Update
from display import Display
import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+600+200")
        self.title("My People")
        self.resizable(False,False)


        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=500, bg='#f5d142')
        self.bottom.pack(fill=X)

        self.top_image = PhotoImage(file='icons/people.png')
        self.top_image_label = Label(self.top, image=self.top_image)
        self.top_image_label.place(x=130, y=25)

        self.heading = Label(self.top, text='My People',
                              font='arial 18 bold', bg='white', fg='#eba134')
        self.heading.place(x=290, y=50)
        
        self.scroll = Scrollbar(self.bottom, orient=VERTICAL)


        self.listBox = Listbox(self.bottom,width=40,height=27)
        self.listBox.grid(row=0, column=0, padx=(40,0))
        self.scroll.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.scroll.set)

        persons = cur.execute("select * from 'contactbook'").fetchall()
        print(persons)
        count=0
        for person in persons:
            self.listBox.insert(count,str(person[0])+". "+person[1]+" "+person[2]+" ")
            count+=1

        self.scroll.grid(row=0, column=1, sticky=N+S)

        btnadd = Button(self.bottom, text='Add',width=10,font='sans 12 bold', command=self.add_people) 
        btnadd.grid(row=0,column=2,padx=10,pady=10,sticky=N)

        btnUpdate = Button(self.bottom, text='Update',width=10,font='sans 12 bold', command=self.update_function) 
        btnUpdate.grid(row=0,column=2,padx=10,pady=50,sticky=N)

        btnDisplay = Button(self.bottom, text='Display',width=10,font='sans 12 bold', command=self.display_function) 
        btnDisplay.grid(row=0,column=2,padx=10,pady=90,sticky=N)

        btnDelete = Button(self.bottom, text='Delete',width=10,font='sans 12 bold', command=self.delete_person) 
        btnDelete.grid(row=0,column=2,padx=10,pady=130,sticky=N)

    def delete_person(self):
        selected_items = self.listBox.curselection()
        person = self.listBox.get(selected_items)[0]
        person_id = person.split(".") 

        query = "delete from contactbook where person_id={}".format(person_id)
        answer = messagebox.askquestion("Warning","Are you sure you want to delete?")
        if answer == 'yes':
            try:
                cur.execute(query)
                con.commit()
                messagebox.showinfo("Success","Deleted")
                self.destroy()
            except Exception as e:
                messagebox.showinfo("Warning",str(e))    


    def add_people(self):
        add_page = AddPeople()
        self.destroy()

    def update_function(self):
        selected_items = self.listBox.curselection()
        person = self.listBox.get(selected_items)[0]
        person_id = person.split(".") 

        updatepage = Update()

    def display_function(self):
        selected_items = self.listBox.curselection()
        person = self.listBox.get(selected_items)[0]
        person_id = person.split(".") 

        displaypage = Display()



 