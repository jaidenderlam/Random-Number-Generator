# random number generator
import random as r

print("-----------------Random Number Generator-----------------")
num = []
for x in range(3):
  ask = input ("Do you want to generate a random number? (yes/no): ")
  ask_capital = ask.lower()
  if ask_capital == "yes":
    num.append(r.randint(1,100))
    print(num)
  else:
    print("Please enter yes or no")
    break


