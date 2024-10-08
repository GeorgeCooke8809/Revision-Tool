from random import randint
import sqlite3
from tkinter import *
import ctypes
import pygame

pygame.init()

correct = pygame.mixer.Sound("Correct.mp3")
incorrect = pygame.mixer.Sound("Incorrect.mp3")

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

guess_no = 0

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

    subject = "ComputerScience"

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
                  command = computer_science_paper_2,
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
                  command = lambda: questions(1.1),
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
                  command = lambda: questions(1.2),
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
                  command = lambda: questions(1.3),
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
                  command = lambda: questions(1.4),
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
              command = lambda: questions(1.5),
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
              command = lambda: questions(1.6),
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

def computer_science_paper_2():
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
                  ).grid(row = 0, column = 0, columnspan = 2, sticky = N+E+S+W, pady = 5, padx = 10)

    topic_1 = Button(topics_f,
                  text = "2.1 - ALGORITHMS",
                  command = lambda: questions(2.1),
                  font = (Font_1, 25, "bold"),
                  background = Contrast,
                  fg = "White",
                  activebackground = Contrast_Light,
                  pady = 10,
                  border = 0,
                  cursor = "hand2",
                  wraplength = 700
                  ).grid(row = 1, column = 0, sticky = N+E+S+W, pady = 5, padx = 10)

    topic_2 = Button(topics_f,
                  text = "2.2 - PROGRAMMING FUNDAMENTALS",
                  command = lambda: questions(2.2),
                  font = (Font_1, 25, "bold"),
                  background = Contrast,
                  fg = "White",
                  activebackground = Contrast_Light,
                  pady = 10,
                  border = 0,
                  cursor = "hand2",
                  wraplength = 700
                  ).grid(row = 1, column = 1, sticky = N+E+S+W, pady = 5, padx = 10)

    topic_3 = Button(topics_f,
                  text = "2.3 - PRODUCING ROBUST PROGRAMS",
                  command = lambda: questions(2.3),
                  font = (Font_1, 25, "bold"),
                  background = Contrast,
                  fg = "White",
                  activebackground = Contrast_Light,
                  pady = 10,
                  border = 0,
                  cursor = "hand2",
                  wraplength = 700
                  ).grid(row = 2, column = 0, sticky = N+E+S+W, pady = 5, padx = 10)

    topic_4 = Button(topics_f,
                  text = "2.4 BOOLEAN LOGIC",
                  command = lambda: questions(2.4),
                  font = (Font_1, 25, "bold"),
                  background = Contrast,
                  fg = "White",
                  activebackground = Contrast_Light,
                  pady = 10,
                  border = 0,
                  cursor = "hand2",
                  wraplength = 700
                  ).grid(row = 2, column = 1, sticky = N+E+S+W, pady = 5, padx = 10)

    topic_5 = Button(topics_f,
              text = "2.5 - PROGRAMMING LANGUAGES & IDES",
              command = lambda: questions(2.5),
              font = (Font_1, 25, "bold"),
              background = Contrast,
              fg = "White",
              activebackground = Contrast_Light,
              pady = 10,
              border = 0,
              cursor = "hand2",
              wraplength = 700
              ).grid(row = 3, column = 0, sticky = N+E+S+W, pady = 5, padx = 10)

    topics_f.grid(row = 2, column = 0, columnspan = 5, sticky = N+E+S+W)
    topics_main_f.pack(fill = "both", expand = True)
    select_window_frame.pack(fill = "both", expand = True)
    
