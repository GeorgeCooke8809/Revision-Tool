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

select_window_frame = Frame(select)

first_run = 0

def inop(): #for when a button isn't programmed yet
    return ctypes.windll.user32.MessageBoxW(0, "INOP", "INOP", 4)

def select_subject(): #select subject page for going into questions
    global subjects_main_f, subjects_f,papers_main_f

    clear_page()

    select.title("Select Subject:")

    subjects_main_f = Frame(select_window_frame) #blue frame on canva
    subjects_main_f.rowconfigure(0, weight = 1, minsize = 75)
    subjects_main_f.rowconfigure(1, weight = 1, minsize = 75)
    subjects_main_f.rowconfigure(2, weight = 375, minsize = 495)
    subjects_main_f.rowconfigure(3, weight = 0)
    subjects_main_f.rowconfigure(4, weight = 0)

    subjects_main_f.columnconfigure(0, weight = 1)
    subjects_main_f.columnconfigure(1, weight = 1)
    subjects_main_f.columnconfigure(2, weight = 1)
    subjects_main_f.columnconfigure(3, weight = 1)
    subjects_main_f.columnconfigure(4, weight = 1)

    papers_main_f = Frame(select_window_frame)
    papers_main_f.pack()

    back = Button(subjects_main_f,
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

    title = Label(subjects_main_f,
                  text = "Select Subject:",
                  font = (Font_1, 65, "bold"),
                  anchor = "w",
                  padx = 10,
                  wrap = True,
                  wraplength = 1000,
                  justify = "left"
                  ).grid(row = 1, column = 0, columnspan = 5, sticky = N+E+S+W)

    subjects_f = Frame(subjects_main_f)#green frame on canve
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
                              command = computer_science_papers,
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
                              command = clear_page,
                              font = (Font_1, 37, "bold"),
                              background = Contrast,
                              fg = "White",
                              activebackground = Contrast_Light,
                              border = 0,
                              cursor = "hand2"
                              ).grid(row = 3, rowspan = 2, column = 1, sticky = N+E+S+W, pady = 10, padx = 10)

    subjects_f.grid(row = 2, column = 0, columnspan = 5, sticky = N+E+S+W)
    subjects_main_f.pack(fill = "both", expand = True)
    select_window_frame.pack(fill = "both", expand = "true")

def clear_page():
    global first_run

    if first_run >= 1:
        select_window_frame.pack_forget()
        subjects_main_f.pack_forget()
        subjects_f.pack_forget()
        papers_main_f.pack_forget()

    first_run = first_run + 1

def computer_science_papers():
    global papers_main_f

    select.title("Select Paper:")

    clear_page()

    papers_main_f = Frame(select_window_frame) #blue frame on canva
    papers_main_f.rowconfigure(0, weight = 1, minsize = 75)
    papers_main_f.rowconfigure(1, weight = 1, minsize = 75)
    papers_main_f.rowconfigure(2, weight = 100)
    papers_main_f.rowconfigure(3, weight = 100)
    papers_main_f.rowconfigure(4, weight = 100)

    papers_main_f.columnconfigure(0, weight = 1)
    papers_main_f.columnconfigure(1, weight = 1)
    papers_main_f.columnconfigure(2, weight = 1)
    papers_main_f.columnconfigure(3, weight = 1)
    papers_main_f.columnconfigure(4, weight = 1)

    back = Button(papers_main_f,
                  text = "<- BACK",
                  command = select_subject,
                  font = (Font_1, 25, "bold"),
                  background = Contrast,
                  fg = "White",
                  activebackground = Contrast_Light,
                  pady = 10,
                  border = 0,
                  cursor = "hand2"
                  ).grid(row = 0, column = 0, sticky = N+E+S+W, pady = 10, padx = 10)

    title = Label(papers_main_f,
                  text = "Select Paper:",
                  font = (Font_1, 65, "bold"),
                  anchor = "w",
                  padx = 10,
                  wrap = True,
                  wraplength = 1000,
                  justify = "left"
                  ).grid(row = 1, column = 0, columnspan = 5, sticky = N+E+S+W)

    all_papers = Button(papers_main_f,
                  text = "ALL",
                  command = inop,
                  font = (Font_1, 25, "bold"),
                  background = Contrast,
                  fg = "White",
                  activebackground = Contrast_Light,
                  pady = 10,
                  border = 0,
                  cursor = "hand2"
                  ).grid(row = 2, column = 0, columnspan = 5, sticky = N+E+S+W, pady = 10, padx = 10)

    paper_1 = Button(papers_main_f,
                  text = "PAPER 1",
                  command = inop,
                  font = (Font_1, 25, "bold"),
                  background = Contrast,
                  fg = "White",
                  activebackground = Contrast_Light,
                  pady = 10,
                  border = 0,
                  cursor = "hand2"
                  ).grid(row = 3, column = 0, columnspan = 5, sticky = N+E+S+W, pady = 10, padx = 10)

    paper_2 = Button(papers_main_f,
                  text = "PAPER 2",
                  command = inop,
                  font = (Font_1, 25, "bold"),
                  background = Contrast,
                  fg = "White",
                  activebackground = Contrast_Light,
                  pady = 10,
                  border = 0,
                  cursor = "hand2"
                  ).grid(row = 4, column = 0, columnspan = 5, sticky = N+E+S+W, pady = 10, padx = 10)

    papers_main_f.pack(fill = "both", expand = True)
    select_window_frame.pack(fill = "both", expand = True)

select_subject()
select.mainloop()