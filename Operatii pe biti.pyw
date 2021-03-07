from tkinter import *

small_font = ('Verdana',20)
small_font_button = ('Verdana',-11, "bold")

root = Tk()
root.title("Operatii pe biti")
root.resizable(False, False)

def or_func(nr1, nr2):
    rez = 0
    x = nr1.get()
    y = nr2.get()
    if x == "" or y == "":
        rez = ""
    if x == "1" and y == "1":
        rez = 1
    if x == "1" and y == "0":
        rez = 1
    if x == "0" and y == "1":
        rez = 1
    if x == "0" and y == "0":
        rez = 0
    return rez

def and_func(nr1, nr2):
    rez = 0
    x = nr1.get()
    y = nr2.get()
    if x == "" or y == "":
        rez = ""
    if x == "1" and y == "1":
        rez = 1
    if x == "1" and y == "0":
        rez = 0
    if x == "0" and y == "1":
        rez = 0
    if x == "0" and y == "0":
        rez = 0
    return rez

def xor_func(nr1, nr2):
    rez = 0
    x = nr1.get()
    y = nr2.get()
    if x == "" or y == "":
        rez = ""
    if x == "1" and y == "1":
        rez = 0
    if x == "1" and y == "0":
        rez = 1
    if x == "0" and y == "1":
        rez = 1
    if x == "0" and y == "0":
        rez = 0
    return rez

def implica_func(nr1, nr2):
    rez = 0
    x = nr1.get()
    y = nr2.get()
    if x == "" or y == "":
        rez = ""
    if x == "1" and y == "1":
        rez = 1
    if x == "1" and y == "0":
        rez = 0
    if x == "0" and y == "1":
        rez = 1
    if x == "0" and y == "0":
        rez = 1
    return rez

def echivalenta_func(nr1, nr2):
    rez = 0
    x = nr1.get()
    y = nr2.get()
    if x == "" or y == "":
        rez = ""
    if x == "1" and y == "1":
        rez = 1
    if x == "1" and y == "0":
        rez = 0
    if x == "0" and y == "1":
        rez = 0
    if x == "0" and y == "0":
        rez = 1
    return rez

def limit_and_change(entry_text, e1, e2):
    #next entry
    if entry_text.get() == "1" or entry_text.get() == "0":
        e2.focus()

    #character limit
    if entry_text.get() == "0" or entry_text.get() == "1":
        pass
    else:
        entry_text.set("")
        e1.focus()

