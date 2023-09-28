from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkcalendar
from PIL import ImageTk, Image
from tkinter import messagebox, END
import sqlite3

tasks_list = []
form = {}
counter = 1

def View():
    con1 = sqlite3.connect("C:\Pythonsql\internship.db")
    cur1 = con1.cursor()
    query = "SELECT * FROM student"
    nameSearch = name_entry_search.get()
    grad_class_search = clicked.get()
    compSearch = comp_entry_search.get()
    compLocSearch = comp_loc_entry_search.get()
    #tagSearch = tags_entry_search.get()
    conditions =[]

    if nameSearch != '':
        conditions.append("name LIKE '{}'".format(nameSearch))

    if grad_class_search in options[1:]:
        conditions.append("graduation_year = {}".format(grad_class_search))

    if compSearch != '':
         conditions.append("company_name LIKE '{}'".format(compSearch))

    if compLocSearch != '':
         conditions.append("location LIKE '{}'".format(compLocSearch))

    #if tagSearch != '':
         #conditions.append("location LIKE '{}'".format(tagSearch))

    if conditions:
        query += "\nWHERE " + " AND ".join(conditions)

    print(query)
    cur1.execute(query)
    rows = cur1.fetchall()

    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)

    con1.close()

def clear_all():
   for item in tree.get_children():
      tree.delete(item)

def searchDB():

    search = tk.Tk()
    search.title('Software Engineering Internships Database')
    search.geometry("1650x300")


    global  name_entry_search, clicked, comp_entry_search, comp_loc_entry_search

    name_label_search = tk.Label(search, text='Name:')
    name_label_search.place(x=70, y=230)
    name_entry_search = tk.Entry(search)
    name_entry_search.place(x=70, y=250)

    comp_label_search = tk.Label(search, text='Company Name:')
    comp_label_search.place(x=500, y=230)
    comp_entry_search = tk.Entry(search)
    comp_entry_search.place(x=500, y=250)

    comp_loc_search = tk.Label(search, text='Internship Location:')
    comp_loc_search.place(x=720, y=230)
    comp_loc_entry_search = tk.Entry(search)
    comp_loc_entry_search.place(x=720, y=250)
    isremote_button = Checkbutton(search, text="Remote")
    isremote_button.place(x=743,y=270)

    tags_label_search = tk.Label(search, text='Tag:')
    tags_label_search.place(x=950, y=230)
    tags_entry_search = tk.Entry(search)
    tags_entry_search.place(x=950, y=250)


    grad_label_search = tk.Label(search, text='Graduation Year:')
    grad_label_search.place(x=260, y=230)

    global options
    options = [
        "Any",
        "2026",
        "2025",
        "2024",
        "2023",
        "2022",
        "2021",
        "2020",
        "2019",
        "2018",
        "2017",
        "2016",
        "2015",
        "2014",
        "2013",
        "2012",
    ]

    clicked = tk.StringVar(search)
    clicked.set("Select Graduation Year")

    drop = tk.OptionMenu(search, clicked, *options)
    drop.place(x=260, y=250)

    global tree
    tree = ttk.Treeview(search,columns=8, column = ("c0", "c1", "c2","c3", "c4", "c5","c6", "c7"), show=["headings"])

    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="Name")

    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Eagle Email")

    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="Graduation Year")

    tree.column("#4", anchor=tk.CENTER)
    tree.heading("#4", text="Company Name")

    tree.column("#5", anchor=tk.CENTER)
    tree.heading("#5", text="Intern Position")

    tree.column("#6", anchor=tk.CENTER)
    tree.heading("#6", text="Location")

    tree.column("#7", anchor=tk.CENTER)
    tree.heading("#7", text="Start Date")

    tree.column("#8", anchor=tk.CENTER)
    tree.heading("#8", text="End Date")

    tree.pack()

    button1 = tk.Button(search, text="Display data", command=View)
    button1.place(x=1500,y=245)

    button2 = tk.Button(search, text="Reset Data", command=clear_all)
    button2.place(x=1415, y=245)



    search.mainloop()



def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)


