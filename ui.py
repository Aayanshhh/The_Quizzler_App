from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some Questions",
            fill=THEME_COLOR,
            font=("Ariel", 20, "italic"),
            width=280  # Corrected alignment
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Quiz Completed")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")  # Fixed typo here

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        print(f"True button pressed, is_right: {is_right}")  # Debug statement
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        print(f"False button pressed, is_right: {is_right}")  # Debug statement
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        print(f"Giving feedback, is_right: {is_right}")  # Debug statement
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


if __name__ == "__main__":
    # Create a mock QuizBrain object for testing purposes
    class MockQuizBrain:
        def __init__(self):
            self.score = 0
            self.questions = ["Is the sky blue?", "Is water wet?"]
            self.question_index = 0

        def still_has_questions(self):
            return self.question_index < len(self.questions)

        def next_question(self):
            question = self.questions[self.question_index]
            self.question_index += 1
            return question

        def check_answer(self, answer):
            return answer == "True"

    quiz_brain = MockQuizBrain()
    quiz_ui = QuizInterface(quiz_brain)
