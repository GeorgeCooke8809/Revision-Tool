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

select_window_frame = Frame(select) # frame that everything is put into to make clearing simpler

first_run = 0 # checks if its the first time going back so that it doesn't break

def inop(): #for when a button isn't programmed yet
    return ctypes.windll.user32.MessageBoxW(0, "INOP", "INOP", 4)

def select_subject(): #select subject page for going into questions
    global subjects_main_f, subjects_f,papers_main_f, topics_main_f

    clear_page()

    select.title("Select Subject")

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

    papers_main_f = Frame(select_window_frame) #declares the papers main frame for next window so doesn't come as undefined when clearing
    papers_main_f.pack()

    topics_main_f = Frame(select_window_frame)
    topics_main_f.pack()

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
        topics_main_f.pack_forget()

    first_run = first_run + 1

def computer_science_papers(): # select which paper of the computer science course to study
    global papers_main_f, subject

    subject = "Computer Science"

    select.title("Select Paper")

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
                  ).grid(row = 0, column = 0, sticky = N+E+S+W, pady = 10, padx = 10) #button to return to subjects page

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
                  command = computer_science_paper_1,
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

def computer_science_paper_1():
    global topics_main_f

    select.title("Select Topic")

    clear_page()

    topics_main_f = Frame(select_window_frame)
    topics_main_f.rowconfigure(0, weight = 1, minsize = 75)
    topics_main_f.rowconfigure(1, weight = 1, minsize = 75)
    topics_main_f.rowconfigure(2, weight = 1000)

    topics_main_f.columnconfigure(0, weight = 1)
    topics_main_f.columnconfigure(1, weight = 1)
    topics_main_f.columnconfigure(2, weight = 1)
    topics_main_f.columnconfigure(3, weight = 1)
    topics_main_f.columnconfigure(4, weight = 1)

    back = Button(topics_main_f,
                  text = "<- BACK",
                  command = computer_science_papers,
                  font = (Font_1, 25, "bold"),
                  background = Contrast,
                  fg = "White",
                  activebackground = Contrast_Light,
                  pady = 10,
                  border = 0,
                  cursor = "hand2"
                  ).grid(row = 0, column = 0, sticky = N+E+S+W, pady = 10, padx = 10) #button to return to subjects page

    title = Label(topics_main_f,
                  text = "Select Topic:",
                  font = (Font_1, 65, "bold"),
                  anchor = "w",
                  padx = 10,
                  wrap = True,
                  wraplength = 1000,
                  justify = "left"
                  ).grid(row = 1, column = 0, columnspan = 5, sticky = N+E+S+W)

    topics_f = Frame(topics_main_f)
    topics_f.rowconfigure(0, weight = 1, minsize = 125)
    topics_f.rowconfigure(1, weight = 1, minsize = 125)
    topics_f.rowconfigure(2, weight = 1, minsize = 125)
    topics_f.rowconfigure(3, weight = 1, minsize = 125)
    topics_f.rowconfigure(4, weight = 1, minsize = 125)
    topics_f.rowconfigure(5, weight = 1, minsize = 125)

    topics_f.columnconfigure(0, weight = 1, minsize = 707)
    topics_f.columnconfigure(1, weight = 1, minsize = 707)

    all_topics = Button(topics_f,
                  text = "ALL",
                  command = inop,
                  font = (Font_1, 25, "bold"),
                  background = Contrast,
                  fg = "White",
                  activebackground = Contrast_Light,
                  pady = 10,
                  border = 0,
                  cursor = "hand2",
                  ).grid(row = 0, column = 0, columnspan = 2, sticky = N+E+S+W, pady = 10, padx = 10)

    topic_1 = Button(topics_f,
                  text = "1.1 - SYSTEMS ARCHITECTURE",
                  command = inop,
                  font = (Font_1, 25, "bold"),
                  background = Contrast,
                  fg = "White",
                  activebackground = Contrast_Light,
                  pady = 10,
                  border = 0,
                  cursor = "hand2",
                  wraplength = 700
                  ).grid(row = 1, column = 0, sticky = N+E+S+W, pady = 10, padx = 10)

    topic_2 = Button(topics_f,
                  text = "1.2 - MEMORY & STORAGE",
                  command = inop,
                  font = (Font_1, 25, "bold"),
                  background = Contrast,
                  fg = "White",
                  activebackground = Contrast_Light,
                  pady = 10,
                  border = 0,
                  cursor = "hand2",
                  wraplength = 700
                  ).grid(row = 1, column = 1, sticky = N+E+S+W, pady = 10, padx = 10)

    topic_3 = Button(topics_f,
                  text = "1.3 - COMPUTER NETWORKS, CONTROLS & PROTOCOLS",
                  command = inop,
                  font = (Font_1, 25, "bold"),
                  background = Contrast,
                  fg = "White",
                  activebackground = Contrast_Light,
                  pady = 10,
                  border = 0,
                  cursor = "hand2",
                  wraplength = 700
                  ).grid(row = 2, column = 0, sticky = N+E+S+W, pady = 10, padx = 10)

    topic_4 = Button(topics_f,
                  text = "1.4 - NETWORK SECURITY",
                  command = inop,
                  font = (Font_1, 25, "bold"),
                  background = Contrast,
                  fg = "White",
                  activebackground = Contrast_Light,
                  pady = 10,
                  border = 0,
                  cursor = "hand2",
                  wraplength = 700
                  ).grid(row = 2, column = 1, sticky = N+E+S+W, pady = 10, padx = 10)

    topic_5 = Button(topics_f,
              text = "1.5 - SYSTEMS SOFTWARE",
              command = inop,
              font = (Font_1, 25, "bold"),
              background = Contrast,
              fg = "White",
              activebackground = Contrast_Light,
              pady = 10,
              border = 0,
              cursor = "hand2",
              wraplength = 700
              ).grid(row = 3, column = 0, sticky = N+E+S+W, pady = 10, padx = 10)

    topic_6 = Button(topics_f,
              text = "1.6 - ETHICAL, LEGAL, CULTURAL AND ENVIRONMENTAL ASPECTS",
              command = questions(1.6),
              font = (Font_1, 25, "bold"),
              background = Contrast,
              fg = "White",
              activebackground = Contrast_Light,
              pady = 10,
              border = 0,
              cursor = "hand2",
              wraplength = 700
              ).grid(row = 3, column = 1, sticky = N+E+S+W, pady = 10, padx = 10)

    topics_f.grid(row = 2, column = 0, columnspan = 5, sticky = N+E+S+W)
    topics_main_f.pack(fill = "both", expand = True)
    select_window_frame.pack(fill = "both", expand = True)
    
def questions(topic):
    global subject




select_subject() #decides starting page
select.mainloop()