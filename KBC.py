import random
print('''RULES TO PLAY THE GAME:
      1. There are total 15 questions and 1 special question.
      2. Each question has 4 options.
      3. Right answer will be the key to unlock the next question.
      4. Wrong answer will end the game.
      5. You can use 3 lifelines.
      6. Moving with the game, question difficulty will increase.
      7. You can quit the game at any time.
      8. There are total 3 Checkpoints at 5, 10 and 15 questions.''')
print('''LIFELINES 
      1. 50-50: Two wrong options will be removed.
      2. Ask a friend: You can ask your friend for help.
      3. Flip the question: You can change the question.''')

print('''PRIZE MONEY FOR EACH QUESTION
      1. 1000
      2. 2000
      3. 3000
      4. 5000
      5. 10000
      6. 20000
      7. 40000
      8. 80000
      9. 160000
      10. 320000
      11. 640000
      12. 1250000
      13. 2500000
      14. 5000000
      15. 10000000
      16. 50000000''')
questions = ["1 What is the capital of Australia?",
             "2 Which planet is known as the Red Planet?",
             "3 What is the Chemcical Formula for Water?",
             "4 Which color is associated with Peace?",
             "5 Which is the largest Ocean of Earth?",
             "6 Which Scientist is reputed as a 'THIEF'?",
             "7 Which famous painter is known for his 'Mona Lisa'?",
             "8 who was the first Indian to win a Oscar?",
             "9 Which of these is a Professional Football League?",
             "10 If ice tuns into vapor, what is the process called?",
             "11 In total how many ways are there that can a batsman get out?"]


L = ['1st ', '2nd', '3rd' ,'4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th']



options = ['''A Melbourne    B Sydney
 C Canberra     D Perth ''','''A Earth    B Saturn
 C Mars     D Jupiter ''','''A H2O2    B H20
 C CO2     D H2''','''A RED     B BLUE
 C WHITE   D GREEN''','''A Atlantic Ocean     B Indian Ocean
 C Pacific Ocean      D Arctic Ocean''', '''A Einstein    B Newton
 C Tesla       D Edison''', '''A Picasso     B Van Gogh
 C Da Vinci    D Monet''','''A A.R. Rahman     B Gulzar
 C Kamal Hassan    D Lata Mangeshkar''','''A NBA     B NFL
 C ISL     D MLS''','''A Evaporation    B Condensation
 C Sublimation    D Freezing''','''A 5     B 10
 C 6     D 3''']


answers = ['C', 'C', 'B', 'C', 'C', 'D', 'C', 'A', 'C', 'C', 'B']


cans = ['Congratulations! You got the right answer', "That's the right answer, Congrats", "Bilkul Sahi Jawab",
         "agar aap koi doosra option choose krte to sayad aap nhi jeet pate\n, That's the right answer"]
wans = ["Sorry, but that's the wrong answer", "That's not the right answer, You Lose"]



for i in range(len(questions)):
    print('Your', L[i], "Question is on your screen:\n", questions[i])
    print("your Options are:\n",options[i])
    ans = input("Choose your option:").strip().upper()
    if ans == answers[i]:
        print(random.choice(cans))
    else:
        print(random.choice(wans))
        print("Game Over")
        break