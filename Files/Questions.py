import sqlite3
from tkinter import *
import ctypes

#set up selction window
select = Tk()
select.geometry("1415x720")
select.resizable(height = "false", width = "false")

#Set Variables for fonts and colours so changable in future updates
Font_1 = "Monoton"
Font_2 = "Tw Cen MT"

Background = "White"
Contrast = "#01104d"
Contrast_Light = "#bfd2ff"

def inop(): #for when a button isn't programmed yet
    return ctypes.windll.user32.MessageBoxW(0, "INOP", "INOP", 4)

def select_subject(): #select subject page for going into questions
    select.title("Select Subject")

    main_f = Frame(select) #blue frame on canva
    main_f.rowconfigure(0, weight = 100)
    main_f.rowconfigure(1, weight = 100)
    main_f.rowconfigure(2, weight = 375, minsize = 495)

    main_f.columnconfigure(0, weight = 1)
    main_f.columnconfigure(1, weight = 1)
    main_f.columnconfigure(2, weight = 1)
    main_f.columnconfigure(3, weight = 1)
    main_f.columnconfigure(4, weight = 1)

    back = Button(main_f,
                  text = "<- BACK",
                  command = inop,
                  font = (Font_1, 25, "bold"),
                  background = Contrast,
                  fg = "White",
                  activebackground = Contrast_Light,
                  pady = 10,
                  border = 0,
                  cursor = "hand2"
                  ).grid(row = 0, column = 0, sticky = N+E+S+W, pady = 10, padx = 10)

    title = Label(main_f,
                  text = "Select Subject:",
                  font = (Font_1, 65, "bold"),
                  anchor = "w",
                  padx = 10,
                  wrap = True,
                  wraplength = 1000,
                  justify = "left"
                  ).grid(row = 1, column = 0, columnspan = 5, sticky = N+E+S+W)

    subjects_f = Frame(main_f)#green frame on canve
    subjects_f.rowconfigure(0, weight = 1)
    subjects_f.rowconfigure(1, weight = 1)
    subjects_f.rowconfigure(2, weight = 1)
    subjects_f.rowconfigure(3, weight = 1)
    subjects_f.rowconfigure(4, weight = 1)

    subjects_f.columnconfigure(0, weight = 1)
    subjects_f.columnconfigure(1, weight = 1)

    #subject buttons:
    computer_science = Button(subjects_f,
                              text = "COMPUTER SCIENCE",
                              command = inop,
                              font = (Font_1, 25, "bold"),
                              background = Contrast,
                              fg = "White",
                              activebackground = Contrast_Light,
                              border = 0,
                              cursor = "hand2"
                              ).grid(row = 0, column = 0, sticky = N+E+S+W, pady = 10, padx = 10)

    biology = Button(subjects_f,
                              text = "BIOLOGY",
                              command = inop,
                              font = (Font_1, 25, "bold"),
                              background = Contrast,
                              fg = "White",
                              activebackground = Contrast_Light,
                              border = 0,
                              cursor = "hand2"
                              ).grid(row = 1, column = 0, sticky = N+E+S+W, pady = 10, padx = 10)

    business = Button(subjects_f,
                              text = "BUSINESS",
                              command = inop,
                              font = (Font_1, 25, "bold"),
                              background = Contrast,
                              fg = "White",
                              activebackground = Contrast_Light,
                              border = 0,
                              cursor = "hand2"
                              ).grid(row = 2, column = 0, sticky = N+E+S+W, pady = 10, padx = 10)

    chemistry = Button(subjects_f,
                              text = "CHEMISTRY",
                              command = inop,
                              font = (Font_1, 25, "bold"),
                              background = Contrast,
                              fg = "White",
                              activebackground = Contrast_Light,
                              border = 0,
                              cursor = "hand2"
                              ).grid(row = 3, column = 0, sticky = N+E+S+W, pady = 10, padx = 10)

    english = Button(subjects_f,
                              text = " ENGLISH",
                              command = inop,
                              font = (Font_1, 25, "bold"),
                              background = Contrast,
                              fg = "White",
                              activebackground = Contrast_Light,
                              border = 0,
                              cursor = "hand2"
                              ).grid(row = 4, column = 0, sticky = N+E+S+W, pady = 10, padx = 10)

    maths = Button(subjects_f,
                              text = "MATHS",
                              command = inop,
                              font = (Font_1, 25, "bold"),
                              background = Contrast,
                              fg = "White",
                              activebackground = Contrast_Light,
                              border = 0,
                              cursor = "hand2"
                              ).grid(row = 0, column = 1, sticky = N+E+S+W, pady = 10, padx = 10)

    media = Button(subjects_f,
                              text = "MEDIA",
                              command = inop,
                              font = (Font_1, 25, "bold"),
                              background = Contrast,
                              fg = "White",
                              activebackground = Contrast_Light,
                              border = 0,
                              cursor = "hand2"
                              ).grid(row = 1, column = 1, sticky = N+E+S+W, pady = 10, padx = 10)

    physics = Button(subjects_f,
                              text = "PHYSICS",
                              command = inop,
                              font = (Font_1, 25, "bold"),
                              background = Contrast,
                              fg = "White",
                              activebackground = Contrast_Light,
                              border = 0,
                              cursor = "hand2"
                              ).grid(row = 2, column = 1, sticky = N+E+S+W, pady = 10, padx = 10)

    all_button = Button(subjects_f,
                              text = "ALL",
                              command = inop,
                              font = (Font_1, 37, "bold"),
                              background = Contrast,
                              fg = "White",
                              activebackground = Contrast_Light,
                              border = 0,
                              cursor = "hand2"
                              ).grid(row = 3, rowspan = 2, column = 1, sticky = N+E+S+W, pady = 10, padx = 10)

    subjects_f.grid(row = 2, column = 0, columnspan = 5, sticky = N+E+S+W)
    main_f.pack(fill = "both", expand = True)

select_subject()
select.mainloop()