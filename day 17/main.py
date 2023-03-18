from  question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
# lines = 0
# sentences_out = False

# while sentences_out == False:
#     new_q = Question(question_data[lines]["text"],question_data[lines]["answer"])
#     Question_bank.append(new_q.text + new_q.answer)
#     lines +=1
#     if lines == 12:
#         sentences_out =True

# print(Question_bank)

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

# while quiz.still_has_questions() == True:
#     quiz.next_question() 

while quiz.still_has_questions() :
    quiz.next_question()
    

print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")