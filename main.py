from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
import string  # Add this import

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = string.ascii_letters 
    numbers = string.digits
    symbols = string.punctuation

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)  # Clear existing text
    password_entry.insert(0, password)  # Insert new password
    
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty fields", message="Please make sure you haven't left any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, 
                                      message=f"These are the details entered: \nEmail: {email}"
                                      f"\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website=website_entry.get()
    try:
        with open("data.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="No data, file not found")
    else:
        if website in data:
            email=data["email"]
            password=data["password"]
            messagebox.showinfo(title=website, message=f"Email:{email}\n password:{password}")
        else:
            messagebox.showinfo(title="Error",message=f"no details for {website} exists")
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password manager")
# window.minsize(width=200,height=200)
window.config(padx=50,pady=50)
#Canvas
canvas=Canvas(width=200, height=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=1)
canvas.grid(row=0, column=1)
#Labels
website_label=Label(text="Website:")
website_label.grid(row=1, column=0)
email_label=Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label=Label(text="Password:")
password_label.grid(row=3, column=0)
#Entries
website_entry=Entry(width=21)
website_entry.grid(row=1, column=1 ,columnspan=2)
website_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"alaskdj@gmail.com")
password_entry=Entry(width=21)
password_entry.grid(row=3, column=1)

#Buttons
search_button=Button(text="Search",width=13,command=find_password)
search_button.grid(row=1, column=2)
generate_password_button=Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3,column=2)
add_button=Button(text="Add", width=36,command=save())
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()