def run():
    add = or_func(e1_content, t1_content)
    l1.config(text=add)

    add2 = or_func(e2_content, t2_content)
    l2.config(text=add2)

    add3 = or_func(e3_content, t3_content)
    l3.config(text=add3)

    add4 = or_func(e4_content, t4_content)
    l4.config(text=add4)

    add5 = or_func(e5_content, t5_content)
    l5.config(text=add5)

    add6 = or_func(e6_content, t6_content)
    l6.config(text=add6)

    add7 = or_func(e7_content, t7_content)
    l7.config(text=add7)

    add8 = or_func(e8_content, t8_content)
    l8.config(text=add8)

    add9 = or_func(e9_content, t9_content)
    l9.config(text=add9)

    add10 = or_func(e10_content, t10_content)
    l10.config(text=add10)

    #######

    cadd = and_func(e1_content, t1_content)
    c1.config(text=cadd)

    cadd2 = and_func(e2_content, t2_content)
    c2.config(text=cadd2)

    cadd3 = and_func(e3_content, t3_content)
    c3.config(text=cadd3)

    cadd4 = and_func(e4_content, t4_content)
    c4.config(text=cadd4)

    cadd5 = and_func(e5_content, t5_content)
    c5.config(text=cadd5)

    cadd6 = and_func(e6_content, t6_content)
    c6.config(text=cadd6)

    cadd7 = and_func(e7_content, t7_content)
    c7.config(text=cadd7)

    cadd8 = and_func(e8_content, t8_content)
    c8.config(text=cadd8)

    cadd9 = and_func(e9_content, t9_content)
    c9.config(text=cadd9)

    cadd10 = and_func(e10_content, t10_content)
    c10.config(text=cadd10)

    #######

    vadd = xor_func(e1_content, t1_content)
    v1.config(text=vadd)

    vadd2 = xor_func(e2_content, t2_content)
    v2.config(text=vadd2)

    vadd3 = xor_func(e3_content, t3_content)
    v3.config(text=vadd3)

    vadd4 = xor_func(e4_content, t4_content)
    v4.config(text=vadd4)

    vadd5 = xor_func(e5_content, t5_content)
    v5.config(text=vadd5)

    vadd6 = xor_func(e6_content, t6_content)
    v6.config(text=vadd6)

    vadd7 = xor_func(e7_content, t7_content)
    v7.config(text=vadd7)

    vadd8 = xor_func(e8_content, t8_content)
    v8.config(text=vadd8)

    vadd9 = xor_func(e9_content, t9_content)
    v9.config(text=vadd9)

    vadd10 = xor_func(e10_content, t10_content)
    v10.config(text=vadd10)

    #######

    qadd = implica_func(e1_content, t1_content)
    q1.config(text=qadd)

    qadd2 = implica_func(e2_content, t2_content)
    q2.config(text=qadd2)

    qadd3 = implica_func(e3_content, t3_content)
    q3.config(text=qadd3)

    qadd4 = implica_func(e4_content, t4_content)
    q4.config(text=qadd4)

    qadd5 = implica_func(e5_content, t5_content)
    q5.config(text=qadd5)

    qadd6 = implica_func(e6_content, t6_content)
    q6.config(text=qadd6)

    qadd7 = implica_func(e7_content, t7_content)
    q7.config(text=qadd7)

    qadd8 = implica_func(e8_content, t8_content)
    q8.config(text=qadd8)

    qadd9 = implica_func(e9_content, t9_content)
    q9.config(text=qadd9)

    qadd10 = implica_func(e10_content, t10_content)
    q10.config(text=qadd10)

    #######

    wadd  = echivalenta_func(e1_content, t1_content)
    w1.config(text=wadd)

    wadd2 = echivalenta_func(e2_content, t2_content)
    w2.config(text=wadd2)

    wadd3 = echivalenta_func(e3_content, t3_content)
    w3.config(text=wadd3)

    wadd4 = echivalenta_func(e4_content, t4_content)
    w4.config(text=wadd4)

    wadd5 = echivalenta_func(e5_content, t5_content)
    w5.config(text=wadd5)

    wadd6 = echivalenta_func(e6_content, t6_content)
    w6.config(text=wadd6)

    wadd7 = echivalenta_func(e7_content, t7_content)
    w7.config(text=wadd7)

    wadd8 = echivalenta_func(e8_content, t8_content)
    w8.config(text=wadd8)

    wadd9 = echivalenta_func(e9_content, t9_content)
    w9.config(text=wadd9)

    wadd10 = echivalenta_func(e10_content, t10_content)
    w10.config(text=wadd10)

def reset():
    e1.delete(0)
    e2.delete(0)
    e3.delete(0)
    e4.delete(0)
    e5.delete(0)
    e6.delete(0)
    e7.delete(0)
    e8.delete(0)
    e9.delete(0)
    e10.delete(0)

    t1.delete(0)
    t2.delete(0)
    t3.delete(0)
    t4.delete(0)
    t5.delete(0)
    t6.delete(0)
    t7.delete(0)
    t8.delete(0)
    t9.delete(0)
    t10.delete(0)

    l1.config(text="")
    l2.config(text="")
    l3.config(text="")
    l4.config(text="")
    l5.config(text="")
    l6.config(text="")
    l7.config(text="")
    l8.config(text="")
    l9.config(text="")
    l10.config(text="")

    c1.config(text="")
    c2.config(text="")
    c3.config(text="")
    c4.config(text="")
    c5.config(text="")
    c6.config(text="")
    c7.config(text="")
    c8.config(text="")
    c9.config(text="")
    c10.config(text="")

    v1.config(text="")
    v2.config(text="")
    v3.config(text="")
    v4.config(text="")
    v5.config(text="")
    v6.config(text="")
    v7.config(text="")
    v8.config(text="")
    v9.config(text="")
    v10.config(text="")

    q1.config(text="")
    q2.config(text="")
    q3.config(text="")
    q4.config(text="")
    q5.config(text="")
    q6.config(text="")
    q7.config(text="")
    q8.config(text="")
    q9.config(text="")
    q10.config(text="")

    w1.config(text="")
    w2.config(text="")
    w3.config(text="")
    w4.config(text="")
    w5.config(text="")
    w6.config(text="")
    w7.config(text="")
    w8.config(text="")
    w9.config(text="")
    w10.config(text="")

    e1.focus()


#Entries

e1_content, t1_content = StringVar(), StringVar()
e1 = Entry(root, width = 2, font = small_font, textvariable=e1_content, justify="center")
e1.grid(column = 0, row = 1)
e1.focus()
e1_content.trace('w', lambda *args: limit_and_change(e1_content, e1, t1))
t1 = Entry(root, width = 2, font = small_font, textvariable=t1_content, justify="center")
t1.grid(column = 0, row = 2)
t1_content.trace('w', lambda *args: limit_and_change(t1_content, t1, e2))

