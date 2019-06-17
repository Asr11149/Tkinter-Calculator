from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"


        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("500x700")
root.title("Calculator")


scvalue = StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="arial 30 bold", bd=30, insertwidth=3, bg="cyan", justify='right' )
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg="grey")
b = Button(f, text="9", padx=16, pady=16, bd=8,fg='black', font="arial 15 bold",)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=16, pady=16, bd=8,fg='black', font="arial 15 bold",)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=16, pady=16, bd=8,fg='black', font="arial 15 bold",)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="6", padx=16, pady=16, bd=8,fg='black', font="arial 15 bold",)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("Button-1", click)

b = Button(f, text="5", padx=16, pady=16, bd=8,fg='black', font="arial 15 bold",)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=16, pady=16, bd=8,fg='black', font="arial 15 bold",)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="3", padx=16, pady=16, bd=8,fg='black', font="arial 15 bold",)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="2",padx=16, pady=16, bd=8,fg='black', font="arial 15 bold",)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=16, pady=16, bd=8,fg='black', font="arial 15 bold",)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="0", padx=16, pady=16, bd=8,fg='black', font="arial 15 bold",)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=16, pady=16, bd=8,fg='black', font="arial 15 bold",)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=16, pady=16, bd=8,fg='black', font="arial 15 bold",)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="/",padx=16, pady=16, bd=8,fg='black', font="arial 15 bold",)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=16, pady=16, bd=8,fg='black', font="arial 15 bold",)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=16, pady=16, bd=8,fg='black', font="arial 15 bold",)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="C", padx=16, pady=16, bd=8,fg='black', font="arial 15 bold",)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=16, pady=16, bd=8,fg='black', font="arial 15 bold",)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="00", padx=16, pady=16, bd=8,fg='black', font="arial 15 bold",)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

f.pack()

root.mainloop()

