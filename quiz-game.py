print("Welcome to the quiz game!")

playing = input("Do you want to play a quiz game? (yes/no): ")
if playing.lower() != "yes":   
    quit()
print("ok! let's play 😊:")
score =0
answers = input("What is the capital of France? ")
if answers.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answers = input("What is 5 + 7? ")
if answers == "12":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answers = input("What is the largest ocean on Earth? ")
if answers.lower() == "pacific":
    print("Correct!")
    score += 1  
else:
    print("Incorrect!")
    
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 3) * 100) + "%.")




