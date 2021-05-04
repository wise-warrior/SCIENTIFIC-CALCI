from tkinter import *
import math as m
root = Tk()     # this creates the window ref. with root.
root.title("   SCI - CALCI  625 VD   ")
root.wm_iconbitmap("C:/Users/OK/PycharmProjects/SCIENTIFIC CALCI/calci_logo_mod_zag_icon.ico")
# to enlarge the entry box height - wise , we increase the font size so the
# window automatically resize.
e = Entry(root, width=28, borderwidth=5, relief=SUNKEN, fg="Black", bg="Yellow" , font='Mistral 20 bold')
e.grid(row=0, column=0, columnspan=10, padx=0, pady=0)  # columnspan allows widget to span more than one col

def click(to_print):
    old = e.get() # this gets the thing entered in the entry box and stores in old variable
    e.delete(0, END) # deletes the old entry
    e.insert(0, old+to_print) # enters the symbol of the button so clicked in the entry box
    return

def sc(event):
    key = event.widget  # event is basically which operation we wanna perform (relates to the BUTTON clicked)
    text = key['text']  # the sci operator so clicked in the calci stored in text.
    no = e.get()  # fetches the entry in the entry box
    result = ''  # string to store the result of the performed operation
    if text == 'deg':
        result = str(m.degrees(float(no)))  # convert the radian angle to deg,converts to str and store in result.
    if text == 'sin':
        result = str(m.sin(float(no)))  # gives the sin of entered angle in rad.
    if text == 'cos':
        result = str(m.cos(float(no)))  # gives the cos of entered angle in rad.
    if text == 'tan':
        result = str(m.tan(float(no)))  # gives tan (angle) in rad
    if text == 'lg':
        result = str(m.log10(float(no)))  # evaluates log10
    if text == 'ln':
        result = str(m.log(float(no)))  # evaluates log e
    if text == 'Sqrt':
        result = str(m.sqrt(float(no)))  # evaluates sqrt (no)
    if text == 'x!':
        result = str(m.factorial(float(no)))  # gives x! (factorial)
    if text == '1/x':
        result = str(1/(float(no)))  # gives 1/x
    if text == 'pi':
        if no == "":
            result = str(m.pi)  # if only pi clicked gives pi value
        else:
            result = str(float(no) * m.pi)  # if pi pressed after pressing a no , gives (pi * no)
    if text == 'e':
        if no == "":
            result = str(m.e)  # if only e clicked , gives the value of e
        else:
            result = str(m.e**float(no))  # if any no entered then e clicked --> gives e ^ no

    e.delete(0, END)  # deletes the entered query (no.s and operators )
    e.insert(0, result) # inserts the result in the entry box

def clear():  # this func clears the entire screen
    e.delete(0, END)
    return

def bksps():  # this func deletes a single element
    current=e.get()  # the current entry fed to current variable
    # these lines figure out the last element and delete it.
    length=len(current)-1
    e.delete(length, END)

# this func evaluates the expressions entered in the entry box
def evaluate():
    ans=e.get()  # fetches the string entered in the entry box
    ans=eval(ans)  # eval func does the evaluation
    e.delete(0, END)  # the old query string deleted
    e.insert(0, ans)  # the new result string inserted in entry box.


# Creating the Buttons -->
# the sci func are evaluated in the sc func so their result reflected on click , while
# the other expressions are evaluated  when clicked "=" .
lg = Button(root, text="lg", padx=28, pady=10, relief=RAISED, bg="Black", fg="White")
lg.bind("<Button-1>", sc) # when this button clicked Sci Func (sc) --> invoked
ln = Button(root, text="ln", padx=28, pady=10, relief=RAISED, bg="Black", fg="White")
ln.bind("<Button-1>", sc) # when this button clicked Sci Func (sc) --> invoked
# lambda func is basically a nameless func which evaluates a certain exp and
# returns the results. Its used when we require func objects for a short period of time.
# command : functionality which we want the button to do.
bracket_open = Button(root, text="(", padx=29, pady=10, relief=RAISED, bg="Black", fg="White",command=lambda: click("("))
bracket_close = Button(root, text=")", padx=31, pady=10, relief=RAISED, bg="Black", fg="White",command=lambda: click(")"))
dot = Button(root, text=".", padx=31, pady=10, relief=RAISED, bg="Black", fg="White",command=lambda: click("."))

exp = Button(root, text="^", padx=29, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click("**"))

degb = Button(root, text="deg", padx=23, pady=10, relief=RAISED, bg="Black", fg="White")
degb.bind("<Button-1>", sc) # when this button clicked Sci Func (sc) --> invoked
sinb= Button(root, text="sin", padx=24, pady=10, relief=RAISED, bg="Black", fg="White",)
sinb.bind("<Button-1>", sc) # when this button clicked Sci Func (sc) --> invoked
cosb= Button(root, text="cos", padx=24, pady=10, relief=RAISED, bg="Black", fg="White")
cosb.bind("<Button-1>", sc) # when this button clicked Sci Func (sc) --> invoked
tanb = Button(root, text="tan", padx=24, pady=10, relief=RAISED, bg="Black", fg="White")
tanb.bind("<Button-1>", sc) # when this button clicked Sci Func (sc) --> invoked

