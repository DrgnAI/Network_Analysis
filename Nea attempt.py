from tkinter import *           #imports the tkinter to make GUI
import sqlite3 
 # make database and users (if not exists already) table at programme start up
with sqlite3.connect('Login.db') as db:
    c = db.cursor()         #.cursor() allows the use of sqlite commands

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEXT NOT NULL);')
db.commit()
db.close()


class main:
    def __init__(self,master):
    	# Window 
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        

    def register_user():

    
        username_info = username.get()
        password_info = password.get()
        
        file=open(username_info+".txt", "w")
        file.write(username_info+"\n")
        file.write(password_info)
        file.close()
        
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        
        Label(screen1, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).pack()
 
def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("300x250")
   
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()
 
  Label(screen1, text = "Please enter details below").pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Username * ").pack()
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1, text = "Password * ").pack()
  password_entry =  Entry(screen1, textvariable = password, show="*")
  password_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()
 
def login():
      def to_loginusr():
          screen1.destroy()
          self.login_user()
      screen1 = Toplevel(screen)
      screen1.title("Login")
      screen1.geometry("1920x1080")
      Label(screen1, text = "Please enter details below").pack()
      Label(screen1, text = "").pack()
      Label(screen1, text = "Username * ").pack()
      username_entry = Entry(screen1, textvariable = self.n_username).pack()
      Label(screen1, text = "Password * ").pack()
      password_entry =  Entry(screen1, textvariable = self.nn_password, show="*").pack()
      Label(screen1, text = "").pack()

 
 
def main_screen():
  global screen
  screen = Tk()
  screen.geometry("300x250")
  screen.title("GUI")
  Label(text = "Main Menu", bg = "green", width = "300", height = "2", font = ("Arial", 13)).pack()
  Label(text = "").pack()
  Button(text = "Login", height = "2", width = "30", command = login).pack()
  Label(text = "").pack()
  Button(text = "Register",height = "2", width = "30", command = register).pack()
 
  screen.mainloop()
 
main_screen()