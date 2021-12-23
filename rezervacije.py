import tkinter as tk
from tkinter import *
from tkinter import messagebox

from db import Database

db = Database('reservacijeinfo.db')
def populate_list():
    reservations_list.delete(0, END)
    for row in db.fetch():
        reservations_list.insert(END, row)


def add_item():
    if guest_text.get() == '' or country_text.get() == '' or num_guests_text.get() == '' or email_text.get() == '' or apartment_text.get() == '' or checkin_text.get() == '' or checkout_text.get() == '' or price_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(guest_text.get(), country_text.get(), num_guests_text.get(), email_text.get(), apartment_text.get(), checkin_text.get(), checkout_text.get(), price_text.get())
    reservations_list.delete(0, END)
    reservations_list.insert(END, (guest_text.get(), country_text.get(), num_guests_text.get(), email_text.get(), apartment_text.get(), checkin_text.get(), checkout_text.get(), price_text.get()))
    clear_text()
    populate_list()

def select_item(event):
    try:
        global selected_item
        index = reservations_list.curselection()[0]
        selected_item = reservations_list.get(index)
#selektujemo vrijednosti iz reservations_list i one se upisuju u entry polja
        guest_entry.delete(0, END)
        guest_entry.insert(END, selected_item[1])
        country_entry.delete(0, END)
        country_entry.insert(END, selected_item[2])
        num_guests_entry.delete(0, END)
        num_guests_entry.insert(END, selected_item[3])
        email_entry.delete(0, END)
        email_entry.insert(END, selected_item[4])
        apartment_entry.delete(0, END)
        apartment_entry.insert(END, selected_item[5])
        checkin_entry.delete(0, END)
        checkin_entry.insert(END, selected_item[6])
        checkout_entry.delete(0, END)
        checkout_entry.insert(END, selected_item[7])
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[8])
    except IndexError:
        pass


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()

def clear_text():
    guest_entry.delete(0, END)
    country_entry.delete(0, END)
    num_guests_entry.delete(0, END)
    email_entry.delete(0, END)
    apartment_entry.delete(0, END)
    checkin_entry.delete(0, END)
    checkout_entry.delete(0, END)
    price_entry.delete(0, END)

def update_item():
    db.update(selected_item[0], guest_text.get(), country_text.get(),
              num_guests_text.get(), email_text.get(), apartment_text.get(), checkin_text.get(), checkout_text.get(), price_text.get())
    populate_list()


#create a window
app=tk.Tk()

app.title("Estate & Winery San Duyevo reservations")
app.geometry("800x596")


#background design
background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(app, image=background_image)
background_label.place(relwidth=1, relheight=1)


# Guest name 
guest_text = StringVar()
guest_label = Label(app, borderwidth = 2, relief="ridge", text='Guest Name', bg = "#80c1ff", fg="#2F4F4F",  font=('Bahnschrift SemiBold', 14), pady=10 )  #pady=20  #, fg = "red", #80c1ff
guest_label.grid(row=0, column=0, sticky=W)  #allign na zapad - W
guest_entry = Entry(app, textvariable=guest_text)
guest_entry.grid(row=0, column=1)


# Country of origin
country_text = StringVar()
country_label = Label(app, borderwidth = 2, relief="ridge", text='Country of origin', fg="#2F4F4F", font=('Bahnschrift SemiBold', 14), pady=10)
country_label.grid(row=1, column=0, sticky=W)
country_entry = Entry(app, textvariable=country_text)
country_entry.grid(row=1, column=1)

# Number of guests
num_guests_text = StringVar()
num_guests_label = Label(app, borderwidth = 2, relief="ridge", text='Number of guests',bg = "#80c1ff", fg="#2F4F4F", font=('Bahnschrift SemiBold', 14), pady=10)
num_guests_label.grid(row=2, column=0, sticky=W)
num_guests_entry = Entry(app, textvariable=num_guests_text)
num_guests_entry.grid(row=2, column=1)

# Guest email
email_text = StringVar()
email_label = Label(app, borderwidth = 2, relief="ridge", text='Guest Email',fg="#2F4F4F", font=('Bahnschrift SemiBold', 14), pady=10)
email_label.grid(row=3, column=0, sticky=W)
email_entry = Entry(app, textvariable=email_text)
email_entry.grid(row=3, column=1)


# Aguestment number
apartment_text = StringVar()
apartment_label = Label(app, borderwidth = 2, relief="ridge", text='Apartment Number',bg="#80c1ff",fg="#2F4F4F", font=('Bahnschrift SemiBold', 14), pady=10)
apartment_label.grid(row=0, column=2, sticky=W)
apartment_entry = Entry(app, textvariable=apartment_text)
apartment_entry.grid(row=0, column=3)

# Check-in date
checkin_text = StringVar()
checkin_label = Label(app, borderwidth = 2, relief="ridge", text='Check-in date', fg="#2F4F4F", font=('Bahnschrift SemiBold', 14), pady=10)
checkin_label.grid(row=1, column=2, sticky=W)
checkin_entry = Entry(app, textvariable=checkin_text)
checkin_entry.grid(row=1, column=3)

# Check-out date
checkout_text = StringVar()
checkout_label = Label(app, borderwidth = 2, relief="ridge", text='Check-out date',bg = "#80c1ff", fg="#2F4F4F", font=('Bahnschrift SemiBold', 14), pady=10)
checkout_label.grid(row=2, column=2, sticky=W)
checkout_entry = Entry(app, textvariable=checkout_text)
checkout_entry.grid(row=2, column=3)

# Price
price_text = StringVar()
price_label = Label(app, borderwidth = 2, relief="ridge", text='Total price', fg="#2F4F4F", font=('Bahnschrift SemiBold', 14), pady=10)
price_label.grid(row=3, column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=3, column=3)

# Reservations List (Listbox)
reservations_list = Listbox(app, height=10, width=72)
reservations_list.grid(row=6, column=0, columnspan=3, rowspan=6, pady=20, padx=20)  #columnspan je 3 pa ce toliko biti i kod scrollbar, da bi bio pored

# Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=6, column=3)

# Set scroll to listbox
reservations_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=reservations_list.yview)

# Bind select
reservations_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(app, text='Add Reservation', width=15, command=add_item)
add_btn.grid(row=5, column=0, pady=20)

remove_btn = Button(app, text='Remove Reservation', width=15, command=remove_item)
remove_btn.grid(row=5, column=1)

update_btn = Button(app, text='Update Reservation', width=15, command=update_item)
update_btn.grid(row=5, column=2)

clear_btn = Button(app, text='Clear Input', width=15, command=clear_text)
clear_btn.grid(row=5, column=3)

populate_list()

app.mainloop()