sqrtb = Button(root, text="Sqrt", padx=23, pady=10, relief=RAISED, bg="Black", fg="White")
sqrtb.bind("<Button-1>", sc) # when this button clicked Sci Func (sc) --> invoked
ac = Button(root, text="C", padx=29, pady=10, relief=RAISED, bg="Dark Red", fg="White",command=lambda: clear())
bksp = Button(root, text="Bksp", padx=19, pady=10, relief=RAISED, bg="Dark Red", fg="White",command=lambda: bksps())
mod = Button(root, text="mod", padx=21, pady=10, relief=RAISED, bg="Black", fg="White",command=lambda: click("%"))
div = Button(root, text="/", padx=30, pady=10, relief=RAISED, bg="Black", fg="White",command=lambda: click("/"))

fact = Button(root, text="x!", padx=29, pady=10, relief=RAISED, bg="Black", fg="White")
fact.bind("<Button-1>", sc) # when this button clicked Sci Func (sc) --> invoked
seven = Button(root, text="7", padx=30, pady=10, relief=RAISED, bg="indigo", fg="white",command=lambda: click("7"))
eight = Button(root, text="8", padx=29, pady=10, relief=RAISED, bg="indigo", fg="White",command=lambda: click("8"))
nine = Button(root, text="9", padx=30, pady=10, relief=RAISED, bg="indigo", fg="White",command=lambda: click("9"))
mult = Button(root, text="*", padx=30, pady=10, relief=RAISED, bg="Black", fg="White",command=lambda: click("*"))

frac = Button(root, text="1/x", padx=25, pady=10, relief=RAISED, bg="Black", fg="White")
frac.bind("<Button-1>", sc) # when this button clicked Sci Func (sc) --> called
four = Button(root, text="4", padx=30, pady=10, relief=RAISED, bg="indigo", fg="White",command=lambda: click("4"))
five = Button(root, text="5", padx=29, pady=10, relief=RAISED, bg="indigo", fg="White",command=lambda: click("5"))
six = Button(root, text="6", padx=30, pady=10, relief=RAISED, bg="indigo", fg="White",command=lambda: click("6"))
minus = Button(root, text="-", padx=30, pady=10, relief=RAISED, bg="Black", fg="White",command=lambda: click("-"))

pib = Button(root, text="pi", padx=28, pady=10, relief=RAISED, bg="Black", fg="White")
pib.bind("<Button-1>", sc) # when this button clicked Sci Func (sc) --> called
one = Button(root, text="1", padx=30, pady=10, relief=RAISED, bg="indigo", fg="White",command=lambda: click("1"))
two = Button(root, text="2", padx=29, pady=10, relief=RAISED, bg="indigo", fg="White",command=lambda: click("2"))
three = Button(root, text="3", padx=30, pady=10, relief=RAISED, bg="indigo", fg="White",command=lambda: click("3"))
plus = Button(root, text="+", padx=29, pady=10, relief=RAISED, bg="Black", fg="White",command=lambda: click("+"))

e_b = Button(root, text="e", padx=29, pady=10, relief=RAISED, bg="Black", fg="White")
e_b.bind("<Button-1>", sc) # when this button clicked Sci Func (sc) --> called
zero = Button(root, text="0", padx=29, pady=10, relief=RAISED, bg="indigo", fg="White",command=lambda: click("0"))
equal = Button(root, text="=", padx=29, pady=10, relief=RAISED, bg="Dark Orange", fg="Black",command=lambda: evaluate())


# Placing the Buttons on the Calci ( based on the desired position ) -->
lg.grid(row=1, column=0)
ln.grid(row=1, column=1)
bracket_open.grid(row=1, column=2)
bracket_close.grid(row=1, column=3)
dot.grid(row=1, column=4)

exp.grid(row=2, column=0)
degb.grid(row=2, column=1)
sinb.grid(row=2, column=2)
cosb.grid(row=2, column=3)
tanb.grid(row=2, column=4)

sqrtb.grid(row=3, column=0)
ac.grid(row=3, column=1)
bksp.grid(row=3, column=2)
mod.grid(row=3, column=3)
div.grid(row=3, column=4)

fact.grid(row=4, column=0)
seven.grid(row=4, column=1)
eight.grid(row=4, column=2)
nine.grid(row=4, column=3)
mult.grid(row=4, column=4)

frac.grid(row=5, column=0)
four.grid(row=5, column=1)
five.grid(row=5, column=2)
six.grid(row=5, column=3)
minus.grid(row=5, column=4)

pib.grid(row=6, column=0)
one.grid(row=6, column=1)
two.grid(row=6, column=2)
three.grid(row=6, column=3)
plus.grid(row=6, column=4)

e_b.grid(row=7, column=1)
zero.grid(row=7, column=2)
equal.grid(row=7, column=3)

# this holds the window until the user closes it.
root.mainloop()

