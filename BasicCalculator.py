from tkinter import *

root = Tk()
root.title("Basic Calculator")

EntryTextBox = Entry(root, width=28, borderwidth=5)
EntryTextBox.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def ButtonClick(number):
    Current = EntryTextBox.get()
    EntryTextBox.delete(0, END)
    EntryTextBox.insert(0, Current + str(number))


def ButtonClear():
    EntryTextBox.delete(0, END)


def ButtonAdd():
    FirstNumber = EntryTextBox.get()
    global Fnumber
    global Math
    Math = "Addition"
    Fnumber = int(FirstNumber)
    EntryTextBox.delete(0, END)


def ButtonMultiply():
    FirstNumber = EntryTextBox.get()
    global Fnumber
    global Math
    Math = "Multiplication"
    Fnumber = int(FirstNumber)
    EntryTextBox.delete(0, END)


def ButtonSubtract():
    FirstNumber = EntryTextBox.get()
    global Fnumber
    global Math
    Math = "Subtraction"
    Fnumber = int(FirstNumber)
    EntryTextBox.delete(0, END)


def ButtonDivide():
    FirstNumber = EntryTextBox.get()
    global Fnumber
    global Math
    Math = "Division"
    Fnumber = int(FirstNumber)
    EntryTextBox.delete(0, END)


def ButtonEqual():
    SecondNumber = EntryTextBox.get()
    EntryTextBox.delete(0, END)
    if Math == "Addition":
        EntryTextBox.insert(0, Fnumber + int(SecondNumber))
    elif Math == "Subtraction":
        EntryTextBox.insert(0, Fnumber - int(SecondNumber))
    elif Math == "Multiplication":
        EntryTextBox.insert(0, Fnumber * int(SecondNumber))
    elif Math == "Division":
        EntryTextBox.insert(0, Fnumber / int(SecondNumber))


ButtonOne = Button(root, text="1", padx=40, pady=20, command=lambda: ButtonClick(1))
ButtonTwo = Button(root, text="2", padx=40, pady=20, command=lambda: ButtonClick(2))
ButtonThree = Button(root, text="3", padx=40, pady=20, command=lambda: ButtonClick(3))
ButtonFour = Button(root, text="4", padx=40, pady=20, command=lambda: ButtonClick(4))
ButtonFive = Button(root, text="5", padx=40, pady=20, command=lambda: ButtonClick(5))
ButtonSix = Button(root, text="6", padx=40, pady=20, command=lambda: ButtonClick(6))
ButtonSeven = Button(root, text="7", padx=40, pady=20, command=lambda: ButtonClick(7))
ButtonEight = Button(root, text="8", padx=40, pady=20, command=lambda: ButtonClick(8))
ButtonNine = Button(root, text="9", padx=40, pady=20, command=lambda: ButtonClick(9))
ButtonZero = Button(root, text="0", padx=40, pady=20, command=lambda: ButtonClick(0))
ButtonClear = Button(root, text="Clear", padx=79, pady=20, command=ButtonClear)
ButtonAdd = Button(root, text="+", padx=39, pady=20, command=ButtonAdd)
ButtonEqual = Button(root, text="=", padx=91, pady=20, command=ButtonEqual)
ButtonSubtract = Button(root, text="-", padx=41, pady=20, command=ButtonSubtract)
ButtonMultiply = Button(root, text="*", padx=43, pady=20, command=ButtonMultiply)
ButtonDivide = Button(root, text="/", padx=43, pady=20, command=ButtonDivide)

# putting buttons on the screen
ButtonOne.grid(row=3, column=0, columnspan=1)
ButtonTwo.grid(row=3, column=1, columnspan=1)
ButtonThree.grid(row=3, column=2, columnspan=1)

ButtonFour.grid(row=2, column=0, columnspan=1)
ButtonFive.grid(row=2, column=1, columnspan=1)
ButtonSix.grid(row=2, column=2, columnspan=1)

ButtonSeven.grid(row=1, column=0, columnspan=1)
ButtonEight.grid(row=1, column=1, columnspan=1)
ButtonNine.grid(row=1, column=2, columnspan=1)

ButtonZero.grid(row=4, column=0, columnspan=1)
ButtonAdd.grid(row=5, column=0, columnspan=1)
ButtonClear.grid(row=4, column=1, columnspan=2)
ButtonEqual.grid(row=5, column=1, columnspan=2)

ButtonSubtract.grid(row=6, column=0, columnspan=1)
ButtonMultiply.grid(row=6, column=1, columnspan=1)
ButtonDivide.grid(row=6, column=2, columnspan=1)
root.mainloop()
