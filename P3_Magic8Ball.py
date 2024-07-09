# import module
import random

# declare variables
name = "William"
question = "Will my favorite sports team win their next game?"
answer = ""
random_number = random.randint(1, 9)
# print(random_number)

# program
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better no tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubful"
else:
  answer = "Error"

# program in action
print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answer)