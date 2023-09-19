import requests
from data_model import Root
from quiz import Quiz
from ui import QuizUI

def main():
    parameters = {
        'amount': 10,
        'type': 'boolean',
    }
    trivia = requests.get("https://opentdb.com/api.php?",params=parameters)
    dane_tr = Root.from_dict(trivia.json())

    quiz = Quiz(dane_tr.results)
    screen = QuizUI(question=quiz)

    screen.mainloop()

if __name__ == '__main__':
    main()