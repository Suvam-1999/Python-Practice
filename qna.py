# You store Q/A pairs, and the program quizzes the user.

# Concepts:
# 	•	Loops
# 	•	Functions
# 	•	Dictionary of Q&A
# 	•	Score counter

import random

questions_answer = {
    "What has to be broken before you can use it?" : "egg",
    "What gets wetter the more it dries?" : "towel",
    "What has hands but can not clap?" : "clock",
}


def run_quiz():     
     print("Game has started !!! \n Here is your first question below !!!")
     items = list(questions_answer.items())
     random.shuffle(items)
     total_score = 0
     for questions , correct_answer in items :
        print(f"Current score is : {total_score}")
        print("Questions : " )
        print (questions)
        user_answer = input("Answer : ").lower()
        if user_answer == correct_answer.lower():
            print("Correct! 🎉\n")
            total_score = total_score + 1
        else:
            print(f"Incorrect ❌. Correct answer is: {correct_answer}\n")
            
     print (f"Your total score is : {total_score}")
     print("Thankyou for playing the game")

print ("    !!!QNA Game for kids!!!   ")
buttons = int(input("Enter 1 to start \nEnter 2 to quit :"))
if buttons == 1:
    run_quiz()
elif buttons == 2 :
    print ('Thankyou for playing the game !!!')

else :
    print ("Invalid number")

        
        
        
      
