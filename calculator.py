import tkinter as tk 
#import math


def press_key(key):
    current = display_var.get()
    if current == "Error":
        current = ""
    if key == "=":
        try:
            result = eval(current)
            display_var.set(result)
        except:
            display_var.set("Error")
    
    elif key == "C":
        display_var.set("")
    else:
        display_var.set(current + key)

root = tk.Tk()
root.title("Calculator App")


display_var = tk.StringVar()
display = tk.Entry(root,textvariable=display_var,justify="right",font="Arial",)
display.grid(row=0,column=0,columnspan=4,padx=10,pady=10)


buttons = [

    ("7",1,0), ("8",1,1), ("9",1,2),("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2),("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2),("-",3,3),
    ("0",4,2), (".",4,1), ("=",4,0), ("+",4,3),
    ("C",5,0)
]


for btn_text, row, col in buttons:
    btn = tk.Button(root,text=btn_text,width=5,height=2,command=lambda key=btn_text:
                    press_key(key),background="white")
    btn.grid(row=row, column=col,padx=5,pady=5)


root.mainloop()


    