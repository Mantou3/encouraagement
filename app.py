print("Title of program: MCQ revision program")
print()

counter = 0
score = 0
total_num_of_qn = 3

counter +=1
tracker = 0

while tracker !=1:

print("Q"+str(counter)+") "+ "What is the value of x when 6x-13=5")
print(" a) 3")
print(" b) 13")
print(" c) 5")
print(" d) 18")
answer = input("Your answer: ")
answer = answer.lower()
if answer == "a":
output = "Correct.Good job:)"
score +=1
elif answer == "b":
output = "Wrong. 6x does not equal to 13"
score -=1
elif answer == "c":
output = "Wrong, 6x does not equal to 5"
tracker =1
score -=1
elif answer == "d":
output = "Wrong. 6x=18."
score -=1
else:
output = "Please choose a, b, c or d only."

print()
print(output)
print()
print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%" )
print()
print()

counter +=1
tracker = 0

while tracker !=1:

print("Q"+str(counter)+") "+ "The chemical formula O2 represents")
print(" a) one oxygen molecule")
print(" b) two oxygen atoms")
print(" c) one oxygen atom")
print(" d) two oxygen molecules")
answer = input("Your answer: ")
answer = answer.lower()
if answer == "a":
output = "Yes, that's right!"
tracker =1
score +=1
elif answer == "b":
output = "Wrong. If so, then it will be written as O and O - two oxygen atoms."
score -=1
elif answer == "c":
output = "Wrong. Clearly the number 2 in the formula must mean something?"
score -=1

elif answer == "d":
output = "Wrong. What's the difference between a molecule and an atom?"
score -=1
else:
output = "Please choose a, b, c or d only."

print()
print(output)
print()
print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%" )
print()
print()

counter +=1
tracker = 0

while tracker !=1:

print("Q"+str(counter)+") "+ "What is the electrical configuration of potassium")
print(" a) 2,1")
print(" b) 2,8,8,1")
print(" c) 2,8,8,2")
print(" d) 2,8,8")
answer = input("Your answer: ")
answer = answer.lower()
if answer == "a":
output = "Wrong. Think again - how many electron shells are filled, and which group is this in?"
score -=1
elif answer == "b":
output = "Correct!keep trying:)"
score +=1
elif answer == "c":
output = "Wrong. Think again - how many electron shells are filled, and which group is this in?"
score -=1

elif answer == "d":
output = "Wrong. Think again-how many electron shells are filled, and which group is this in? "
tracker =1
score -=1
else:
output = "Please choose a, b, c or d only."

print()
print(output.lower())
print()
print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%" )
print()
print()

print("End of quiz!)
