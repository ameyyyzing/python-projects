from tkinter import *
import datetime
from mypeople import MyPeople
from addpeople import AddPeople
from aboutus import About
date= datetime.datetime.now().date()
date= str(date)

class Application(object):
    def __init__(self,master):
        self.master = master

        #frames
        self.top = Frame(master, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(master, height=500, bg='#4287f5')
        self.bottom.pack(fill=X)

        self.top_image = PhotoImage(file='icons/phonebook.png')
        self.top_image_label = Label(self.top, image=self.top_image)
        self.top_image_label.place(x=130, y=25)

        self.heading = Label(self.top, text='My Phonebook',font='arial 15 bold', bg='white', fg='#eba134')
        self.heading.place(x=250, y=40)
        self.date_label = Label(self.top,text="Today's Date: "+date, font='arial 12 bold', fg='#eba134',bg='white')
        self.date_label.place(x=450,y=110)

        self.viewButton = Button(self.bottom, text="  My People  ", font='arial 12 bold', command=self.my_people)
        self.viewButton.place(x=250, y=70)

        self.addButton = Button(self.bottom, text=" Add People ", font='arial 12 bold', command=self.addpeoplefunction)
        self.addButton.place(x=250, y=130)

        self.aboutButton = Button(self.bottom, text="   About Us   ", font='arial 12 bold', command=self.about_us)
        self.aboutButton.place(x=250, y=190)
  
    def my_people(self):
        people = MyPeople()

    def addpeoplefunction(self):
        addpeoplewindow = AddPeople()

    def about_us(self):
        aboutpage = About()   

        

def main():
    root = Tk()
    app = Application(root)
    root.title("Contact Book")
    root.geometry("650x550+350+200")
    root.resizable(False,False)
    root.mainloop()





if __name__ == "__main__":
      main() 