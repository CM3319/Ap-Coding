import random 

# create a new document called pythonReview.py and answer the following
# questions. 

# Question 1
# Build a program that determines if a student has submitted their class work 
# and homework assignment. The program should use an operator that allows 
# for evaluating 2 conditions and determining if the conditions are true 
# or false.

# hint: find the a operator that allows you to evaluate 2 condtions.

is_classwork_submitted = ("classwork_submitted" == "yes")
is_homework_submitted = ("homework_submitted" == "yes")

# Question 2
# Create a function that will take in a string as an argument and output 
# that string in reverse order.

# hint: look into string reverse in w3schools

fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)








# Question 3
# Create a number guessing function where the program will continuously 
# ask the user to enter a number until the guess the number correctly. 
# Your program should also give the user information on if their guess 
# is close to the correct number. If the guess is above the correct number 
# it should tell the user it is too high and try again. 
# If the guess is below the number, it should tell the user it is too low, 
# it should tell them it is too low and to guess again. Once the user gets 
# it correct the program should congratulate them, stop, and tell them how 
# many attempts they made.


def number_guessing_game():

    secret_number = random.randint(1, 100) 
    attempts = 0
    guess = 0
    
    print('Im thinking of a number 1-100, tri and guess it')

    def Guess():
         if guess < secret_number:
               print("Too low, try again!")
            elif guess > secret_number:
                print("Too high, try again!")
            else:
                print(f"Congratulations! You guessed the number")
                
       
