from tkinter import *
import random

root = Tk()
color_list = ['#FF3333'] 
number = 1
dot_value = 0
w = root.winfo_reqwidth()
h = root.winfo_reqheight()
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d' % (ws,hs))
root.resizable(height=False, width=False)
root.attributes('-topmost', True)
root.attributes('-alpha', 0)
root.overrideredirect(1)
root.config(background='black')

import time
wait = time.sleep
 
def fade_away():
    alpha = root.attributes("-alpha")
    if alpha > 0:
        alpha -= .01
        root.attributes("-alpha", alpha)
        root.after(100, fade_away)
    else:
        root.destroy()
 
def pack_msg():
    global Main_message, text
    try:
        Main_message.destroy()
    except:
        pass
    text = StringVar()
    Main_message = Label(root, textvariable=text)
    Main_message.config(fg='#FF3333', bg='black', font=('Times', 35))
    Main_message.place(relx=0.5, rely=0.5, anchor='center')
 
def fade_in():
    alpha = root.attributes('-alpha')
    if 0 <= alpha <= 0.9900000000000007:
        alpha += .01
        Main_message.config(fg='#FF3333', bg='black', font=('Times', 35))
        root.attributes("-alpha", alpha)
        root.after(100, fade_in)
    elif alpha == 1.0:
        root.after(2000, lambda: text.set("TEXT 1"))
        root.after(2000, lambda: text.set("TEXT 2"))
        root.after(2000, lambda: text.set("TEXT 3"))
        root.after(2000, lambda: text.set("TEXT 4"))
        root.after(2000, lambda: text.set("FINAL TEXT"))
        root.after(5000, fade_away)
    else:
        root.destroy()
 
pack_msg()
text.set("FIRST TEXT")
fade_in()
root.mainloop()

# by OverlordV1per github page: https://github.com/OverlordV1per
