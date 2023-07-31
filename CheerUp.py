import tkinter as tk
from tkinter import ttk
from tkinter import *
 
root = tk.Tk()
root.title("AI Friend")
root.geometry("300x200")
root.config(bg="Darkblue")
root.resizable(False,False)
guessN=tk.StringVar()

def fgender():
    global gender
    gender = "Girl"
    sta_tus(root)
def mgender():
    global gender
    gender = "Boy"
    sta_tus(root)

def sta_tus(root):
    global guessNm
    guessNm=guessN.get()
    guessNm=guessNm.upper()
    f=Frame(root, width=300, height=300, background="darkblue") 
    f.place(x=0, y=0)
    l1=Label(root, text=f"Hello, \n{guessNm}.\nWhat do you want to Talk About?", width=25, font=('Times', 15, 'bold'), bg= 'Darkblue', fg= 'White')
    l1.place(x=0, y=20)

    loveL = tk.Button(root, text="LoveLife", command=lambda: love_life(root))
    loveL.configure(font=('calibri', 15, 'bold'), bg= 'lightBlue', fg= 'black')
    loveL.place(x=50, y=130)

    lifeL = tk.Button(root, text="Life", command=lambda: life(root))
    lifeL.configure(font=('calibri', 15, 'bold'), bg= 'Light Blue', fg= 'black', width=7)
    lifeL.place(x=170, y=130)

