# Write a magic8.py Python program that can answer any “Yes” or “No” question with a different fortune each time it executes.
import random

name = "Joe"

question = "Will y Be Rich ?"

answer = ""

random_number = random.randint(1, 10)

#print(random_number)

if random_number == 1 :
  answer = "Yes - Definitely"
elif random_number == 2 :
  answer = "It is decidedly so"
elif random_number == 3 :
  answer = "Without a doubt"
elif random_number == 4 : 
  answer = "Reply hazy, try again"
elif random_number == 5 : 
  answer = "Ask again later"
elif random_number == 6 : 
  answer = "Better not tell you now"
elif random_number == 7 : 
  answer = "My sources say no"
elif random_number == 8 : 
  answer = "Outlook not so good"
elif random_number == 9 : 
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Signs point to yes"
else :
   answer = "Error"

if len(name) == 0 :
  print("Question: " + question)
else : 
  print(name + " asks: " + question)

if len(question) == 0 :
   print("The Magic 8-Ball cannot provide a fortune unless you ask it something.")
else :
  print( "Magic 8-Ball's answer: " + answer)



