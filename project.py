from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("login")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False,False)
def signin():
    username=user.get()
    password=code.get()
    if username== 'harshitha' and password=='1234':
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry("925x500+300+200")
        screen.config(bg="white")
        Label(screen,text="hello",bg="#fff",font=("ar",15,"bold")).pack(expand=True)
        screen.mainloop()
def forgotpassword():
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry("600x500+300+200")
        screen.config(bg="white")
        Label(screen, text="forgotpassword?", bg="#fff", font=("ar", 15, "bold")).place(x=100,y=5)
        Entry(screen, width=25, fg='black', border=0, bg='white', font=("Microsoft YaHei UI Light", 11)).place(x=200, y=30)

        Label(screen, text="phone number", bg="#fff", font=("ar", 11)).place(x=100,y=30)
        Label(screen, text="Enter otp", bg="#fff", font=("ar", 11)).place(x=100, y=50)
        Entry(screen, width=25, fg='black', border=0, bg='white', font=("Microsoft YaHei UI Light", 11)).place(x=200, y=50)
        Button(screen,text="Submit", fg="blue", bg="white",cursor="hand2", font=("Microsoft YaHei UI Light", 10)).place(x=250,y=80)

        screen.mainloop()


def signup():
    screen = Toplevel(root)
    screen.title("App")
    screen.geometry("600x500+300+200")
    screen.config(bg="white")
    Label(screen, text="Sign Up",fg="#57a1f8", bg="white", font=("ar", 29,)).place(x=100, y=5)
    Entry(screen, width=25, fg='black', border=0, bg='white', font=("Microsoft YaHei UI Light", 11)).place(x=250, y=50)

    Label(screen, text="Name", bg="#fff", font=("ar", 11)).place(x=100, y=50)
    Label(screen, text="E-mail", bg="#fff", font=("ar", 11)).place(x=100, y=70)
    Label(screen, text="Phone", bg="#fff", font=("ar", 11)).place(x=100, y=90)
    Label(screen, text="create password", bg="#fff", font=("ar", 11)).place(x=100, y=110)
    Label(screen, text="Re-enter password", bg="#fff", font=("ar", 11)).place(x=100, y=130)
    Entry(screen, width=25, fg='black', border=0, bg='white', font=("Microsoft YaHei UI Light", 11)).place(x=250, y=70)
    Entry(screen, width=25, fg='black', border=0, bg='white', font=("Microsoft YaHei UI Light", 11)).place(x=250, y=90)
    Entry(screen, width=25, fg='black', border=0, bg='white', font=("Microsoft YaHei UI Light", 11)).place(x=250, y=110)
    Entry(screen, width=25, fg='black', border=0, bg='white', font=("Microsoft YaHei UI Light", 11)).place(x=250, y=130)
    Button(screen, text="Submit", fg="blue", bg="white", cursor="hand2", font=("Microsoft YaHei UI Light", 10)).place(
        x=250, y=150)

    screen.mainloop()



frame = Frame(root, width=250, height=250, bg="white")
frame.place(x=480, y=50)
heading = Label(frame,text="sign in",fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light",29))
heading.place(x=100,y=5)
def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    name=user.get()
    if name==" ":
        user.insert(0,'Username')

user = Entry(frame,width=25, fg='black', border=0, bg='white', font=("Microsoft YaHei UI Light",11))
user.place(x=30, y=80)
user.insert(0,"Username/gmail")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25, y=107)
def on_enter(e):
    code.delete(0, 'end')
def on_leave(e):
    name=code.get()
    if name==" ":
        code.insert(0,'Password')
code = Entry(frame,width=25, fg='black', border=0, bg='white', font=("Microsoft YaHei UI Light",11))
code.place(x=30, y=150)
code.insert(0,"Password")
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)
Frame(frame, width=295,height=2, bg='black').place(x=25, y=177)
Button(frame, width=20, pady=7, text='sign in', bg="#57a1f8", fg='blue', border=0,command=signin).place(x=15, y=204)

label = Label(root, text="New User?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 10))
label.place(x=620, y=300)
label = Button(root, text="sign up", fg="blue", bg="white",cursor="hand2", font=("Microsoft YaHei UI Light", 10),command=signup)
label.place(x=680, y=300)
label = Button(root, text="forgot password?", fg="blue", bg="white",cursor="hand2", font=("Microsoft YaHei UI Light", 10),command=forgotpassword)
label.place(x=490, y=300)

root.mainloop()
