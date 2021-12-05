from tkinter import *
from quiz_brain import QuizBrain

COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=COLOR)

        self.score_lbl = Label(text="Score: 0", fg="white", bg=COLOR, font=("Arial", 20, "normal"))
        self.score_lbl.grid(row=0, column=1)

        self.canvas = Canvas(width=400, height=350, bg="white")
        self.question_text = self.canvas.create_text(200, 175,
                                                     width=350,
                                                     text="Starting text",
                                                     font=("Arial", 20, "italic"),
                                                     fill=COLOR)
        self.canvas.grid(pady=50, row=1, column=0, columnspan=2)

        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, bd=0, highlightthickness=0, command=self.false_click)
        self.false_btn.grid(row=2, column=1)

        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, bd=0, highlightthickness=0, command=self.true_click)
        self.true_btn.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            next_q = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=next_q)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz.\n"
                                                            f"Your final score is: {self.quiz.score}/{self.quiz.question_number}")
            self.true_btn.config(state=DISABLED)
            self.false_btn.config(state=DISABLED)

    def true_click(self):
        self.action_on_response(self.quiz.check_answer("True"))

    def false_click(self):
        self.action_on_response(self.quiz.check_answer("False"))

    def action_on_response(self, result):
        if result:
            self.score_lbl.config(text=f"Score: {self.quiz.score}")
            self.canvas.configure(bg="#7CFC00")
        else:
            self.canvas.configure(bg="#DB7093")
        self.window.after(1000, self.get_next_question)