def life(root):
    f=Frame(root, width=300, height=300, background="darkblue") 
    f.place(x=0, y=0)
    l1=Label(root, text=f"How's the life going \n{guessNm}?", width=25, font=('Times', 15, 'bold'), bg= 'Darkblue', fg= 'White')
    l1.place(x=5, y=40)

    loveL = tk.Button(root, text="Good", command=lambda: go_od(root))
    loveL.configure(font=('calibri', 15, 'bold'), bg= 'lightBlue', fg= 'black', width=7)
    loveL.place(x=50, y=130)

    lifeL = tk.Button(root, text="Not Good", command=lambda: notgo_od(root))
    lifeL.configure(font=('calibri', 15, 'bold'), bg= 'Light Blue', fg= 'black')
    lifeL.place(x=170, y=130)
    
    def notgo_od(root):
        f=Frame(root, width=300, height=300, background="darkblue") 
        f.place(x=0, y=0)
        l1=Label(root, text=f"I'm Sorry for what you've been thought, \nRight now {guessNm}.", width=30, font=('Times', 12, 'bold'), bg= 'Darkblue', fg= 'White')
        l1.place(x=15, y=50)

        loveL = tk.Button(root, text="Ok", command=lambda: notgo_od1(root))
        loveL.configure(font=('calibri', 15, 'bold'), bg= 'lightBlue', fg= 'black', width=7)
        loveL.place(x=120, y=130)

        def notgo_od1(root):
            f=Frame(root, width=300, height=300, background="darkblue") 
            f.place(x=0, y=0)
            l1=Label(root, text=f"Our world now is Full of Hatred.\nThey Bashed you through Internet,\nEven you just wanted to help\nand make them Laught.\nEven you are the one who is Depressed.", width=30, font=('Times', 12, 'bold'), bg= 'Darkblue', fg= 'White')
            l1.place(x=15, y=5)

            loveL = tk.Button(root, text="Ok", command=lambda: notgo_od2(root))
            loveL.configure(font=('calibri', 15, 'bold'), bg= 'lightBlue', fg= 'black', width=7)
            loveL.place(x=120, y=130)

        def notgo_od2(root):
            f=Frame(root, width=300, height=300, background="darkblue") 
            f.place(x=0, y=0)
            l2=Label(root, text=f"But, Don't Give up on Life {guessNm}.\nEven you dont have Work\nAnd you are just Nothing\nLike a Trash...\nthe Only way is...", width=30, font=('Times', 12, 'bold'), bg= 'Darkblue', fg= 'White')
            l2.place(x=20, y=10)
            loveL = tk.Button(root, text="Ok", command=lambda: notgo_od3(root))
            loveL.configure(font=('calibri', 15, 'bold'), bg= 'lightBlue', fg= 'black', width=7)
            loveL.place(x=120, y=130)

        def notgo_od3(root):
            f=Frame(root, width=300, height=300, background="darkblue") 
            f.place(x=0, y=0)
            if gender== "Boy":
                l2=Label(root, text=f"Is to Believe in your Self. :)\nDon't Give up,\nGod has a Big Plan for you.\nAnd you will be Surprise of that\nCheerup {guessNm}.\nYour are Handsome :)", width=30, font=('Times', 12, 'bold'), bg= 'Darkblue', fg= 'White')
            elif gender =="Girl":
                l2=Label(root, text=f"Is to Believe in your Self. :)\nDon't Give up,\nGod has a Big Plan for you.\nAnd you will be Surprise of that\nCheerup {guessNm}.\nYour are Pretty :)", width=30, font=('Times', 12, 'bold'), bg= 'Darkblue', fg= 'White')
            l2.place(x=20, y=10)
            loveL = tk.Button(root, text="Ok", command=lambda: notgo_od4(root))
            loveL.configure(font=('calibri', 15, 'bold'), bg= 'lightBlue', fg= 'black', width=7)
            loveL.place(x=120, y=130)

        def notgo_od4(root):
            f=Frame(root, width=300, height=300, background="darkblue") 
            f.place(x=0, y=0)
            l2=Label(root, text=f"Keep Up {guessNm}. \nand Always, Keep a Smile\nI see your Cute ;)\n Godbless you. :)", width=25, font=('Times', 15, 'bold'), bg= 'Darkblue', fg= 'White')
            l2.place(x=5, y=10)
            loveL = tk.Button(root, text="Ok", command=exit)
            loveL.configure(font=('calibri', 13, 'bold'), bg= 'lightBlue', fg= 'black', width=10)
            loveL.place(x=110, y=130)

    def go_od(root):
        f=Frame(root, width=300, height=300, background="darkblue") 
        f.place(x=0, y=0)
        l1=Label(root, text=f"I'm Glad that your Life \nis in Good and Peace. :)", width=25, font=('Times', 15, 'bold'), bg= 'Darkblue', fg= 'White')
        l1.place(x=5, y=40)

        loveL = tk.Button(root, text="Ok", command=lambda: go_od1(root))
        loveL.configure(font=('calibri', 15, 'bold'), bg= 'lightBlue', fg= 'black', width=7)
        loveL.place(x=120, y=130)

        def go_od1(root):
            f=Frame(root, width=300, height=300, background="darkblue") 
            f.place(x=0, y=0)
            l2=Label(root, text=f"..God loves you so much. :)\nHe Help you to get you for a\nGood and Peace Life.\n", width=25, font=('Times', 15, 'bold'), bg= 'Darkblue', fg= 'White')
            l2.place(x=5, y=10)

            loveL = tk.Button(root, text="Ok", command=lambda: go_od2(root))
            loveL.configure(font=('calibri', 15, 'bold'), bg= 'lightBlue', fg= 'black', width=7)
            loveL.place(x=120, y=130)
        def go_od2(root):
            f=Frame(root, width=300, height=300, background="darkblue") 
            f.place(x=0, y=0)
            l2=Label(root, text=f"Always Thank God for your Strength.\n and Protection. {guessNm}\nHave more Blessings come to you. :)", width=30, font=('Times', 12, 'bold'), bg= 'Darkblue', fg= 'White')
            l2.place(x=10, y=30)

            loveL = tk.Button(root, text="Thank you", command=lambda: go_od3(root))
            loveL.configure(font=('calibri', 15, 'bold'), bg= 'lightBlue', fg= 'black')
            loveL.place(x=110, y=130)
        def go_od3(root):
            f=Frame(root, width=300, height=300, background="darkblue") 
            f.place(x=0, y=0)
            l2=Label(root, text=f"Thanks {guessNm}\nand Take Care Always. :)", width=25, font=('Times', 15, 'bold'), bg= 'Darkblue', fg= 'White')
            l2.place(x=5, y=50)

            loveL = tk.Button(root, text="Ok", command=exit)
            loveL.configure(font=('calibri', 15, 'bold'), bg= 'lightBlue', fg= 'black', width=7)
            loveL.place(x=120, y=130)



