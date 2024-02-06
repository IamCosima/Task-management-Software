from customtkinter import *
import tkinter as tk
from PIL import ImageTk, Image
#from CTkListbox import *
from CTkMessagebox import CTkMessagebox

Main_title_font=("Roboto", 24)
Sub_title_font= ("Roboto", 17)
Main_body_font=("Roboto", 14)

logged_in = ''
title_list = ''

def login_main():
    login_page =  CTkToplevel()
    login_page.geometry("600x480")
    login_page.resizable(0,0)
    login_page.title('Login')

    #--text: #d4fbf5;
    #--background: #010d0b;
    #--primary: #77f2db;
    #--secondary: #0e458d;
    #--accent: #223fea;

    #frame
    frame_Login_Details =  CTkFrame(master=login_page, width=300, height=480)
    frame_Login_Details.pack_propagate(0)
    frame_Login_Details.pack(expand=True, side="right")

    #images
    email_icon = Image.open("assets\email-icon.png")
    password_icon = Image.open("assets\password-icon.png")

    email_icon =  CTkImage(dark_image=email_icon, light_image=email_icon, size=(20,20))
    password_icon =  CTkImage(dark_image=password_icon, light_image=password_icon, size=(17,17))


    def signup():
        login_page.destroy()
        signup_page()  

    def sucsess():
        username = entry_Username.get()
        global logged_in 
        logged_in  = username
        password= entry_password.get()
        filename =  'users/'+ username + '.txt'
        try:
            with open(filename,'r') as f:
                user= f.readline().strip()
                password_f = f.readline().strip()
        except FileNotFoundError:
            CTkMessagebox(title="Error", message='User Does not exist please make an account', icon="cancel")

        if user != username.strip() or password_f != password.strip():
            CTkMessagebox(title="Error", message='Username or Password Incorrect', icon="warning")
        else:
            login_page.withdraw()
            main_page.deiconify()
            loadname()
    #widget

    label_Title =  CTkLabel(master=frame_Login_Details, text="Welcome Back!", anchor="w", justify="left", font= Main_title_font)
    label_Title.pack(anchor="w", pady=(50, 5), padx=(25, 0))
    label_Subtitle =  CTkLabel(master=frame_Login_Details, text="Sign in to your account", anchor="w", justify="left", font=Sub_title_font)
    label_Subtitle.pack(anchor="w", padx=(25, 0))

    label_Username =  CTkLabel(master=frame_Login_Details, text="  Username:", anchor="w", justify="left", font=Sub_title_font, image=email_icon, compound="left")
    label_Username.pack(anchor="w", pady=(38, 0), padx=(25, 0))

    entry_Username =  CTkEntry(master=frame_Login_Details,placeholder_text="Enter Username",width=225, border_width=1)
    entry_Username.pack(anchor="w", padx=(25, 0))

    Label_Password =  CTkLabel(master=frame_Login_Details, text="  Password:", anchor="w", justify="left", font= Sub_title_font, image=password_icon, compound="left")
    Label_Password.pack(anchor="w", pady=(21, 0), padx=(25, 0))

    entry_password =  CTkEntry(master=frame_Login_Details,placeholder_text="Enter password",width=225, border_width=1)
    entry_password.pack(anchor="w", padx=(25, 0))

    login_button = CTkButton(master=frame_Login_Details, text="Login", font=Main_body_font, width=225,command=sucsess)
    login_button.pack(anchor="w", pady=(40, 0), padx=(25, 0))
    
    signup_button = CTkButton(master=frame_Login_Details, text="signup", font=Main_body_font, width=225,command=signup)
    signup_button.pack(anchor="w", pady=(40, 0), padx=(25, 0))

