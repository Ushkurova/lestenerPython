from tkinter import *

class extra():
    def __init__(self, s_p):
        self.s_p = s_p
        self.w = Tk()
        self.t = Text(self.w, width=25, height=6)
        self.t.pack()
        self.btn2 = Button(self.w, text='save passwords', command=self.save_p)
        self.btn2.pack()

    def save_p(self):
        p = self.t.get('1.0', 'end')
        with open('passwords.txt', 'w') as file:
            file.write(p)
        self.s_p[p] = p

        self.w.destroy()

