import tkinter as tk
import time 
import datetime as date


windown = tk.Tk()
windown.title('Clock')

def Time_result():
    Time_H = time.strftime('%H')
    Time_M = time.strftime('%M')
    Time_S = time.strftime('%S')
    date_1=date.datetime.now()
    #cl_0 = print(f'{Time_H}:{Time_M}:{Time_S}')
    L_1.config(text=f'{Time_H}:{Time_M}:{Time_S} ',font=50)
    L_2.config(text=date_1,font=50)
    L_1.after(1000,Time_result)


L_1 = tk.Label(windown,text="Time NOW : ")
L_1.pack()
L_2 = tk.Label(windown)
L_2.pack()
Time_result()


windown.geometry('250x50')
windown.mainloop()