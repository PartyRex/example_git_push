import requests
import random
from similar_text import similar_text

response = requests.get('http://jservice.io/api/clues?category=218').json()

#print(response)

#create a jeopardy game. 


#### LEVEL 1

# 1. Print out just the first item in the entire response.

#print(response[1])

# 2. Print out just the question of the first item in the entire response. 
# > You might notice that each of the dictionary keys has the letter u in front of it - this just means the string that follows is represented in Unicode, and it won't affect your code in any way today. You can igore the u.

# print(response[0]["question"])
# print(len(response))
# # 3. Refactor your code so that it prints out a random question, not just the first one every time.

# print(response[(random.randint(0, 100))]["question"])

# 4. Now, get some user input after the question. If what they type matches the answer, print a "congratulations!" message of some sort. If it doesn't match, print a "sorry" message of some sort.
#     * It's important to think about how specific Python's matching will be. If the user types "gorge" but the correct answer is "Gorge.", then the user will get the question wrong. *Consider finding a way of making your program responsive to small variations in capitalization or punctuation.*
    
# 5. If you get it wrong, you probably still want to know the right answer - it can be so frustrating if you were sure you were right. If the user gets it wrong, print out a message that tells them what the correct answer really was.

# selected=random.randint(0,100)
# question=[response][selected]["question"]
# answer=response[selected]["answer"]

# selected_question = input("Please select what number (0-100) of question you'd like: ")
# selected_question=int(selected_question)
# print("Your question is: " + response[selected_question]["question"])
# user_answer = input("What is your answer? ")
# if user_answer == response[selected_question]["answer"]:
#     print("You're right! Congratulations!")
# else:
#     print("You're wrong, but the right answer was " + response[selected_question]["answer"])



# #### LEVEL 2

# 6. Wrap this game in a loop so the user can play multiple rounds.

# def game(number):
#     for x in range(0, number):
#         selected_question = input("Please select what number (0-100) of question you'd like: ")
#         selected_question=int(selected_question)
#         print("Your question is: " + response[selected_question]["question"])
#         user_answer = input("What is your answer? ")
#         if user_answer == response[selected_question]["answer"]:
#             print("You're right! Congratulations!")
#         else:
#             print("You're wrong, but the right answer was " + response[selected_question]["answer"])
#     print("Game Over!")
#     return "Your game has been completed " + str(number) + " times."

# trials = input("How many times do you want to play? ")
# game(int(trials))

# 7. Create a score variable:
#     * If the user gets a question right, increase their score by the point value of the question.
#     * If the user gets a question wrong, decrease their score by the point value of the question.
#     * Print out their score after each round.

# def scored_game(number):
#     score=0
#     for x in range(0, number):
#         print("Your score is " + str(score))
#         selected_question = input("Please select what number (0-100) of question you'd like: ")
#         selected_question=int(selected_question)
#         print("Your question is: " + response[selected_question]["question"])
#         user_answer = input("What is your answer? ")
#         if user_answer == response[selected_question]["answer"]:
#             print("You're right! Congratulations!")
#             score+=response[selected_question]["value"]
#         else:
#             print("You're wrong, but the right answer was " + response[selected_question]["answer"])
#             score-=response[selected_question]["value"]
#     print("Game Over! You finished with a score of " + str(score))
#     return "Your game has been completed " + str(number) + " times."

# trials = input("How many times do you want to play? ")
# scored_game(int(trials))


# #### LEVEL 3

# 8. One of the most frustrating parts of this game is missing an answer due to typos, spelling errors, capitalization mismatches, or unexpected punctuation. Some of this is relatively easy to fix with Python's core methods, but there is no core function to show that "george" and "gorge" are SO CLOSE that the user probably actually knew the answer.
#     * There's a library called [similar-text](https://pypi.org/project/similar_text/) that will let us examine how similar two strings are.
#     * Install that library, import it at the top of your program, and then look at the documentation to figure out how to use it.
#     * If the user's answer is really close to the real answer, let them know that they almost have it, but that they may want to type it more carefully.
#     * It may also be beneficial to consider a way of recognizing that "Grapes of Wrath" and "The Grapes of Wrath" would be considered a mismatch. Are you going to give the user another chance if all they're missing is a small word like "the"?

# ![Jeopardy Board](jBoard.jpg)

# def advanced_scored_game(number):
#     score=0
#     for x in range(0, number):
#         print("Your score is " + str(score))
#         selected_question = input("Please select what number (0-100) of question you'd like: ")
#         selected_question=int(selected_question)
#         print("Your question is: " + response[selected_question]["question"])
#         user_answer = input("What is your answer? ")
#         #check to see if exactly equal
#         if user_answer.lower() == response[selected_question]["answer"].lower():
#             print("You're right! Congratulations!")
#             score+=response[selected_question]["value"]
#         #check to see if value is within 30% similar
#         elif (similar_text(user_answer.lower(), response[selected_question]["answer"].lower())>=30):
#                 print(str(similar_text(user_answer.lower(),  response[selected_question]["answer"].lower())))
#                 try_two=input("Try again. Are you sure your answer is correct? ")
#                 if try_two.lower()==response[selected_question]["answer"].lower():
#                     score+=response[selected_question]["value"]
#                     print("Good job, you got the answer right!")
#                 else:
#                     print("Sorry, you're wrong.")
#                     score-=response[selected_question]["value"]
#         else:
#             print("You're wrong, but the right answer was " + response[selected_question]["answer"])
#             score-=response[selected_question]["value"]
#     print("Game Over! You finished with a score of " + str(score))
#     return "Your game has been completed " + str(number) + " times."

# trials = input("How many times do you want to play? ")
# advanced_scored_game(int(trials))


# #### LEVEL 4

# 9. The real jeopardy board has six categories, and 5 questions per category of increasing difficulty. That's 30 unique questions. The player also gets to CHOOSE which questions to answer and when.
#     * Find a way to load all 30 questions, and then offer the user a choice of which question to attempt.
#     * Find a way to print out a visual representation of the board in the console.
#       * Bonus: print the score at the top or bottom of the board.
#     * Keep track of which questions the user has already tried, and throw them an error if they try to access the same question twice.


"""

MEGA SCIENCE JEOPARDY

"""

#start by figuring out a way to load 6 categories

#randomly select 5 questions for each category