e2_content, t2_content = StringVar(), StringVar()
e2 = Entry(root, width = 2, font = small_font, textvariable=e2_content, justify="center")
e2.grid(column = 1, row = 1)
e2_content.trace('w', lambda *args: limit_and_change(e2_content, e2, t2))
t2 = Entry(root, width = 2, font = small_font, textvariable=t2_content, justify="center")
t2.grid(column = 1, row = 2)
t2_content.trace('w', lambda *args: limit_and_change(t2_content, t2, e3))

e3_content, t3_content = StringVar(), StringVar()
e3 = Entry(root, width = 2, font = small_font, textvariable=e3_content, justify="center")
e3.grid(column = 2, row = 1)
e3_content.trace('w', lambda *args: limit_and_change(e3_content, e3, t3))
t3 = Entry(root, width = 2, font = small_font, textvariable=t3_content, justify="center")
t3.grid(column = 2, row = 2)
t3_content.trace('w', lambda *args: limit_and_change(t3_content, t3, e4))

e4_content, t4_content = StringVar(), StringVar()
e4 = Entry(root, width = 2, font = small_font, textvariable=e4_content, justify="center")
e4.grid(column = 3, row = 1)
e4_content.trace('w', lambda *args: limit_and_change(e4_content, e4, t4))
t4 = Entry(root, width = 2, font = small_font, textvariable=t4_content, justify="center")
t4.grid(column = 3, row = 2)
t4_content.trace('w', lambda *args: limit_and_change(t4_content, t4, e5))

e5_content, t5_content = StringVar(), StringVar()
e5 = Entry(root, width = 2, font = small_font, textvariable=e5_content, justify="center")
e5.grid(column = 4, row = 1)
e5_content.trace('w', lambda *args: limit_and_change(e5_content, e5, t5))
t5 = Entry(root, width = 2, font = small_font, textvariable=t5_content, justify="center")
t5.grid(column = 4, row = 2)
t5_content.trace('w', lambda *args: limit_and_change(t5_content, t5, e6))

e6_content, t6_content = StringVar(), StringVar()
e6 = Entry(root, width = 2, font = small_font, textvariable=e6_content, justify="center")
e6.grid(column = 5, row = 1)
e6_content.trace('w', lambda *args: limit_and_change(e6_content, e6, t6))
t6 = Entry(root, width = 2, font = small_font, textvariable=t6_content, justify="center")
t6.grid(column = 5, row = 2)
t6_content.trace('w', lambda *args: limit_and_change(t6_content, t6, e7))

e7_content, t7_content = StringVar(), StringVar()
e7 = Entry(root, width = 2, font = small_font, textvariable=e7_content, justify="center")
e7.grid(column = 6, row = 1)
e7_content.trace('w', lambda *args: limit_and_change(e7_content, e7, t7))
t7 = Entry(root, width = 2, font = small_font, textvariable=t7_content, justify="center")
t7.grid(column = 6, row = 2)
t7_content.trace('w', lambda *args: limit_and_change(t7_content, t7, e8))

e8_content, t8_content = StringVar(), StringVar()
e8 = Entry(root, width = 2, font = small_font, textvariable=e8_content, justify="center")
e8.grid(column = 7, row = 1)
e8_content.trace('w', lambda *args: limit_and_change(e8_content, e8, t8))
t8 = Entry(root, width = 2, font = small_font, textvariable=t8_content, justify="center")
t8.grid(column = 7, row = 2)
t8_content.trace('w', lambda *args: limit_and_change(t8_content, t8, e9))

e9_content, t9_content = StringVar(), StringVar()
e9 = Entry(root, width = 2, font = small_font, textvariable=e9_content, justify="center")
e9.grid(column = 8, row = 1)
e9_content.trace('w', lambda *args: limit_and_change(e9_content, e9, t9))
t9 = Entry(root, width = 2, font = small_font, textvariable=t9_content, justify="center")
t9.grid(column = 8, row = 2)
t9_content.trace('w', lambda *args: limit_and_change(t9_content, t9, e10))

e10_content, t10_content = StringVar(), StringVar()
e10 = Entry(root, width = 2, font = small_font, textvariable=e10_content, justify="center")
e10.grid(column = 9, row = 1)
e10_content.trace('w', lambda *args: limit_and_change(e10_content, e10, t10))
t10 = Entry(root, width = 2, font = small_font, textvariable=t10_content, justify="center")
t10.grid(column = 9, row = 2)
t10_content.trace('w', lambda *args: limit_and_change(t10_content, t10, t10))

