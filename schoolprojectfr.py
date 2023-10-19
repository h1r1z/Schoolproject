import tkinter
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from PIL import ImageTk, Image

ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("dark-blue")

#LOGIN WINDOW/START WINDOW/MAIN WINDOW
app = ctk.CTk()
app.attributes('-fullscreen', True)
app.title('Login')
#LOGIN WINDOW/START WINDOW/MAIN WINDOW 

#CREDENTIALS STORED IN DICTIONARY AS {USERNAME: PASSWORD}
valid_credentials = {"test":"test"}

def login(username, password):
    #LOGIN LOGIC
    if username in valid_credentials and valid_credentials[username] == password:
        app.destroy()
        main_page()
    else:
        CTkMessagebox(title="Error", message="Invalid Login Credentials", icon="cancel")

def main_page():
    main_page=ctk.CTk()
    main_page.attributes('-fullscreen', True)
    main_page.title("Password Manager")

    main_page.grid_columnconfigure(1, weight=1)
    main_page.grid_columnconfigure((2, 3), weight=0)
    main_page.grid_rowconfigure((0, 1, 2), weight=1)

    #sidebar frame
    sidebar_frame = ctk.CTkFrame(main_page,width=140, corner_radius=0)
    sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
    sidebar_frame.grid_rowconfigure(4, weight=1)

    #sidebar text ( password manager)
    logo_label = ctk.CTkLabel(sidebar_frame, text="Password Manager", font=ctk.CTkFont(size=20, weight="bold"))
    logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

    #button for
    sidebar_button_1 = ctk.CTkButton(sidebar_frame,text="randombutton1")
    sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

    #button for
    sidebar_button_2 = ctk.CTkButton(sidebar_frame,text="randombutton2")
    sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

    #button for
    sidebar_button_3 = ctk.CTkButton(sidebar_frame,text="randombutton3")
    sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

    def change_appearance_mode_event( new_appearance_mode: str):
        #logic in changing appearance mode
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event( new_scaling: str):
        #logic in changing scaling
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    #drop down menu for appearance mode
    appearance_mode_label = ctk.CTkLabel(sidebar_frame, text="Appearance Mode:", anchor="w")
    appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
    appearance_mode_optionemenu = ctk.CTkOptionMenu(sidebar_frame, values=["Dark", "Light", "System"],command=change_appearance_mode_event)
    appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

    #drop down menu for scaling
    scaling_label = ctk.CTkLabel(sidebar_frame, text="UI Scaling:", anchor="w")
    scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
    scaling_optionemenu = ctk.CTkOptionMenu(sidebar_frame, values=["100%","110%", "120%","90%","80%"],command=change_scaling_event)
    scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

    logo_label = ctk.CTkLabel(main_page,text="WELCOME{username}", font=ctk.CTkFont(size=20, weight="bold"))
    logo_label.grid(row=0, column=1, padx=20, pady=(20, 10))

    main_page.mainloop()

def registeration_window():
    registeration_window = ctk.CTkToplevel(master=app)
    registeration_window.attributes('-fullscreen', True)
    registeration_window.title('Registeration')

    img1 = ImageTk.PhotoImage(Image.open("pattern.png"))
    l1 = ctk.CTkLabel(master=registeration_window, image=img1)
    l1.pack()

    frame = ctk.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2 = ctk.CTkLabel(master=frame, text="Registeration", font=('Century Gothic', 20))
    l2.place(x=90, y=45)

    new_username_entry  = ctk.CTkEntry(master=frame, width=220, placeholder_text=' New Username')
    new_username_entry.place(x=50, y=110)

    new_password_entry = ctk.CTkEntry(master=frame, width=220, placeholder_text='New Password', show="*")
    new_password_entry.place(x=50, y=165)

    confirm_password_entry  = ctk.CTkEntry(master=frame, width=220, placeholder_text='Confirm Password', show="*")
    confirm_password_entry.place(x=50, y=220)

    error_label = ctk.CTkLabel(master=frame, text="")
    error_label.place(x=50, y=280)
    registeration_window.after(100, registeration_window.lift)

    def register():
        #REGISTRATION LOGIC 
        new_username = new_username_entry.get()
        new_password = new_password_entry.get()
        confirm_password = confirm_password_entry.get()

        if new_username == new_password:
            CTkMessagebox(title="Error", message="Username and password cannot be the same", icon="cancel")
        elif new_username in valid_credentials:
            CTkMessagebox(title="Error", message="Username already exists", icon="cancel")
        elif new_password != confirm_password:
           CTkMessagebox(title="Error", message="Passwords dont match", icon="cancel")
        elif new_password == confirm_password:
            valid_credentials[new_username] = new_password
            CTkMessagebox(title="Success", message="Registeration Successful", icon="check")
            registeration_window.destroy() 

    button1 = ctk.CTkButton(master=frame, width=220, text="Register", corner_radius=6, command=register)
    button1.place(x=50, y=280)

def button_function():
    #LOGIN BUTTON FUNCTION
    global entered_username
    entered_username = entry1.get()
    entered_password = entry2.get()
    login(entered_username, entered_password)

#LOGIN WINDOW/MAIN WINDOW/START WINDOW
img1 = ImageTk.PhotoImage(Image.open("pattern.png"))
l1 = ctk.CTkLabel(master=app, image=img1)
l1.pack()

frame = ctk.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2 = ctk.CTkLabel(master=frame, text="Password Manager Login", font=('Century Gothic', 20))
l2.place(x=40, y=45)

entry1 = ctk.CTkEntry(master=frame, width=220, placeholder_text='Username')
entry1.place(x=50, y=110)

entry2 = ctk.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
entry2.place(x=50, y=165)

button1 = ctk.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=6)
button1.place(x=50, y=240)

button2 = ctk.CTkButton(master=frame, width=220, text="Register", command=registeration_window, corner_radius=6)
button2.place(x=50, y=280)

error_label = ctk.CTkLabel(master=frame, text="",)
error_label.place(x=50, y=280)
#LOGIN WINDOW/MAIN WINDOW/START WINDOW

app.mainloop()