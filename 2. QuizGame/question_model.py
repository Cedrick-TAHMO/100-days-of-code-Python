class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

    def textfunc(self):
        return self.text

    def answerfunc(self):
        return self.answer