def add_student(conn, student):
    sql = ''' INSERT INTO student(name, eagle_email,
                                              graduation_year,
                                              company_name,
                                              intern_position,
                                              location,
                                              start_date,
                                              end_date)
                  VALUES(?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, student)
    conn.commit()
    return cur.lastrowid

"""def update_student(conn, student_up):
    sql = ''' UPDATE student SET name=?, eagle_email=?, graduation_year=?, company_name=?, intern_position=?, location=?, start_date=?, end_date=?
                  WHERE name=? '''
    cur = conn.cursor()
    cur.execute(sql, student_up)
    conn.commit()
    return cur.lastrowid
"""

def submitData():
    database = r"C:\Pythonsql\internship.db"
    connection = create_connection(database)

    full_name = name_entry.get()
    email = email_entry.get()
    grad_class = grad_class_entry.get()
    company_name = company_entry.get()
    internship_position = position_entry.get()
    internship_location = loc_entry.get()
    start_date = cal.selection_get().strftime('%Y-%m-%d')
    end_date = cal2.selection_get().strftime('%Y-%m-%d')

    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    grad_class_entry.delete(0, tk.END)
    company_entry.delete(0, tk.END)
    position_entry.delete(0, tk.END)
    loc_entry.delete(0, tk.END)


    students_table = """CREATE TABLE IF NOT EXISTS student (
                                              name text NOT NULL,
                                              eagle_email text NOT NULL,
                                              graduation_year text NOT NULL,
                                              company_name integer NOT NULL,
                                              intern_position text NOT NULL,
                                              location text NOT NULL,
                                              start_date text NOT NULL,
                                              end_date text NOT NULL
                                          );"""
    student = (
    full_name, email, grad_class, company_name, internship_position, internship_location, start_date, end_date)

    if connection is not None:
        create_table(connection, students_table)
        add_student(connection, student)



col1 = 40
col2 = 160

root = tk.Tk()
root.geometry("600x900")
root.title('Software Engineering Internships Database')
global p1
p1 = tk.PhotoImage(file="icon.png")
root.iconphoto(True, p1)

image1 = Image.open("C:/Pythonsql/logo.png")
test = ImageTk.PhotoImage(image1)
logo = tk.Label(root, image=test)
logo.image = test
logo.place(x=100, y=13)

name_label = tk.Label(root, text='Name:', fg="blue")
name_label.place(x=col1, y=200)

name_entry = tk.Entry(root)
name_entry.place(x=col2, y=200)

email_label = tk.Label(root, text='Eagle Email:', fg="green")
email_label.place(x=col1, y=250)

email_entry = tk.Entry(root)
email_entry.place(x=col2, y=250)

grad_class_label = tk.Label(root, text='Graduation Class:', fg="blue")
grad_class_label.place(x=col1, y=300)

grad_class_entry = tk.Entry(root)
grad_class_entry.place(x=col2, y=300)

company_label = tk.Label(root, text='Company Name: ',fg="green")
company_label.place(x=col1, y=350)

company_entry = tk.Entry(root)
company_entry.place(x=col2, y=350)

# Internship Position label and entry
position_label = tk.Label(root, text='Internship Position: ', fg="blue")
position_label.place(x=col1, y=400)

position_entry = tk.Entry(root)
position_entry.place(x=col2, y=400)

# Internship Location label and entry
loc_label = tk.Label(root, text='Internship location: ', fg="green")
loc_label.place(x=col1, y=450)

loc_entry = tk.Entry(root)
loc_entry.place(x=col2, y=450)

#Start Date label and entry
start_date_label = tk.Label(root, text='Start Date:', fg="blue")
start_date_label.place(x=110, y=490)

cal = tkcalendar.Calendar(root, selectmode='day',
                year=2020, month=5,
                day=22, background="white", disabledbackground="blue", bordercolor="green",
               headersbackground="green", normalbackground="white", foreground='blue',
               normalforeground='blue', headersforeground='white')

cal.place(x=30, y=520)

# End Date label and entry
end_date_label = tk.Label(root, text='End Date:',fg="green")
end_date_label.place(x=400, y=490)

cal2 = tkcalendar.Calendar(root, selectmode='day',
                year=2020, month=5,
                day=22,  background="white", disabledbackground="blue", bordercolor="green",
               headersbackground="green", normalbackground="white", foreground='blue',
               normalforeground='blue', headersforeground='white')

cal2.place(x=300,y=520)


label = tk.Label(root, text='Tags:')
label.place(x=320, y=200)

list = Listbox(root, selectmode="multiple")
x = ["C", "C++", "C#", "Java", "Python",
    "R", "Go", "Ruby", "JavaScript", "Swift",
    "SQL", "Perl", "XML"]

for each_item in range(len(x)):
    list.insert(END, x[each_item])

list.place(x=360, y=205)

Submit_form = tk.Button(root, text="Submit", command=submitData,height= 3, width=13, relief='raised')
Submit_form.place(x=100, y=765)
Search_form = tk.Button(root, text="Search", command=searchDB,height= 3, width=13, relief='raised')
Search_form.place(x=380, y=765)
button3 = tk.Button(root, text="Update Data")
button3.place(x=112, y=830)


root.mainloop()