#Labels

l1 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
l1.grid(column = 0, row = 3)
c1 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
c1.grid(column = 0, row = 4)
v1 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
v1.grid(column = 0, row = 5)
q1 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
q1.grid(column = 0, row = 6)
w1 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
w1.grid(column = 0, row = 7)

l2 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
l2.grid(column = 1, row = 3)
c2 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
c2.grid(column = 1, row = 4)
v2 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
v2.grid(column = 1, row = 5)
q2 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
q2.grid(column = 1, row = 6)
w2 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
w2.grid(column = 1, row = 7)

l3 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
l3.grid(column = 2, row = 3)
c3 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
c3.grid(column = 2, row = 4)
v3 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
v3.grid(column = 2, row = 5)
q3 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
q3.grid(column = 2, row = 6)
w3 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
w3.grid(column = 2, row = 7)

l4 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
l4.grid(column = 3, row = 3)
c4 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
c4.grid(column = 3, row = 4)
v4 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
v4.grid(column = 3, row = 5)
q4 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
q4.grid(column = 3, row = 6)
w4 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
w4.grid(column = 3, row = 7)

l5 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
l5.grid(column = 4, row = 3)
c5 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
c5.grid(column = 4, row = 4)
v5 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
v5.grid(column = 4, row = 5)
q5 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
q5.grid(column = 4, row = 6)
w5 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
w5.grid(column = 4, row = 7)

l6 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
l6.grid(column = 5, row = 3)
c6 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
c6.grid(column = 5, row = 4)
v6 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
v6.grid(column = 5, row = 5)
q6 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
q6.grid(column = 5, row = 6)
w6 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
w6.grid(column = 5, row = 7)

l7 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
l7.grid(column = 6, row = 3)
c7 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
c7.grid(column = 6, row = 4)
v7 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
v7.grid(column = 6, row = 5)
q7 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
q7.grid(column = 6, row = 6)
w7 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
w7.grid(column = 6, row = 7)

l8 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
l8.grid(column = 7, row = 3)
c8 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
c8.grid(column = 7, row = 4)
v8 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
v8.grid(column = 7, row = 5)
q8 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
q8.grid(column = 7, row = 6)
w8 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
w8.grid(column = 7, row = 7)

l9 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
l9.grid(column = 8, row = 3)
c9 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
c9.grid(column = 8, row = 4)
v9 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
v9.grid(column = 8, row = 5)
q9 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
q9.grid(column = 8, row = 6)
w9 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
w9.grid(column = 8, row = 7)

l10 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
l10.grid(column = 9, row = 3)
c10 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
c10.grid(column = 9, row = 4)
v10 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
v10.grid(column = 9, row = 5)
q10 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
q10.grid(column = 9, row = 6)
w10 = Label(root, text="", bg = "lightgray", relief = RIDGE,  width = 2, font = small_font)
w10.grid(column = 9, row = 7)

#Text

or_text = Label(root, text="OR", width = 4, relief = RIDGE, font = small_font, bg = "lightgray")
or_text.grid(column = 10 , row = 3)
and_text = Label(root, text="AND", width = 4, relief = RIDGE, font = small_font, bg = "lightgray")
and_text.grid(column = 10 , row = 4)
xor_text = Label(root, text="XOR", width = 4, relief = RIDGE, font = small_font, bg = "lightgray")
xor_text.grid(column = 10 , row = 5)
implica_text = Label(root, text="IMPL", width = 4, relief = RIDGE, font = small_font, bg = "lightgray")
implica_text.grid(column = 10 , row = 6)
echivalent_text = Label(root, text="IFF", width = 4, relief = RIDGE, font = small_font, bg = "lightgray")
echivalent_text.grid(column = 10 , row = 7)
sign_font = ("Verdana", 10)
sign = Label(root, text="by Cristian Alexandru", fg="gray", font=small_font_button, anchor=E, justify="left")
sign.grid(columnspan = 10 , row = 8)

#Buttons

run_button = Button(root, text="RUN", width = 8, height = 2, relief = RIDGE, font = small_font_button, bg="green", command = run)
run_button.grid(column = 10 , row = 1)
reset_button = Button(root, text="RESET", width = 8, height = 2, relief = RIDGE, font = small_font_button, bg="red", command = reset)
reset_button.grid(column = 10 , row = 2)

root.mainloop()
