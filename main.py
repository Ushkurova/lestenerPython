from tkinter import *
from extra import extra
from mylist import MyList

def get_pass():
    i = 0

    for password in s_p:
        if current_password == i:
            return s_p[password]
        i += 1

def n_w():
    a = extra(s_p)

def callback(key, value, action):
    global current_password
    if action == 'set':
        current_password += 1
    elif action == 'delete':
        current_password -=1
    l['text'] = get_pass()


s_p = MyList()
with open('passwords.txt', 'r') as file:
    sss = file.readlines()
for password in sss:
    s_p[password] = password


s_p.add_callback(callback)

current_password = 0
w = Tk()
l = Label(w, text=get_pass())
l.pack()
btn = Button(w, text='new window', command=n_w)
btn.pack()

w.mainloop()