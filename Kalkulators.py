from tkinter import*

mansLogs = Tk()
mansLogs.title("Kalkulators")
# mansLogs.geometry("300x300")
# izveido pogas
btn0 = Button(mansLogs, text="0", padx="40", pady="20")
btn1 = Button(mansLogs, text="1", padx="40", pady="20")
btn2 = Button(mansLogs, text="2", padx="40", pady="20")
btn3 = Button(mansLogs, text="3", padx="40", pady="20")
btn4 = Button(mansLogs, text="4", padx="40", pady="20")
btn5 = Button(mansLogs, text="5", padx="40", pady="20")
btn6 = Button(mansLogs, text="6", padx="40", pady="20")
btn7 = Button(mansLogs, text="7", padx="40", pady="20")
btn8 = Button(mansLogs, text="8", padx="40", pady="20")
btn9 = Button(mansLogs, text="9", padx="40", pady="20")

btnSas = Button(mansLogs, text="+", padx="40", pady="20")
btnAtn = Button(mansLogs, text="-", padx="40", pady="20")
btnReiz = Button(mansLogs, text="*", padx="40", pady="20")
btnDal = Button(mansLogs, text="/", padx="40", pady="20")
btnVien = Button(mansLogs, text="=", padx="40", pady="20")
btnDel = Button(mansLogs, text="Del", padx="40", pady="20")

# definē novietojumu
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