def questions(topic):
    global subject, entry, answer, box, question, question_frame, question_window, topic_q


    select.destroy()

    question_window = Tk()
    question_window.geometry("1190x400")
    question_window.title("Questions")
    question_window.resizable(width = False, height = False)

    data = sqlite3.connect("Questions.db")
    cursor = data.cursor()

    cursor.execute("SELECT * FROM %s where Topic = %s" % (subject, topic))
    question_options = cursor.fetchall()
    question_number = randint(0,(len(question_options)-1))

    question_string = question_options[question_number]
    topic_q = question_string[0]
    paper = question_string[1]
    question = question_string[2]
    answer = question_string[3]

    question_frame = Frame(question_window)

    question_frame.rowconfigure(0, weight = 1, minsize = 50)
    question_frame.rowconfigure(1, weight = 1, minsize = 150)
    question_frame.rowconfigure(2, weight = 1, minsize = 75)
    question_frame.rowconfigure(3, weight = 1, minsize = 75)

    top_string = str(topic_q) + " (" + str(subject) + " - " + str(paper) + ")"
    top_string = Label(question_frame,
                      text = top_string,
                      font = (Font_2, 25, "italic"),
                      anchor = "w",
                      padx = 10,
                      wrap = True,
                      wraplength = 1000,
                      justify = "left"
                      ).grid(row = 0, column = 0, sticky = N+E+S+W)

    question_label = Label(question_frame,
                      text = question,
                      font = (Font_1, 35, "bold"),
                      anchor = "nw",
                      padx = 10,
                      wrap = True,
                      wraplength = 1000,
                      justify = "left"
                      ).grid(row = 1, column = 0, sticky = N+E+S+W)

    box = Entry(question_frame,
                  font = (Font_1, 30),
                  width = 55,
                  justify = "center",
                  bg = Contrast_Light,
                  border = 0
                  )
    box.grid(row = 2, column = 0, sticky = N+E+S+W)

    box.bind("<Return>", submit_command)

    submit = Button(question_frame,
                  text = "SUBMIT",
                  command = submit_command,
                  font = (Font_1, 30, "bold"),
                  background = Contrast,
                  fg = "White",
                  activebackground = Contrast_Light,
                  border = 0,
                  cursor = "hand2",
                  wraplength = 700
                  ).grid(row = 3, column = 0, sticky = N+E+S+W)

    question_frame.pack(fill = "both", expand = "true")
    question_window.mainloop()

def submit_command(event=None):
    global guess_no
    guess = box.get()

    if guess.upper() == answer.upper():
        question_label = Label(question_frame,
                      text = question,
                      font = (Font_1, 35, "bold"),
                      fg = "Green",
                      anchor = "nw",
                      padx = 10,
                      wrap = True,
                      wraplength = 1000,
                      justify = "left"
                      ).grid(row = 1, column = 0, sticky = N+E+S+W)
        question_frame.pack_forget()
        question_frame.pack(fill = "both", expand = "true")
        guess_no = 0
        correct.play()
        new_question(topic_q)
    else:
        incorrect.play()
        guess_no = guess_no + 1

        if guess_no == 3:
            new_question(topic_q)
            guess_no = 0

def new_question(topic):
    data = sqlite3.connect("Questions.db")
    cursor = data.cursor()

    cursor.execute("SELECT * FROM %s where Topic = %s" % (subject, topic))
    question_options = cursor.fetchall()
    question_number = randint(0,(len(question_options)-1))

    question_string = question_options[question_number]
    topic = question_string[0]
    paper = question_string[1]
    question = question_string[2]
    answer = question_string[3]

    print(question_string)

    top_string = str(topic) + " (" + str(subject) + " - " + str(paper) + ")"
    top_string = Label(question_frame,
                      text = top_string,
                      font = (Font_2, 25, "italic"),
                      anchor = "w",
                      padx = 10,
                      wrap = True,
                      wraplength = 1000,
                      justify = "left"
                      ).grid(row = 0, column = 0, sticky = N+E+S+W)

    question_label = Label(question_frame,
                      text = question,
                      font = (Font_1, 35, "bold"),
                      anchor = "nw",
                      padx = 10,
                      wrap = True,
                      wraplength = 1000,
                      justify = "left"
                      ).grid(row = 1, column = 0, sticky = N+E+S+W)

    submit = Button(question_frame,
                  text = "SUBMIT",
                  command = submit_command,
                  font = (Font_1, 30, "bold"),
                  background = Contrast,
                  fg = "White",
                  activebackground = Contrast_Light,
                  border = 0,
                  cursor = "hand2",
                  wraplength = 700
                  ).grid(row = 3, column = 0, sticky = N+E+S+W)

    box.delete(0,END)

    question_frame.pack(fill = "both", expand = "true")


select_subject() #decides starting page
select.mainloop()