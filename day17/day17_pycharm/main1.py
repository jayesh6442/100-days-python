from qustions_model import Questions
from data import question_data
from quiz_brain import QuiaBrain
question_bank=[]
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Questions(question_text,question_answer)
    question_bank.append(new_question)


quiz = QuiaBrain(question_bank)
quiz.next_question()