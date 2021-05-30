from tkinter import messagebox
import xlrd
import random
import tkinter as tk
from PyDictionary import PyDictionary
loc = (r"C:\Users\Hp\Downloads\allword.xls") #change this as per requirement

dict = PyDictionary()
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
def create_word():
    a=sheet.cell_value(random.randint(0,sheet.nrows), 0)
    if dict.meaning(a)==NotADirectoryError:
        create_word()
    else:
        return a


a=create_word()
meaning = dict.meaning(a)
print("Word :{}, length :{}".format(a,len(a)-1))

main_e=tk.Tk()
main_e.geometry('400x200')
main_e.resizable(False,False)
main_e.title("WORD GAME BY PVK")
main_head=tk.Label(text='Welcome to PVK WORD GAME')
main_head.place(x=100,y=10)
def on_hint():
    if meaning==None:
        messagebox.showinfo("Hint", "Load error . Reload")
    elif "Noun" in meaning.keys():
        messagebox.showinfo("Hint",meaning['Noun'])
    elif "Verb" in meaning.keys():
        messagebox.showinfo("Hint",meaning['Verb'])
    elif "Adjective" in meaning.keys():
        messagebox.showinfo("Hint",meaning['Adjective'])
    else:
        messagebox.showinfo("Hint", "Load error . Reload")
def on_submit():
    global a
    word=a
    print(word)
    if word == answer.get():
        messagebox.showinfo('PVK',"Hurray ! YOu guessed it")
    else:
        messagebox.showinfo('PVK',"Try again")
    print(answer.get())
lab_1=tk.Label(main_e,text="Answer:")
lab_1.place(x=100,y=50)
lab_2=tk.Label(main_e,text="Clue : Length of word is {}".format(len(a)-1))
lab_2.place(x=100,y=75)
answer=tk.Entry()
answer.place(x=150,y=50)
hint_bx=tk.Button(text='Hint',command=on_hint)
hint_bx.place(x=150,y=100)
sub_bx=tk.Button(text='Submit',command=on_submit)
sub_bx.place(x=200,y=100)
main_e.mainloop()