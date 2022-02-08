from tkinter import *
import os.path                     
from tkinter import messagebox

def store_info():
    employee_name = employee_entry.get()
    phone_number = phone_number_entry.get()
    address = address_text.get("1.0", "end")
    radio_button_choice = gender_variable.get()
    coding = skill_variable.get()
    administration = skill_variable1.get()

    if radio_button_choice == 1:
        gender = "Male"
    else:
        gender = "Female"

    if coding == 1:
        coding_skill = "Coding"
    else:
        coding_skill = "None"

    if administration == 1:
        administration_skill = "Administration"
    else:
        administration_skill = "None"

    data = [employee_name, gender, phone_number, address, coding_skill, administration_skill]
    values = ["Ime: ",
              "Pol: ",
              "Broj telefona: ",
              "Adresa: ",
              "Vestina1: ",
              "Vestina2: "]

    is_file_there = os.path.exists("Users.txt")  


    if is_file_there:
        text_file = open("Users.txt", "a")   
        text_file.write("=========================")
        for i in range(len(data)):
            text_file.write(f"\n {values[i]} {data[i]} \n")
        text_file.close()
        messagebox.showinfo("User info", "Data successfully added")
    else:
        text_file = open("Users.txt", "w")  
        text_file.write("========================================= USERS ============================================")
        for i in range(len(data)):
            text_file.write(f"\n {values[i]} {data[i]} \n")
        text_file.close()
        messagebox.showinfo("User info", "Data successfully added")

root = Tk()

root.title("Employee form")
root.geometry("600x480")
placement = 20

title1 = Label(root, text='Employee records System', bg='green', fg='white', height=2)
title1.pack(fill=X)

employee_name_label = Label(root, text="Employee Name")
employee_name_label.place(x=20, y=placement + 40)
                                                                                               
employee_entry = Entry(root)                                                                   
employee_entry.place(x=200, y=placement + 40)

gender_label = Label(root, text="Gender")
gender_label.place(x=20, y=placement + 80)

gender_variable = IntVar()                 
male = Radiobutton(root, text='Male', variable=gender_variable, value=1)
male.place(x=200, y=placement + 80)
female = Radiobutton(root, text='Female', variable=gender_variable, value=2)
female.place(x=200, y=placement + 100)

phone_number_label = Label(root, text="Phone number")
phone_number_label.place(x=20, y=placement + 140)

phone_number_entry = Entry(root)
phone_number_entry.place(x=200, y=placement + 140)

address_label = Label(root, text="Address")
address_label.place(x=20, y=placement + 180)

address_text = Text(root)
address_text.place(x=200, y=placement + 180, width=200, height=50)

skills_label = Label(root, text="Skills")
skills_label.place(x=20, y=placement + 260)

skill_variable = IntVar()                       
skill_variable1 = IntVar()
coding = Checkbutton(root, text='Coding', variable=skill_variable)
coding.place(x=200, y=placement + 260)
administration = Checkbutton(root, text="Administration", variable=skill_variable1)
administration.place(x=200, y=placement + 280)


submit_button = Button(root, text="Submit info", command=store_info)
submit_button.place(x=200, y=420)


root.mainloop()
