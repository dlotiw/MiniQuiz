from typing import List
from typing import Any
from dataclasses import dataclass
import html

@dataclass
class Result:
    category: str
    type: str
    difficulty: str
    question: str
    correct_answer: str
    incorrect_answer: str

    @staticmethod
    def from_dict(obj: Any) -> 'Result':
        _category = str(obj.get("category"))
        _type = str(obj.get("type"))
        _difficulty = str(obj.get("difficulty"))
        _question = html.unescape(str(obj.get("question")))
        _correct_answer = str(obj.get("correct_answer"))
        #Using only true/false questions so only one wrong answer
        _incorrect_answer = str(obj.get("incorrect_answers")[0])
        return Result(_category, _type, _difficulty, _question, _correct_answer, _incorrect_answer)

@dataclass
class Root:
    response_code: int
    results: List[Result]

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _response_code = int(obj.get("response_code"))
        _results = [Result.from_dict(y) for y in obj.get("results")]
        return Root(_response_code, _results)
