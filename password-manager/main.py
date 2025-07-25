from os import write
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [random.choice(letters) for letter in range(random.randint(8, 10))]

    password_symbols = [random.choice(symbols) for symbol in range(random.randint(2, 4))]

    password_numbers = [random.choice(numbers) for number in range(random.randint(2, 4))]

    password_list = password_symbols + password_numbers + password_letters
    random.shuffle(password_list)

    _password = "".join(password_list)

    password_entry.insert(0 , _password)
    pyperclip.copy(_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email =email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email":email,
            "password":password
        }
    }


    if website =="" or password == "":
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")

    else:
        # using json

        try :
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title = "error",  message = "No Data File Found")

    else:
        # using a for loop
        # for (key, value) in data.items():
        #     if website == key:
        #         messagebox.showinfo(title=website,message=f"Email: {value["email"]} \n Password:{value["password"]}")

        # using in keyword (more faster)
        if website in data:
            email = data[website]["email"]
            password = data[website]["email"]
            messagebox.showinfo(title=website, message=f"Email: {email} \n Password:{password}")
        else:
            messagebox.showinfo(title="error", message=f"No details for {website} exists")







# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config( padx=50 , pady= 50 , bg= "white")


canvas = Canvas(width=200 , height= 200 , bg= "white" , highlightthickness= 0)
logo_img= PhotoImage(file="logo.png")
canvas.create_image(100,100,image = logo_img)
canvas.grid(  column =1 , row = 0 )


#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=20)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=37)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0 ,"angela@gmail.com")
password_entry = Entry(width=20)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search" , command=find_password, width= 13)
search_button.grid(row=1 , column= 2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)





window.mainloop()
