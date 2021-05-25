import tkinter as tk
from tkinter import messagebox
main_screen = tk.Tk()
main_screen.title("SGPA CALCULATOR")
main_screen.geometry('600x300')
main_screen.resizable(False, False)

main_head = tk.Label(main_screen, text="Welcome to PVK SGPA Calculator", bg='white', fg='brown')
main_head.place(x=180, y=10)
main_head.configure(font=('none', 12, 'bold'))

main_na = tk.Label(main_screen, text="Course Code\t\tGrade obtained\t\tMax credits")
main_na.place(x=30, y=55)

course_1 = tk.Label(main_screen, text='19MAT209')
course_2 = tk.Label(main_screen, text='19CSE300')
course_3 = tk.Label(main_screen, text='19PHY123')
course_4 = tk.Label(main_screen, text='19AIE214')
course_5 = tk.Label(main_screen, text='19CSE302')
course_6 = tk.Label(main_screen, text='19SSK964')

course_1.place(x=30, y=80)
course_2.place(x=30, y=105)
course_3.place(x=30, y=130)
course_4.place(x=30, y=155)
course_5.place(x=30, y=180)
course_6.place(x=30, y=205)

cre_aq1 = tk.Entry(width=15)
cre_aq2 = tk.Entry(width=15)
cre_aq3 = tk.Entry(width=15)
cre_aq4 = tk.Entry(width=15)
cre_aq5 = tk.Entry(width=15)
cre_aq6 = tk.Entry(width=15)

cre_aq1.place(x=170, y=80)
cre_aq2.place(x=170, y=105)
cre_aq3.place(x=170, y=130)
cre_aq4.place(x=170, y=155)
cre_aq5.place(x=170, y=180)
cre_aq6.place(x=170, y=205)

cre_max1 = tk.Entry(width=15)
cre_max2 = tk.Entry(width=15)
cre_max3 = tk.Entry(width=15)
cre_max4 = tk.Entry(width=15)
cre_max5 = tk.Entry(width=15)
cre_max6 = tk.Entry(width=15)

cre_max1.place(x=320, y=80)
cre_max2.place(x=320, y=105)
cre_max3.place(x=320, y=130)
cre_max4.place(x=320, y=155)
cre_max5.place(x=320, y=180)
cre_max6.place(x=320, y=205)


def calc():
    sum=0
    dict={'O':10,'A+':9.5,'A':9,'B+':8,'C':7,'D':6,'E':5,'F':0}
    m_1=cre_aq1.get()
    sum += (float(dict[m_1])*(int(cre_max1.get())))
    m_2 = cre_aq1.get()
    sum += (float(dict[m_2]) * (int(cre_max2.get())))
    m_3 = cre_aq1.get()
    sum += (float(dict[m_3]) * (int(cre_max3.get())))
    m_4 = cre_aq1.get()
    sum += (float(dict[m_4]) * (int(cre_max4.get())))
    m_5 = cre_aq1.get()
    sum += (float(dict[m_5]) * (int(cre_max5.get())))
    m_6 = cre_aq1.get()
    sum += (float(dict[m_6]) * (int(cre_max6.get())))
    avg=sum//6
    messagebox.showinfo("PVK SGPA CALCULATOR","Your SGPA is {}".format(avg))
    cre_max1.delete(1)
    cre_max2.delete(1)
    cre_max3.delete(1)
    cre_max4.delete(1)
    cre_max5.delete(1)
    cre_max6.delete(1)
    cre_aq1.delete(1)
    cre_aq2.delete(1)
    cre_aq3.delete(1)
    cre_aq4.delete(1)
    cre_aq5.delete(1)
    cre_aq6.delete(1)




sub_button = tk.Button(text='Submit', activeforeground='yellow', activebackground='black', padx=20, pady=3,
                       highlightcolor='yellow', command=calc)
sub_button.place(x=500, y=140)
tk.mainloop()
