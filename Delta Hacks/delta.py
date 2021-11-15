from tkinter import *
from tkinter import ttk
import tkinter.font as font
from Organizer import *



###################################Root of Project###################################

root=Tk()
root.resizable(height = None, width = None)
root.title("Delta Calander")
root.minsize(500, 500) 



##########################Setting a Gradient Background##############################


filename = PhotoImage(file = "C:\\Users\Abraham\Desktop\Delta Hacks\gradient1.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)




############################Creating a new window functions#############################


def create_window():
    global list2, list1, i, button
    list2 = sorting(list1)
    for i in range(10 - i):
        list2.append("")
            

    
    next_window=Tk()
    next_window.minsize(500, 500)
    filename = PhotoImage(file = "C:\\Users\Abraham\Desktop\Delta Hacks\gradient1.png")
    background_label = Label(next_window, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    next_window.title("Delta Calender")

    myFont = font.Font(family='Courier', size=20, weight="bold")
    title2 = Label(next_window, text = "Your Organized Goal List", bg = '#B4D7D1')
    title2['font'] = myFont
    title2.place(relwidth = 0.9, relheight= 0.1, relx= 0.05, rely=0.01)

   
    myFont2 = font.Font(family='Courier', size=10, weight='bold')

    one = ttk.Label(next_window, text= ("1. " + (str(list2[0])).split("|")[0]).upper(),background = '#B4D7D1')
    one["font"] = myFont2
    one.place(relx=0.10, rely=0.15, relwidth=0.80, relheight=0.05)
    two = ttk.Label(next_window, text= "2. "+ str(list2[1]).split("|")[0].upper(),background = '#B4D7D1')
    two["font"] = myFont2
    two.place(relx=0.10, rely=0.22, relwidth=0.8, relheight=0.05)
    three = ttk.Label(next_window, text="3. " + str(list2[2]).split("|")[0].upper(),background = '#B4D7D1')
    three["font"] = myFont2
    three.place(relx=0.10, rely=0.29, relwidth=0.8, relheight=0.05)
    four = ttk.Label(next_window, text="4. " + str(list2[3]).split("|")[0].upper(),background = '#B4D7D1')
    four["font"] = myFont2
    four.place(relx=0.10, rely=0.36, relwidth=0.8, relheight=0.05)
    five = ttk.Label(next_window, text="5. " + str(list2[4]).split("|")[0].upper(),background = '#B4D7D1')
    five["font"] = myFont2
    five.place(relx=0.10, rely=0.43, relwidth=0.8, relheight=0.05)
    six = ttk.Label(next_window, text="6. " + str(list2[5]).split("|")[0].upper(),background = '#B4D7D1')
    six["font"] = myFont2
    six.place(relx=0.10, rely=0.50, relwidth=0.8, relheight=0.05)
    seven = ttk.Label(next_window, text="7. " + str(list2[6]).split("|")[0].upper(),background = '#B4D7D1')
    seven["font"] = myFont2
    seven.place(relx=0.10, rely=0.57, relwidth=0.8, relheight=0.05)
    eight = ttk.Label(next_window, text="8. " + str(list2[7]).split("|")[0].upper(),background = '#B4D7D1')
    eight["font"] = myFont2
    eight.place(relx=0.10, rely=0.64, relwidth=0.8, relheight=0.05)
    nine = ttk.Label(next_window, text="9. " + str(list2[8]).split("|")[0].upper(),background = '#B4D7D1')
    nine["font"] = myFont2
    nine.place(relx=0.10, rely=0.71, relwidth=0.8, relheight=0.05)
    ten = ttk.Label(next_window, text="10. " + str(list2[9]).split("|")[0].upper(),background = '#B4D7D1')
    ten["font"] = myFont2
    ten.place(relx=0.10, rely=0.78, relwidth=0.8, relheight=0.05)

    button = ttk.Button(next_window, text="Upload to Google Calander", command=uploadToCalender)
    button.place(relx=0.25, rely=0.90, relwidth=0.5, relheight=0.07)
    

    next_window.mainloop()

def uploadToCalender():
    global button
    list3 = []
    button.config( state = DISABLED )
    for x in range(len(list1)):
        if list1[x] != "":
            list3.append(str(list1[x]))
    APICalendar(list3)

def To_the_nextwindow():
    global i, shmoke, var 
    content = shmoke.get()
    content2 = var.get()
    list1.append( str(content) + "|" + str(content2))
    root.destroy()
    create_window()

nextButton = ttk.Button(root,text="Submit",command=To_the_nextwindow)
nextButton.place(relwidth = 0.3, relheight= 0.05, relx= 0.35, rely=0.9)

#############################Creating a Title############################################

myFont = font.Font(family='Courier', size=20, weight='bold')
titlel = Label(root, text = "Enter Daily Goals", bg = '#B4D7D1')
titlel['font'] = myFont
titlel.place(relwidth = 1, relheight= 0.15, relx= 0, rely=0)

#############################Creating input interface#####################################

global count, i, list1
count = 0.20
list1 = []
i = 0



def adder():
    global count,i, list1, var
    content = shmoke.get()
    content2 = var.get()
    list1.append( str(content) + "|" + str(content2))
    i = i + 1
    if (count < 0.80):
        count = count + 0.07
        createEntry(count)
    
    
def createEntry(count):
    global shmoke, shmoke1, var
    shmoke = ttk.Entry(root)
    shmoke1=OptionMenu
    shmoke.place( relwidth = 0.4, relheight= 0.05, relx= 0.05, rely= count)
    var = StringVar(root)
    var.set("")
    choices = [ "", "Fitness-Priority 1","Fitness-Priority 2", "Fitness-Priority 3" ,
                "Leisure-Priority 1" , "Leisure-Priority 2" , "Leisure-Priority 3", "Academic Work-Priority 1", "Academic Work-Priority 2" , "Academic Work-Priority 3",
                "Extracurricular-Priority 1", "Extracurricular-Priority 2", "Extracurricular-Priority 3", "Career-Priority 1", "Career-Priority 2" , "Career-Priority 3", "Errands-Priority 1",
                "Errands-Priority 2", "Errands-Priority 3",]
    shmoke1 = ttk.OptionMenu(root, var, *choices)
    shmoke1.place( relwidth = 0.4, relheight= 0.05, relx= 0.55, rely= count )




def Destroyers():
    root.destroy()

myFont1 = font.Font(family='Courier', size=10, weight='bold')
Label_1 = Label(root, text="Activites",background = '#B4D7D1')
Label_1.place(relwidth = 0.4, relheight= 0.05, relx= 0.05, rely=0.15)
Label_1["font"] = myFont1

Label_2 = Label(root, text="Catogory/Priority",background = '#B4D7D1')
Label_2.place(relwidth = 0.4, relheight= 0.05, relx= 0.55, rely=0.15)
Label_2["font"] = myFont1
      
      
#inital goal entry
shmoke = ttk.Entry(root)
shmoke.place( relwidth = 0.4, relheight= 0.05, relx= 0.05, rely=0.20 )

#Add another goal button
b1 = ttk.Button(root, text="Add another goal", command=adder)
b1.place(relwidth = 0.3, relheight= 0.05, relx= 0.05, rely=0.9)

#Add clear all button
b2 = ttk.Button(root, text="Quit Application", command=Destroyers)
b2.place(relwidth = 0.3, relheight= 0.05, relx= 0.65, rely=0.9)

#Add drop down menue
var = StringVar(root)
choices = [ "", "Fitness-Priority 1","Fitness-Priority 2", "Fitness-Priority 3" ,
                "Leisure-Priority 1" , "Leisure-Priority 2" , "Leisure-Priority 3", "Academic Work-Priority 1", "Academic Work-Priority 2" , "Academic Work-Priority 3",
                "Extracurricular-Priority 1", "Extracurricular-Priority 2", "Extracurricular-Priority 3", "Career-Priority 1", "Career-Priority 2" , "Career-Priority 3", "Errands-Priority 1",
                "Errands-Priority 2", "Errands-Priority 3",]
shmoke1 = ttk.OptionMenu(root, var, *choices)
shmoke1.place( relwidth = 0.4, relheight= 0.05, relx= 0.55, rely=0.20 )




root.mainloop()
