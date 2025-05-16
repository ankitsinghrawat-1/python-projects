import random

print('''RULES TO PLAY THE GAME:
      1. There are total 15 questions.
      2. Each question has 4 options.
      3. Right answer will unlock the next question.
      4. Wrong answer will end the game.
      5. You can use 3 lifelines: 50-50, Ask a Friend, Flip the Question.
      6. You can quit the game at any time.
      7. There are checkpoints at 5, 10, and 15 questions.''')

points = ['1000', '2000', '3000', '5000', '10000', '20000', '40000', '80000', '160000', '320000', '640000',
          '1250000', '2500000', '5000000', '10000000', '50000000']

questions = [
    "1 What is the capital of Australia?",
    "2 Which planet is known as the Red Planet?",
    "3 What is the Chemical Formula for Water?",
    "4 Which color is associated with Peace?",
    "5 Which is the largest Ocean of Earth?",
    "6 Which Scientist is reputed as a 'THIEF'?",
    "7 Which famous painter is known for his 'Mona Lisa'?",
    "8 Who was the first Indian to win an Oscar?",
    "9 Which of these is a Professional Football League?",
    "10 If ice turns into vapor, what is the process called?",
    "11 In total, how many ways can a batsman get out?"
]

options = [
    '''A Melbourne    B Sydney
C Canberra     D Perth ''',
    '''A Earth    B Saturn
C Mars     D Jupiter ''',
    '''A H2O2    B H2O
C CO2     D H2''',
    '''A RED     B BLUE
C WHITE   D GREEN''',
    '''A Atlantic Ocean     B Indian Ocean
C Pacific Ocean      D Arctic Ocean''',
    '''A Einstein    B Newton
C Tesla       D Edison''',
    '''A Picasso     B Van Gogh
C Da Vinci    D Monet''',
    '''A A.R. Rahman     B Gulzar
C Kamal Hassan    D Lata Mangeshkar''',
    '''A NBA     B NFL
C ISL     D MLS''',
    '''A Evaporation    B Condensation
C Sublimation    D Freezing''',
    '''A 5     B 10
C 6     D 3'''
]

answers = ['A', 'C', 'B', 'C', 'C', 'D', 'C', 'A', 'C', 'C', 'B']
answer_text = ['Melbourne', 'Mars', 'H2O', 'White', 'Pacific Ocean', 'Edison', 'Da Vinci', 'A.R. Rahman', 'ISL', 'Sublimation', '10']

cans = ['Congratulations! You got the right answer', "That's the right answer, Congrats", "Bilkul Sahi Jawab"]
wans = ["Sorry, but that's the wrong answer", "That's not the right answer, You Lose"]

used_lifelines = {"50-50": False, "Ask a Friend": False, "Flip the Question": False}

def fifty_fifty(question_index):
    if used_lifelines["50-50"]:
        print("You have already used the 50-50 lifeline.")
        return
    used_lifelines["50-50"] = True
    correct_option = answers[question_index]
    all_options = ['A', 'B', 'C', 'D']
    incorrect_options = [opt for opt in all_options if opt != correct_option]
    removed_options = random.sample(incorrect_options, 2)
    print("50-50 Lifeline Activated!")
    print("Remaining Options:")
    for opt in all_options:
        if opt not in removed_options:
            print(opt, "-", options[question_index].split(opt)[1].strip())

def ask_a_friend(question_index):
    if used_lifelines["Ask a Friend"]:
        print("You have already used the Ask a Friend lifeline.")
        return
    used_lifelines["Ask a Friend"] = True
    print("Ask a Friend Lifeline Activated!")
    print(f"Your friend suggests the answer is: {answers[question_index]} ({answer_text[question_index]})")

def flip_the_question(question_index):
    if used_lifelines["Flip the Question"]:
        print("You have already used the Flip the Question lifeline.")
        return
    used_lifelines["Flip the Question"] = True
    new_question_index = random.choice([i for i in range(len(questions)) if i != question_index])
    print("Flip the Question Lifeline Activated!")
    print(f"New Question: {questions[new_question_index]}")
    print(f"Options: {options[new_question_index]}")
    return new_question_index

p = 0
for i in range(len(questions)):
    print(f"Your {i + 1} Question is on your screen:\n{questions[i]}")
    print(f"Options:\n{options[i]}")
    print("If you want to use any lifeline? (yes/no)")
    ans = input("Choose your option: ").strip().upper()
    if ans == 'yes':
        print("Your lifeline options are:\n 1. 50-50\n 2. Ask a Friend\n 3. Flip the Question")
        choice = int(input("Choose your lifeline: "))
        if choice == 1:
            fifty_fifty(i)
        elif choice == 2:
            ask_a_friend(i)
        elif choice == 3:
            new_index = flip_the_question(i)
            if new_index is not None:
                i = new_index
                continue
        else:
            print("Invalid lifeline choice.")

    
    if ans == answers[i] or ans == 'yes' or ans == 'no':
        print(random.choice(cans))
        p = int(points[i])
        print(f"Your total points are: {p}")
    else:
        print(random.choice(wans))
        print(f"The correct answer was {answers[i]} ({answer_text[i]}).")
        print(f"You lose! Your total score is {p}.")
        break
else:
    print(f"Congratulations! You have completed the game and won {p} points!")