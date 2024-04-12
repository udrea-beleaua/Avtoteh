import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import database



def mainwindow():
    app=customtkinter.CTk()
    app.title('Avtoteh')
    app.geometry('900x420')
    app.config(bg='#16161a')
    app.resizable(False,False)
    
    font1 = ('Helvetica', 20, 'bold')
    font2 = ('Arial', 17, 'bold')
    font3 = ('Arial', 13, 'bold')
    font4 = ('Arial', 13, 'bold', 'underline')
    
    id_label = customtkinter.CTkLabel(app,font=font1,text='ID:',text_color='#fffffe',bg_color='#16161a')
    id_label.place(x=45,y=20)
    
    id_entry = customtkinter.CTkEntry(app,font=font1,text_color='#fffffe',fg_color='#72757e',border_color='#7f5af0',border_width=2,width=180)
    id_entry.place(x=100,y=20)
    
    name_label = customtkinter.CTkLabel(app,font=font1,text='Name:',text_color='#fffffe',bg_color='#16161a')
    name_label.place(x=20,y=80)
    
    name_entry = customtkinter.CTkEntry(app,font=font1,text_color='#fffffe',fg_color='#72757e',border_color='#7f5af0',border_width=2,width=180)
    name_entry.place(x=100,y=80)
    
    marca_label = customtkinter.CTkLabel(app,font=font1,text='Marca:',text_color='#fffffe',bg_color='#16161a')
    marca_label.place(x=20,y=140)
    
    marca_entry = customtkinter.CTkEntry(app,font=font1,text_color='#fffffe',fg_color='#72757e',border_color='#7f5af0',border_width=2,width=180)
    marca_entry.place(x=100,y=140)
    
    model_label = customtkinter.CTkLabel(app,font=font1,text='Model:',text_color='#fffffe',bg_color='#16161a')
    model_label.place(x=20,y=200)
    
    model_entry = customtkinter.CTkEntry(app,font=font1,text_color='#fffffe',fg_color='#72757e',border_color='#7f5af0',border_width=2,width=180)
    model_entry.place(x=100,y=200)
    
    status_label = customtkinter.CTkLabel(app,font=font1,text='Status:',text_color='#fffffe',bg_color='#16161a')
    status_label.place(x=20,y=260)
    
    status_entry = customtkinter.CTkEntry(app,font=font1,text_color='#fffffe',fg_color='#72757e',border_color='#7f5af0',border_width=2,width=180)
    status_entry.place(x=100,y=260)
    
    add_button=customtkinter.CTkButton(app,font=font1,text_color='#fffffe',text='Adauga anunt',fg_color='#7f5af0',bg_color='#16161a',cursor='hand2',corner_radius=15,width=260)
    add_button.place(x=20,y=310)
    
    clear_button=customtkinter.CTkButton(app,font=font1,text_color='#fffffe',text='Anunt nou',fg_color='#2cb67d',bg_color='#16161a',cursor='hand2',corner_radius=15,width=260)
    clear_button.place(x=20,y=360)
    
    update_button=customtkinter.CTkButton(app,font=font1,text_color='#fffffe',text='Editeaza anunt',fg_color='#7f5af0',bg_color='#16161a',cursor='hand2',corner_radius=15,width=260)
    update_button.place(x=300,y=360)
    
    delete_button=customtkinter.CTkButton(app,font=font1,text_color='#fffffe',text='Sterge anunt',fg_color='#2cb67d',bg_color='#16161a',cursor='hand2',corner_radius=15,width=260)
    delete_button.place(x=580,y=360)
    
    
        
        


    app.mainloop()
mainwindow()
    
