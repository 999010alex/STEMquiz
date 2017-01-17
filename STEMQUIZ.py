# STEMquiz
print("This is a quiz that tests your knowledge of science and math.")
name = input("Enter your name: ")

print("Hello " + name + " are you ready to take this quiz?")

print("I will ask 10 questions and three choices for each question.")
print("Select the right answer by pressing A, B or C.")

print("______________________________________________________________")

#set the quiz score to 0.
score = 0
score = int(score) #convert the 0 into a number

print("Question 1")
print("How far is earth from the sun?")
print("A. 90,000,000 miles")
print("B. 9 miles")
print("C. 10,000,000,000,000 miles")
Q1answer = 'a'
Q1response = input('your answer: ')
if Q1response =="A" or Q1response =="a":
    print("Well done " + name + " your response is correct!")
    score = score +1

else:
    print("THAT IS INCORRECT YOU FOOL!")

print("Your current score is " + str(score) + " out of 10.")

print("__________________________________")
print("Question 2")
print("Which Galaxy do we live in?")
print("A. Andromeda Galaxy")
print("B. Milky Way")
print("C. What's a galaxy?")
Q1answer = 'b'
Q1response = input('your answer: ')
if Q1response =="B" or Q1response =="b":
    print("Well done " + name + " your response is correct!")
    score = score +1

else:
    print("u stupid")

print("Your current score is " + str(score) + " out of 10.")


print("__________________________________")
print("Question 3")
print("If x = 3 and y = 6 then whats x * y?")
print("A. 14")
print("B. 10")
print("C. 18")
Q1answer = 'C'
Q1response = input('your answer: ')
if Q1response =="C" or Q1response =="c":
    print("Well done " + name + " your response is correct!")
    score = score +1

else:
    print("Come on man this isin't even that hard...")

print("Your current score is " + str(score) + " out of 10.")


print("__________________________________")
print("Question 4")
print("Whats the area of a rectangle if the length is 3 and width is 2?")
print("A. 3")
print("B. 6")
print("C. 9")
Q1answer = 'b'
Q1response = input('your answer: ')
if Q1response =="B" or Q1response =="b":
    print("Well done " + name + " your response is correct!")
    score = score +1

else:
    print("wrong...")

print("Your current score is " + str(score) + " out of 10.")


print("__________________________________")
print("Question 5")
print("If z is 3 and y is 4 then what is y/z?")
print("A. 1.25")
print("B. 0.75")
print("C. y/z")
Q1answer = 'A'
Q1response = input('your answer: ')
if Q1response =="A" or Q1response =="a":
    print("Well done " + name + " your response is correct!")
    score = score +1

else:
    print("This was not that difficult, and yet you somehow failed, good job.")

print("Your current score is " + str(score) + " out of 10.")
print("__________________________________")
print("Question 6")
print("Which nation first got a satalite in orbit?")
print("A. Soviet Union")
print("B. USA")
print("C. Canada")
Q1answer = 'A'
Q1response = input('your answer: ')
if Q1response =="A" or Q1response =="a":
    print("Well done " + name + " your response is correct!")
    score = score +1

else:
    print("Think of the Sputnik, INCORRECT.")
print("Your current score is " + str(score) + " out of 10.")

print("__________________________________")
print("Question 7")
print("What is the formula for volume of a box rectangle?")
print("A. l * w * h")
print("B. lw")
print("C. bh")
Q1answer = 'A'
Q1response = input('your answer: ')
if Q1response =="A" or Q1response =="a":
    print("Well done " + name + " your response is correct!")
    score = score +1

else:
    print("Incorrect")

print("Your current score is " + str(score) + " out of 10.")

print("__________________________________")
print("Question 8")
print("How do you derive 3x^3 + 4x^2 + 5x + 6?")
print("A. 3x^2 +4x + 5")
print("B. 9x^2 + 8x +5")
print("C. 6")
Q1answer = 'b'
Q1response = input('your answer: ')
if Q1response =="B" or Q1response =="b":
    print("Well done " + name + " your response is correct!")
    score = score +1

else:
    print("This was not that difficult, and yet you somehow failed, good job.")
print("Your current score is " + str(score) + " out of 10.")


print("__________________________________")
print("Question 9")
print("How many planets are there in our solar system? (not including dwarf planets)")
print("A. 9")
print("B. 8")
print("C. Unknown")
Q1answer = 'c'
Q1response = input('your answer: ')
if Q1response =="C" or Q1response =="c":
    print("Well done " + name + " your response is correct!")
    score = score +1

else:
    print("While there are 8 known planets, astronomers beleive in the possibility that there could be another planet beyond the Kuiper Belt.")

print("Your current score is " + str(score) + " out of 10.")


print("__________________________________")
print("Question 10")
print("Which scientist came with the theroy of relativity?")
print("A. Einstein")
print("B. Newton")
print("C. Mr. I")
Q1answer = 'a'
Q1response = input('your answer: ')
if Q1response =="A" or Q1response =="a":
    print("Well done " + name + " your response is correct!")
    score = score +1

else:
    print("Boolean Joolean")

print("Congrats! You finished the quiz, your final score is " + str(score) + " out of 10.")

