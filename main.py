from tkinter import *
import pyperclip as clip
import string
import random


def copy_password():
    text = show_password.cget("text")
    clip.copy(text=text)
    after_copy.pack(padx=5, pady=5)


def checkbox():
    global characters
    if string.digits in characters:
        characters = characters.replace(string.digits, "")
    if " " in characters:
        characters = characters.replace(" ", "")
    if string.punctuation in characters:
        characters = characters.replace(string.punctuation, "")

    if var1.get():
        characters += string.digits
    if var2.get():
        characters += " "
    if var3.get():
        characters += string.punctuation


def check_optios(value):
    global characters
    characters = string.ascii_letters
    match value:
        case "None":
            characters *= 0
        case "Low":
            characters *= 1
        case "Medium":
            characters *= 2
        case "High":
            characters *= 3
        case "Very High":
            characters *= 4


def random_character(length):
    global input_length
    option_text.configure(text=f"length : {length}")
    input_length = length
    option_frame.pack(padx=10, pady=10)
    check_frame.pack(padx=50, pady=5)
    generator_button.pack(padx=5, pady=5)


def generatr_password_button():
    global input_length
    copy_button.pack(padx=15, pady=15)

    def generator():
        try:
            result = random.choice(characters)
            yield result
        except:
            show_password.configure(text="select password length")

    password = ""
    input_length_copy = int(input_length)
    try:
        while input_length_copy > 0:
            password += next(generator())
            input_length_copy -= 1
        show_password.configure(text=password)
    except:
        show_password.configure(text="You didn't pick any items to create a password")


characters = ""
input_length = 0

root = Tk()
root.geometry("800x700")
root.configure(bg="DeepSkyblue4")
root.minsize(700, 650)
root.title("Password Generator")

password_frame = Frame(root, bg="green2", bd=1)
password_frame.pack(padx=10, pady=10)
show_password = Label(
    password_frame,
    text="Select length to generate password",
    fg="black",
    bg="SpringGreen2",
    width=100,
    height=3,
    font=("Vazir", 20, "bold"),
    bd=3,
    relief="solid",
)
show_password.pack(padx=10, pady=10)

copy_button = Button(password_frame, text="copy password", command=copy_password)
after_copy = Label(
    password_frame,
    text="password copied",
    fg="black",
    bg="turquoise2",
    width=15,
    height=2,
    font=("Vazir", 10, "bold"),
)


check_frame = Frame(root, bg="darkgoldenrod4", bd=1)
var1 = BooleanVar()
var2 = BooleanVar()
var3 = BooleanVar()
check_button_1 = Checkbutton(
    check_frame,
    text="Use Numbers",
    variable=var1,
    bg="darkgoldenrod1",
    bd=1,
    relief="solid",
    command=checkbox,
).pack(anchor="w", padx=50, pady=5)
check_button_2 = Checkbutton(
    check_frame,
    text="Use Spaces",
    variable=var2,
    bg="darkgoldenrod2",
    bd=1,
    relief="solid",
    command=checkbox,
).pack(anchor="w", padx=50, pady=5)
check_button_3 = Checkbutton(
    check_frame,
    text="Use Symbols",
    variable=var3,
    bg="darkgoldenrod1",
    bd=1,
    relief="solid",
    command=checkbox,
).pack(anchor="w", padx=50, pady=5)


option_frame = Frame(root, bg="deep sky blue", bd=1)

option_text = Label(
    option_frame,
    text="How much uppercase and lowercase letters are used",
    bg="cyan",
    width=50,
    height=2,
    font=("Vazir", 10, "bold"),
    bd=3,
    relief="solid",
)
option_text.pack(padx=5, pady=5)

selected_option = StringVar(value="None")
options = ("None", "Low", "Medium", "High", "Very High")
option_menu = OptionMenu(option_frame, selected_option, *options, command=check_optios)
option_menu.pack(padx=5, pady=5)


length_frame = Frame(root, bg="darkorange1", bd=1)
length_frame.pack(padx=10, pady=10)

length = Scale(
    length_frame,
    from_=1,
    to=600,
    orient=HORIZONTAL,
    highlightbackground="gold",
    activebackground="yellow",
    background="darkgoldenrod1",
    troughcolor="darkgoldenrod3",
    command=random_character,
)
length.pack(padx=5, pady=5)

option_text = Label(
    length_frame,
    text="Length : 1",
    bg="blue",
    fg="white",
    width=60,
    height=2,
    font=("Vazir", 13, "bold"),
    bd=3,
    relief="solid",
)
option_text.pack(padx=5, pady=5)


generator_button = Button(
    root,
    text="generate password",
    font=("Vazir", 20, "bold"),
    activebackground="black",
    activeforeground="white",
    background="gold",
    border=5,
    command=generatr_password_button,
)


root.mainloop()
