# This is a simple number guessing game, where the answer is a number from 0-9

def play():
    import random

    instructions = """
    This is a number guessing game. The answer is a number from 0-9. Keep guessing until you get the right one. Good luck!
    """.strip()
    print(instructions)
    a = str(random.randint(0, 9))
    g, rnge, ag = None, list(map(str, list(range(10)))), []
    while g != a:
        g = input("Guess a number between 0 and 9 inclusive: ")
        if g not in rnge:
            print("This is not a valid guess!", end=" ")
            continue
        elif g in ag:
            print("You guessed this already!", end=" ")
            continue
        else:
            ag += [g]
            if g != a:
                print("This guess is incorrect!")
    print("You guessed it! The answer was", str(a) + "!")

# def printInstructions():
#     instructions = """
#     This is a number guessing game. The answer is a number from 0-9. Keep guessing until you get the right one. Good luck!
#     """.strip()
#     print(instructions)

# def generateAnswer():
#     import random

#     return str(random.randint(0, 9))

# def playGame(answer):
#     guess = None
#     validGuesses = list(map(str, list(range(10))))
#     alreadyGuessed = []
#     while guess != answer:
#         guess = input("Guess a number between 0 and 9 inclusive: ")
#         if guess not in validGuesses:
#             print("This is not a valid guess!", end=" ")
#             continue
#         elif guess in alreadyGuessed:
#             print("You guessed this already!", end=" ")
#             continue
#         else:
#             alreadyGuessed.append(guess)
#             if guess != answer:
#                 print("This guess is incorrect!")
#     print(f"You guessed it! The answer was {answer}!")

# def play():
#     printInstructions()
#     answer = generateAnswer()
#     playGame(answer)

play()