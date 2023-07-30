from  tkinter import *
import ast
idx=0

def add_dispaly (num):
    global idx
    display.insert(idx,num)
    idx+=1

def add_opp_display(opperation):
    global idx
    length = len(opperation)
    display.insert(idx,opperation)
    idx+=length

def all_clear():
    global idx
    idx=0
    display.delete(0,END)

def calculate():
    entire_string=display.get()
    global idx
    try :
        node=ast.parse(entire_string,mode="eval")
        result = eval(compile(node,'<string>','eval'))
        all_clear()
        display.insert(0,str(result))
        idx+=len(str(result))
    except Exception:
        all_clear()
        display.insert(0,"ERROR")

def del_one():
    global idx
    if(idx!=0):
        idx -= 1
        display.delete(idx ,idx+1)




root = Tk()
root.title("Calculator")
root.option_add( "*font", "Arial 28  " )
display = Entry(root)
display.grid(row=1,columnspan=6)

counter=1
for i in range (2,5):
    for j in range(3):
        button = Button(root,text=counter ,width=4 ,height=2 , command=lambda text=counter : add_dispaly(text))
        button.grid(row=i,column=j)
        counter +=1
button = Button(root,text=0 , width=4 ,height=2,command=lambda text=0 : add_dispaly(text))
button.grid(row=5,column=1)

opp=["+","-","*","/","3.14","%","(","**",")","**2","."]
counter=0
for i in range(2,6):
    for j in range(3,6):
        if(counter<=10):
            operations = Button(root,text=opp[counter], width=4 ,height=2 ,command= lambda op=opp[counter]:add_opp_display(op))
            operations.grid(row=i,column=j)
            counter+=1

ac_button=Button(root,text="AC",width=4 ,height=2 ,command=all_clear)
ac_button.grid(row=5,column=0)

del_button = Button(root,text="DEL",width=4,height=2,command=del_one)
del_button.grid(row=5 , column=2)

equal_button=Button(root,text="=",width=4,height=2 , command=calculate)
equal_button.grid(row=5,column=5)




root.mainloop()
