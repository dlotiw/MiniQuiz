import requests
from question_model import Question
from data import Root
from quiz_brain import QuizBrain


parameters = {
    'amount': 10,
    'type': 'boolean',
}
trivia = requests.get("https://opentdb.com/api.php?",params=parameters)


dane_tr = Root.from_dict(trivia.json())

quiz = QuizBrain(dane_tr.results)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