def signup_page():
    register_page =  CTkToplevel()
    register_page.geometry("600x480")
    register_page.resizable(0,0)
    register_page.title('Sign Up')


    def redirect():
        register_page.withdraw()
        login_main()
    
    def signup():
        username = signup_entry_Username.get()
        password1 = signup_entry_password.get()
        paswordcon = signup_entry_password.get()

        if username.strip() == '' or password1.strip() == '' or paswordcon.strip() == '':
            CTkMessagebox(title="Error", message='Please fill in information', icon="warning")
        elif password1 != paswordcon:
            CTkMessagebox(title="Error", message='Passwords do not match', icon="warning") 
        else:
            filename =  'users/'+ username + '.txt'
            with open(filename,'w') as f:
                f.write('{}\n'.format(username))
                f.write('{}\n'.format(password1))
            
            CTkMessagebox(title="Error", message='Registation was Sucsessful', icon="check")
            redirect()


    #--text: #d4fbf5;
    #--background: #010d0b;
    #--primary: #77f2db;
    #--secondary: #0e458d;
    #--accent: #223fea;
    #frame
    frame_register_Details =  CTkFrame(master=register_page, width=300, height=480)
    frame_register_Details.pack_propagate(0)
    frame_register_Details.pack(expand=True, side="right")

    #images
    email_icon = Image.open("assets\email-icon.png")
    password_icon = Image.open("assets\password-icon.png")

    email_icon =  CTkImage(dark_image=email_icon, light_image=email_icon, size=(20,20))
    password_icon =  CTkImage(dark_image=password_icon, light_image=password_icon, size=(17,17))

  
    #widget
        
    signup_label_Title =CTkLabel(master=frame_register_Details, text="Create an account", anchor="w", justify="left", font=Main_title_font)
    signup_label_Title.pack(anchor="w", pady=(50, 5), padx=(25, 0))
    
    signup_label_Subtitle =CTkLabel(master=frame_register_Details, text="Please enter relevant information", anchor="w", justify="left", font= Sub_title_font)
    signup_label_Subtitle.pack(anchor="w", padx=(25, 0))

    signup_label_Username =CTkLabel(master=frame_register_Details, text="  Username:", anchor="w", justify="left", font= Sub_title_font, image=email_icon, compound="left")
    signup_label_Username.pack(anchor="w", pady=(38, 0), padx=(25, 0))

    signup_entry_Username = CTkEntry(master=frame_register_Details,placeholder_text="Enter Username",width=225, border_width=1)
    signup_entry_Username.pack(anchor="w", padx=(25, 0))

    signup_Label_Password =CTkLabel(master=frame_register_Details, text="  Password:", anchor="w", justify="left", font= Sub_title_font, image=password_icon, compound="left")
    signup_Label_Password.pack(anchor="w", pady=(21, 0), padx=(25, 0))

    signup_entry_password =CTkEntry(master=frame_register_Details,placeholder_text="Enter password",width=225, border_width=1)
    signup_entry_password.pack(anchor="w", padx=(25, 0))

    signup_Label_Passwordcon =CTkLabel(master=frame_register_Details, text="  Password Confirmation:", anchor="w", justify="left", font= Sub_title_font, image=password_icon, compound="left")
    signup_Label_Passwordcon.pack(anchor="w", pady=(21, 0), padx=(25, 0))

    signup_entry_passwordcon =  CTkEntry(master=frame_register_Details,placeholder_text="Enter password",width=225, border_width=1)
    signup_entry_passwordcon.pack(anchor="w", padx=(25, 0))

    register_button = CTkButton(master=frame_register_Details, text="Sign Up", font=Main_body_font, width=225,command=signup)
    register_button.pack(anchor="w",pady=(21, 0), padx=(25, 0))


def splash():
    splash_screen = CTkToplevel()
    splash_screen.title("splash Screen")
    splash_screen.geometry("300x200")
    splash_screen.overrideredirect(True)

    Label_splash =  CTkLabel(master=splash_screen,text="Task Management",text_color='#d4fbf5')
    Label_splash.pack(pady=20)

    def show():
        splash_screen.destroy()
        login_main()
        #main_page.deiconify()
    
    splash_screen.after(3000,show)

main_page = CTk()
main_page.geometry("1080x720")
main_page.resizable(0,0)
main_page.title('Task Management')
#main_page.withdraw()
set_appearance_mode('system')
#main_page.bind('<Right>', select)
#main_page.bind('<Left>', deselect)
def add_task():
    task = task_entrybox.get()
    if task:
        task_list.insert(0,task)
        task_entrybox.delete(0,END)
        save_tasks()
    else:
        CTkMessagebox(title="Error", message="Enter a task", icon="cancel")

def remove_task():
    selected_normal = task_list.curselection()
    selected_priority = task_priority_list.curselection()
    if selected_normal:
        task_list.delete(selected_normal[0])
        save_tasks()
    elif selected_priority:
        task_priority_list.delete(selected_priority[0])
        save_tasks()

    else:
        CTkMessagebox(title="Error", message="Choose a task to delete", icon="cancel")

def save_tasks():
    global logged_in
    global title_list
    filename = logged_in +'_'+ title_list.replace("\n", "") + '.txt'
    with open(filename,'w') as f:
        tasks = task_list.get(0,END) + task_priority_list.get(0,END)
        for task in tasks:
            f.write(task + "\n")


def load_tasks():
    print('Load task called')
    task_complete_list.delete(0,END)
    task_priority_list.delete(0,END)
    task_list.delete(0,END)
    global logged_in
    global title_list
    print("current tile name " + title_list)
    filename = logged_in +'_'+ title_list.replace("\n", "") + '.txt'
    try:
        with open(filename,'r') as f:
            tasks = f.readlines()
            for task in tasks:
                if '!!!' in task:
                    task_priority_list.insert(0,task.strip())
                elif '\u2713' in tasks:
                    task_complete_list.insert(0,task.strip())
                else:
                    task_list.insert(0,task.strip())
    except FileNotFoundError:
        CTkMessagebox(title="Error", message='Cannot load Tasks', icon="cancel")
    

