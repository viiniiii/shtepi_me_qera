question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]
class quiz_brain:
    def __init__(self,question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer,current_question.answer)
    def check_answer(self, user_answer, current_question.answer):
        if user_answer.lower() == current_question.answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong!")
        print(f"The correct answer was {current_question.answer}")
        print(f"Your score is {self.score}/{self.question_number}")
    def still_has_question(self):
        return self.question_number < len(self.question_list)
    

class question:
    def __init__(self,text,answer):
        self.text = text
        self.answer = answer
question_bank = []
for key in question_data:
    question_bank.append(question(key['text'],key['answer']))


quiz = quiz_brain(question_bank)

while quiz.still_has_question():
    quiz.next_question()