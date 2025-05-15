import question_model
import data
from quiz_brain import QuizBrain

question_bank = []
for items in data.question_data:
    Quest = question_model.Question(items["text"], items["answer"])
    question_bank.append(Quest)

quiz = QuizBrain(question_bank)

while quiz.still_has_question() :
     quiz.next_question()
