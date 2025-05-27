#create a game tha asks questions and gives multiple choices and allows the user to answer and play again

def quiz():
    score = 0  # Initialize score
    print("Welcome to the Quiz Game!\n")

    print("Question 1: What is the capital of France?")
    print("A) Berlin")
    print("B) Madrid")
    print("C) Paris")

    answer1 = input("Your answer: ").upper()
    if answer1 == "C":
        print("Correct!\n")
        score += 1
    else:
        print("incorect. The correct answer is C) Paris.\n")

    # Question 2
    print("Question 2: What is the largest planet in our solar system?")
    print("A) Earth")
    print("B) Jupiter")
    print("C) Saturn")
    answer2 = input("Your answer: ").upper()
    if answer2 == "B":
        print("correct!\n")
        score += 1
    else:
        print("incorect. The correct answer is B) Jupiter.\n")
    return score
while True:
    score = quiz()
    again = input("do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print(f"your final score is {score}")
        break