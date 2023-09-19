from tkinter import *
from tkinter import messagebox
from quiz import Quiz

THEME_COLOR = "#375362"

class QuizUI:
    
    def __init__(self, question: Quiz) -> 'QuizUI':
        self.question = question
        self.window = Tk()    
        self.window.title("MiniQuiz")
        self.window.config(padx=20,pady=20,background=THEME_COLOR)
        #Score
        self.score_label = Label(text=f"Score: {self.question.score}/{len(self.question.question_list)}")
        self.score_label.config(padx=20,pady=20,fg="white",bg=THEME_COLOR,font=("Arial",20,"bold"))
        self.score_label.grid(row=0,column=1)

        #QuizQuestion
        self.canvas = Canvas(width=400,height=250,background='white',highlightthickness=0,)
        self.question_text = self.canvas.create_text(200,125,
                                                text=question.current_question.question,fill=THEME_COLOR,
                                                font=("Ariel",20,"italic"),width=380)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        #Wrong button
        self.wrong_image = PhotoImage(file="MiniQuiz/images/false.png")
        self.wrong_button = Button(image=self.wrong_image,background=THEME_COLOR,
                                   highlightthickness=0,activebackground=THEME_COLOR,bd=0,command=self.wrong_button_click)
        self.wrong_button.grid(row=2,column=1)

        #Right button
        self.right_image = PhotoImage(file="MiniQuiz/images/true.png")
        self.right_button = Button(image=self.right_image,background=THEME_COLOR,
                                   highlightthickness=0,activebackground=THEME_COLOR,bd=0,command=self.right_button_click)
        self.right_button.grid(row=2,column=0)
        

    def add_score(self):
        self.score_label.config(text=f"Score: {self.question.score}/{len(self.question.question_list)}")
        

    def wrong_button_click(self):
        if self.question.check_answer('False'):
            self.add_score()
        if self.question.next_question():
            self.canvas.itemconfig(self.question_text,text=self.question.current_question.question)
        else:
            self.ending()
        
    
    def right_button_click(self):
        if self.question.check_answer('True'):
            self.add_score()
        if self.question.next_question():
            self.canvas.itemconfig(self.question_text,text=self.question.current_question.question)
        else:
            self.ending()
    
    def ending(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.window.destroy()

    def mainloop(self):
        self.window.mainloop()