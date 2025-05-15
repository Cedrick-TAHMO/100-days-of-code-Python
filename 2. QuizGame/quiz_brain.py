class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_List = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_List)


    def next_question(self):
        question = self.question_List[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True or False)?: ")
        self.check_answer(user_answer, question.answer)
        self.final_percentage()

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Amazing job that was Right!!")
            print(f"Your score: {self.score}/{self.question_number}")
        else:
            print("Unfortunately that was Wrong")
            print(f"Your score: {self.score}/{self.question_number}")
        print(f"The correct answer was: {correct_answer} \n")

    def final_percentage(self):

        if self.still_has_question():
            pass
        else:
            percentage = self.score/self.question_number
            percentage = round(percentage*100, 2)
            print("You've completed the quiz!!")
            print(f"Your success percentage: {percentage}%")

