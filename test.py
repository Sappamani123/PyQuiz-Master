from question_bank import quiz
print("All the best!")
print("There are 10 questions , Each question carries 1 mark and you have to score 80% to pass.")
print("**********")
score=0
def check_answers(user_answer,correct_answer):
    if user_answer==correct_answer:
        return True
    else:
        return False
for i in range(len(quiz)):
    print(quiz[i]["question"])
    for j in quiz[i]["options"]:
        print(j)
    guess=input("Enter your answer(A/B/C/D):").upper()
    is_correct=check_answers(guess,quiz[i]["answer"])
    if is_correct:
        print("COrrect answer")
        score+=1
    else:
        print("Wrong answer")
        print(f"Correct answer is {quiz[i]["answer"]}")
        print(f"Your current score is {score}/{i+1}")
print(f"Your final score is {score}")
percentage=(score/len(quiz))*100
print(f"The percentage you got is {percentage}%")
if percentage>=80:
    print(" Cogratulations! You passed the quiz")
else :
    print("Fail, Try again")
    print("You percentage is less than 80%")

