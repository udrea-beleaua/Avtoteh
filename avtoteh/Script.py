from tkinter import *
import customtkinter
import sqlite3
import bcrypt
from tkinter import messagebox
import loadingscreen

app = customtkinter.CTk()
app.title('Avtoteh')
app.geometry('1280x720')
app.config(bg='#16161a')

font1 = ('Helvetica', 25, 'bold')
font2 = ('Arial', 17, 'bold')
font3 = ('Arial', 13, 'bold')
font4 = ('Arial', 13, 'bold', 'underline')

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        username TEXT NOT NULL,
        password TEXT NOT NULL)''')

def signup():
    username = username_entry.get()
    password = password_entry.get()
    if username != '' and password != '':
        cursor.execute("SELECT username FROM users WHERE username=?", [username])
        if cursor.fetchone() is not None:
            messagebox.showerror('Error', "Username already exists.")
        else:
            encoded_password = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            cursor.execute('INSERT INTO users VALUES (?,?)', [username, hashed_password])
            conn.commit()
            messagebox.showinfo("Success", 'Account has been created.')
    else:
        messagebox.showerror('Error', 'Enter all data.')

def login():
    frame1.destroy()
    global frame2
    frame2 = customtkinter.CTkFrame(app, bg_color='#16161a', fg_color='#16161a', width=frame_width, height=frame_height)
    frame2.place(x=0, y=0)

    login_label2 = customtkinter.CTkLabel(frame2, font=font1, text='Log in', text_color='#7f5af0', bg_color='#16161a')
    login_label2.place(relx=0.85, rely=0.20, anchor='ne')

    global username_entry2
    global password_entry2
    
    username_entry2 = customtkinter.CTkEntry(frame2, font=font2, text_color='#fffffe', fg_color='#2A2B2A', bg_color='#16161a',
                                        border_color='#7f5af0', border_width=3, placeholder_text='Username',
                                        placeholder_text_color='#fffffe', width=350, height=50)
    username_entry2.place(relx=0.95, rely=0.3, anchor='ne')
    
    password_entry2 = customtkinter.CTkEntry(frame2, font=font2, text_color='#fffffe', fg_color='#2A2B2A', bg_color='#16161a',
                                        border_color='#7f5af0', border_width=3, placeholder_text='Password',
                                        placeholder_text_color='#fffffe', width=350, height=50, show='*')
    password_entry2.place(relx=0.95, rely=0.4, anchor='ne')
    
    login_button2 = customtkinter.CTkButton(frame2, command=login_account, font=font2, text_color='#fffffe', text='Log in', fg_color='#7f5af0',
                                            hover_color='#7f5af0', bg_color='#16161a', cursor='hand2', corner_radius=5, width=120)
    login_button2.place(relx=0.862, rely=0.5, anchor='ne')
    
    signup_label = customtkinter.CTkLabel(frame2, font=font3, text="Don't have an account?", text_color='#7f5af0', bg_color='#16161a')
    signup_label.place(relx=0.85, rely=0.55, anchor="ne")
    
    signup_button = customtkinter.CTkButton(frame2, command=goback, font=font4, text_color='#fffffe', text='SignUp', fg_color='#16161a',
                                            hover_color='#16161a', cursor='hand2', width=40)
    signup_button.place(relx=0.89, rely=0.55, anchor='ne')

def login_account():
    username = username_entry2.get()
    password = password_entry2.get()
    if username !='' and password !='':
        cursor.execute('SELECT password FROM users WHERE username=?',[username])
        result = cursor.fetchone()
        if result:
            if bcrypt.checkpw(password.encode('utf-8'), result[0]):
                app.destroy()
                loadingscreen.loadingscreen()
            else:
                messagebox.showerror('Error', 'Invalid password')
        else:
            messagebox.showerror('Error', 'Invalid username')
    else:
        messagebox.showerror('Error', 'Enter all data.')

def goback():
    global frame1, frame2
    if frame2:
        frame2.destroy()
    frame1 = customtkinter.CTkFrame(app, bg_color='#16161a', fg_color='#16161a', width=frame_width, height=frame_height)
    frame1.place(x=0, y=0)
    signup_label = customtkinter.CTkLabel(frame1, font=font1, text='Sign up', text_color='#7f5af0', bg_color='#16161a')
    signup_label.place(relx=0.85, rely=0.20, anchor='ne')
    global username_entry,password_entry
    username_entry = customtkinter.CTkEntry(frame1, font=font2, text_color='#fffffe', fg_color='#2A2B2A', bg_color='#16161a',
                                            border_color='#7f5af0', border_width=3, placeholder_text='Username',
                                            placeholder_text_color='#fffffe', width=350, height=50)
    username_entry.place(relx=0.95, rely=0.3, anchor='ne')
    password_entry = customtkinter.CTkEntry(frame1, font=font2, text_color='#fffffe', fg_color='#2A2B2A', bg_color='#16161a',
                                            border_color='#7f5af0', border_width=3, placeholder_text='Password',
                                            placeholder_text_color='#fffffe', width=350, height=50, show='*')
    password_entry.place(relx=0.95, rely=0.4, anchor='ne')
    signup_button = customtkinter.CTkButton(frame1, command=signup, font=font2, text_color='#fffffe', text='Sign up', fg_color='#7f5af0',
                                            hover_color='#7f5af0', bg_color='#16161a', cursor='hand2', corner_radius=5, width=120)
    signup_button.place(relx=0.862, rely=0.5, anchor='ne')
    login_label = customtkinter.CTkLabel(frame1, font=font3, text="Already have an account?", text_color='#7f5af0', bg_color='#16161a')
    login_label.place(relx=0.85, rely=0.55, anchor='ne')
    login_button = customtkinter.CTkButton(frame1, command=login, font=font4, text_color='#fffffe', text='Login', fg_color='#16161a',
                                           hover_color='#16161a', cursor='hand2', width=40)
    login_button.place(relx=0.89, rely=0.55, anchor='ne')


frame_width = 1280 
frame_height = 720 

frame1 = customtkinter.CTkFrame(app, bg_color='#16161a', fg_color='#16161a', width=frame_width, height=frame_height)
frame1.place(x=0, y=0)

signup_label = customtkinter.CTkLabel(frame1, font=font1, text='Sign up', text_color='#7f5af0', bg_color='#16161a')
signup_label.place(relx=0.85, rely=0.20, anchor='ne')

username_entry = customtkinter.CTkEntry(frame1, font=font2, text_color='#fffffe', fg_color='#2A2B2A', bg_color='#16161a',
                                        border_color='#7f5af0', border_width=3, placeholder_text='Username',
                                        placeholder_text_color='#fffffe', width=350, height=50)
username_entry.place(relx=0.95, rely=0.3, anchor='ne')

password_entry = customtkinter.CTkEntry(frame1, font=font2, text_color='#fffffe', fg_color='#2A2B2A', bg_color='#16161a',
                                        border_color='#7f5af0', border_width=3, placeholder_text='Password',
                                        placeholder_text_color='#fffffe', width=350, height=50, show='*')
password_entry.place(relx=0.95, rely=0.4, anchor='ne')

signup_button = customtkinter.CTkButton(frame1, command=signup, font=font2, text_color='#fffffe', text='Sign up', fg_color='#7f5af0',
                                        hover_color='#7f5af0', bg_color='#16161a', cursor='hand2', corner_radius=5, width=120)
signup_button.place(relx=0.862, rely=0.5, anchor='ne')

login_label = customtkinter.CTkLabel(frame1, font=font3, text="Already have an account?", text_color='#7f5af0', bg_color='#16161a')
login_label.place(relx=0.85, rely=0.55, anchor='ne')

login_button = customtkinter.CTkButton(frame1, command=login, font=font4, text_color='#fffffe', text='Login', fg_color='#16161a',
                                       hover_color='#16161a', cursor='hand2', width=40)
login_button.place(relx=0.89, rely=0.55, anchor='ne')

app.mainloop()
