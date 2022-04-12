from tkinter import*

mansLogs = Tk()
mansLogs.title("Kalkulators")
# mansLogs.geometry("300x300")

def btnClick(number):
    current = e.get()
    # nolasa esošo skaitli
    e.delete(0, END)
    # nodzēš iepriekšējo
    newNumber = str(current) + str(number)
    e.insert(0, newNumber)
    # ievieto displejā
    return 0
    # ja nav ko atgriezt, tad raksta ruturn 0

def btnCommand(command):
    global num1
    # jāiegaumē skaitis un darbiba
    global mathOp
    mathOp = command
    num1 = int(e.get())
    e.delete(0, END)
    return 0

# izveido pogas
e = Entry(mansLogs, width = 15, font=("Arial Black", 20))

btn0 = Button(mansLogs, text="0", padx="40", pady="20", command = lambda:btnClick(0))
btn1 = Button(mansLogs, text="1", padx="40", pady="20", command = lambda:btnClick(1))
btn2 = Button(mansLogs, text="2", padx="40", pady="20", command = lambda:btnClick(2))
btn3 = Button(mansLogs, text="3", padx="40", pady="20", command = lambda:btnClick(3))
btn4 = Button(mansLogs, text="4", padx="40", pady="20", command = lambda:btnClick(4))
btn5 = Button(mansLogs, text="5", padx="40", pady="20", command = lambda:btnClick(5))
btn6 = Button(mansLogs, text="6", padx="40", pady="20", command = lambda:btnClick(6))
btn7 = Button(mansLogs, text="7", padx="40", pady="20", command = lambda:btnClick(7))
btn8 = Button(mansLogs, text="8", padx="40", pady="20", command = lambda:btnClick(8))
btn9 = Button(mansLogs, text="9", padx="40", pady="20", command = lambda:btnClick(9))

btnSas = Button(mansLogs, text="+", padx="40", pady="20", command = lambda:btnCommand("+"))
btnAtn = Button(mansLogs, text="-", padx="40", pady="20", command = lambda:btnCommand("-"))
btnReiz = Button(mansLogs, text="*", padx="40", pady="20", command = lambda:btnCommand("*"))
btnDal = Button(mansLogs, text="/", padx="40", pady="20", command = lambda:btnCommand("/"))
btnVien = Button(mansLogs, text="=", padx="40", pady="20")
btnDel = Button(mansLogs, text="Del", padx="40", pady="20")

# definē novietojumu
e.grid(row=0, column=0, columnspan=4)

btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btn0.grid(row=4, column=0)

btnDal.grid(row=1, column=3)
btnReiz.grid(row=2, column=3)
btnSas.grid(row=3, column=3)
btnAtn.grid(row=4, column=3)
btnDel.grid(row=4, column=1)
btnVien.grid(row=4, column=2)

mansLogs.mainloop()