def love_life(root):
    f=Frame(root, width=300, height=300, background="darkblue") 
    f.place(x=0, y=0)
    l1=Label(root, text=f"How's your Lovelife \n{guessNm}?", width=25, font=('Times', 15, 'bold'), bg= 'Darkblue', fg= 'White')
    l1.place(x=5, y=40)

    loveL = tk.Button(root, text="Good", command=lambda: go_od(root))
    loveL.configure(font=('calibri', 15, 'bold'), bg= 'lightBlue', fg= 'black', width=7)
    loveL.place(x=50, y=130)

    lifeL = tk.Button(root, text="Not Good", command=lambda: notgo_od(root))
    lifeL.configure(font=('calibri', 15, 'bold'), bg= 'Light Blue', fg= 'black')
    lifeL.place(x=170, y=130)
    
    def notgo_od(root):
        f=Frame(root, width=300, height=300, background="darkblue") 
        f.place(x=0, y=0)
        l1=Label(root, text=f"I'm Sorry about that, \nI know it's so Hard and Sad\nto be alone. but, \nKeep on.. life is full of Surprises.", width=25, font=('Times', 15, 'bold'), bg= 'Darkblue', fg= 'White')
        l1.place(x=5, y=20)

        loveL = tk.Button(root, text="Ok", command=lambda: notgo_od1(root))
        loveL.configure(font=('calibri', 15, 'bold'), bg= 'lightBlue', fg= 'black', width=7)
        loveL.place(x=120, y=130)

        def notgo_od1(root):
            f=Frame(root, width=300, height=300, background="darkblue") 
            f.place(x=0, y=0)
            if gender == "Boy":
                l2=Label(root, text=f"Don't worry {guessNm}. \nYou are Handsome :) and A Good Guy \nYou have a Good Heart.\nand I know One day you will met a Girl.\nThat will Love you Deeply \nand Care for you", width=30, font=('Times', 12, 'bold'), bg= 'Darkblue', fg= 'White')
            elif gender == "Girl":
                l2=Label(root, text=f"Hey Don't Worry {guessNm}. \nYou are Pretty :) and Beautiful ;)\nYou have a Good Heart.\nand I know One day you will met a Man.\nThat will Love you Deeply \nand Care for you", width=30, font=('Times', 12, 'bold'), bg= 'Darkblue', fg= 'White')
            l2.place(x=20, y=10)
            loveL = tk.Button(root, text="Thank you", command=lambda: notgo_od2(root))
            loveL.configure(font=('calibri', 13, 'bold'), bg= 'lightBlue', fg= 'black', width=10)
            loveL.place(x=100, y=140)

        def notgo_od2(root):
            f=Frame(root, width=300, height=300, background="darkblue") 
            f.place(x=0, y=0)
            if gender == "Boy":
                l2=Label(root, text=f"Keep Up {guessNm}. \nand Always, Keep a Smile\nYou're so Handsome ;)\n Godbless you. :)", width=25, font=('Times', 15, 'bold'), bg= 'Darkblue', fg= 'White')
            elif gender == "Girl":
                l2=Label(root, text=f"Keep Up {guessNm}. \nand Always, Keep a Smile\nYou're so Pretty :3\n Godbless you. :)", width=25, font=('Times', 15, 'bold'), bg= 'Darkblue', fg= 'White')
            l2.place(x=5, y=10)
            loveL = tk.Button(root, text="Ok", command=exit)
            loveL.configure(font=('calibri', 13, 'bold'), bg= 'lightBlue', fg= 'black', width=10)
            loveL.place(x=110, y=130)

    def go_od(root):
        f=Frame(root, width=300, height=300, background="darkblue") 
        f.place(x=0, y=0)
        l1=Label(root, text=f"I'm Glad that your relationship \nis in Good. :)", width=25, font=('Times', 15, 'bold'), bg= 'Darkblue', fg= 'White')
        l1.place(x=5, y=40)

        loveL = tk.Button(root, text="Ok", command=lambda: go_od1(root))
        loveL.configure(font=('calibri', 15, 'bold'), bg= 'lightBlue', fg= 'black', width=7)
        loveL.place(x=120, y=130)

        def go_od1(root):
            f=Frame(root, width=300, height=300, background="darkblue") 
            f.place(x=0, y=0)
            if gender == "Boy":
                l2=Label(root, text=f"Remember,\nAlways Love your partner. \nDon't do any Action \nthat can hurt her feelings.", width=25, font=('Times', 15, 'bold'), bg= 'Darkblue', fg= 'White')
            elif gender == "Girl":
                l2=Label(root, text=f"Remember,\nIf a Guy loves you Truly. \nHe never hurt \nyour feelings.", width=25, font=('Times', 15, 'bold'), bg= 'Darkblue', fg= 'White')
            l2.place(x=5, y=10)

            loveL = tk.Button(root, text="Ok", command=lambda: go_od2(root))
            loveL.configure(font=('calibri', 15, 'bold'), bg= 'lightBlue', fg= 'black', width=7)
            loveL.place(x=120, y=130)
        def go_od2(root):
            f=Frame(root, width=300, height=300, background="darkblue") 
            f.place(x=0, y=0)
            if gender == "Boy":
                l2=Label(root, text=f"Girls have a Sensitive Heart. \nBut.. they have a Pure Heart.", width=25, font=('Times', 15, 'bold'), bg= 'Darkblue', fg= 'White')
            elif gender == "Girl":
                l2=Label(root, text=f"It is hard to find. \na Good Guy this day, \nand i'm glad you find one.", width=25, font=('Times', 15, 'bold'), bg= 'Darkblue', fg= 'White')
            l2.place(x=5, y=30)

            loveL = tk.Button(root, text="Ok", command=lambda: go_od3(root))
            loveL.configure(font=('calibri', 15, 'bold'), bg= 'lightBlue', fg= 'black', width=7)
            loveL.place(x=120, y=130)
        def go_od3(root):
            f=Frame(root, width=300, height=300, background="darkblue") 
            f.place(x=0, y=0)
            l2=Label(root, text=f"Thanks {guessNm}\nand Take Care Always. \n\nGodbless you. :)", width=25, font=('Times', 15, 'bold'), bg= 'Darkblue', fg= 'White')
            l2.place(x=5, y=10)

            loveL = tk.Button(root, text="Ok", command=exit)
            loveL.configure(font=('calibri', 15, 'bold'), bg= 'lightBlue', fg= 'black', width=7)
            loveL.place(x=120, y=130)



l1=Label(root, text="What's your Name My Friend?", width=25, font=('Times', 15, 'bold'), bg= 'Darkblue', fg= 'White')
e1=Entry(root, textvariable=guessN, width=25, font=('calibri', 13, 'bold')) 
l1.place(x=5, y=30)
e1.place(x=40, y=70) 

maleN = tk.Button(root, text="I'm Male", command=mgender)
maleN.configure(font=('calibri', 15, 'bold'), bg= 'lightBlue', fg= 'black')
maleN.place(x=40, y=130)

femaleN = tk.Button(root, text="I'm Female", command=fgender)
femaleN.configure(font=('calibri', 15, 'bold'), bg= 'Pink', fg= 'black')
femaleN.place(x=160, y=130)


root.mainloop()