def loadname():
    global logged_in
    global title_list
    filename_2 = 'users/'+ logged_in + '.txt'
    try:
       with open(filename_2,'r') as f:
            names = f.readlines()
            for name in names:
                if '+' in name:
                    title_list = name.strip('+')
                    task_title.configure(text=title_list)
                   
    except FileNotFoundError:
        CTkMessagebox(title="Error", message='Cannot load Tasks', icon="cancel")
    
    load_tasks()

def prioritise_task():
    task = '!!!'+task_entrybox.get()
    if task:
        task_priority_list.insert(0,task)
        task_entrybox.delete(0,END)
        save_tasks()
    else:
        CTkMessagebox(title="Error", message="Enter a task", icon="cancel")

def completed_task():
    selected_normal = task_list.curselection()
    selected_priority = task_priority_list.curselection()
    if selected_normal:
        task_complete_list.insert(END,task_list.get(selected_normal[0])+'\u2713')
        task_list.delete(selected_normal[0])
        save_tasks()
    elif selected_priority:
        task_complete_list.insert(END,task_complete_list.get(selected_priority[0])+'\u2713')
        task_priority_list.delete(selected_priority[0])
        save_tasks()

    else:
        CTkMessagebox(title="Error", message="Choose a task to Compleate", icon="cancel")

def loadlist():
    global title_list
    title_list = "+" +task_title_entry.get().upper()
    title_list = title_list.strip()
    print('Current title: '+title_list)
    global logged_in
    filename_2 = 'users/'+ logged_in + '.txt'
    try:
       with open(filename_2,'r') as f:
            names = f.readlines()
            for name in names:
                if title_list == name.strip():
                    title_list = name.strip('+')
                    task_title.configure(text=title_list)
                    load_tasks()
                    task_title_entry.delete(0,END)
                    return
                else:
                    CTkMessagebox(title="Error", message='List does not exist', icon="cancel")
    except FileNotFoundError:
        CTkMessagebox(title="Error", message='Cannot load Tasks', icon="cancel")

def addname():
    global logged_in
    filename_2 =  'users/'+ logged_in + '.txt'
    with open(filename_2,'a') as f:
        tasksname = '+'+ task_title_entry.get().upper()
        f.write(tasksname +"\n")
    loadname()
    task_title_entry.delete(0,END)


task_title = CTkLabel(master =main_page,font=Main_title_font,text='Create List')
task_title.place(x=40,y=10)
add_task_button = CTkButton(master =main_page,font=Sub_title_font,text='Add Task',width=120,command=add_task, fg_color='#56df64')
add_task_button.place(x=40,y=100)
prioritise_task_button = CTkButton(master =main_page,font=Sub_title_font,text='Prioritise Task',width=120,command=prioritise_task,fg_color='#356303')
prioritise_task_button.place(x=180,y=100)

complete_task_button = CTkButton(master =main_page,font=Sub_title_font,text='Complete Task',width=120,command=completed_task,fg_color='#356303')
complete_task_button.place(x=320,y=100)

remove_task_button = CTkButton(master =main_page,font=Sub_title_font,text='Remove Task',width=120,command=remove_task,fg_color='#ba0f0f')
remove_task_button.place(x=470,y=100)


title = CTkLabel(master =main_page,font=Sub_title_font,text='Enter title of list')
title.place(x=40,y=40)

task_title_entry =  CTkEntry(master =main_page,placeholder_text="Enter Task",width=250,height=20)
task_title_entry.place(x=40,y=70)

name_task_button = CTkButton(master =main_page,font=Sub_title_font,text='Create list',width=120,command=addname,fg_color='#356303')
name_task_button.place(x=300,y=60)

open_task_button = CTkButton(master =main_page,font=Sub_title_font,text='Open list',width=120,command=loadlist,fg_color='#356303')
open_task_button.place(x=430,y=60)

task_entrybox =  CTkEntry(master =main_page,placeholder_text="Enter Task",width=450,height=50)
task_entrybox.place(x=40,y=140)

#frame
frame_list =  CTkFrame(master=main_page, width=720, height=480)
frame_list.place(x=40,y=220)


task_priority_title = CTkLabel(master =frame_list,font=Main_title_font,text='Priority Tasks')
task_priority_title.place(x=40,y=20)
task_priority_list = tk.Listbox(frame_list,width=15,height=15,font=Main_body_font)
task_priority_list.place(x=40,y=50)


task_list_title = CTkLabel(master =frame_list,font=Main_title_font,text='Normal Tasks')
task_list_title.place(x=250,y=20)
task_list = tk.Listbox(frame_list,width=15,height=15,font=Main_body_font)
task_list.place(x=250,y=50)


task_complete_title = CTkLabel(master =frame_list,font=Main_title_font,text='Completed Tasks')
task_complete_title.place(x=450,y=20)
task_complete_list = tk.Listbox(frame_list,width=15,height=15,font=Main_body_font)
task_complete_list.place(x=450,y=50)
splash()


tk.mainloop()

#attribuations
#https://github.com/Akascape/CTkListbox
#https://github.com/tomschimansky/customtkinter
#https://github.com/Akascape/CTkMessagebox

#test