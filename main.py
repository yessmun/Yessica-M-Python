print ("Welcome to my first game!")

name = input("What is your name? ")
age = int(input("What is your age? "))

print("hello", name, "your age is", age, "years old :) ")

if age >= 18:
  print ("You are the right age to play!")

  wants_to_play = input("Do you want to play? ")
  if wants_to_play == "yes":
    print("Let's play!")
  
else:
  print ("Sorry you are not old enough to play :( ")





'''
Datatypes Notes: 
str - "hello" "hi" "89"
int - 8, 7, 9
float - 6.0, 2.0 
bool - True, false
'''