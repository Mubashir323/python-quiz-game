print("===== Python Quiz Game =====")

name = input("Enter your name: ")
print("Good luck,", name, "!")

score = 0

answer = input("What language are we learning? A) Python  B) Java  C) C++  D) HTML: ")

if answer.lower() == "a":
    print("Correct! ✅")
    score += 1
else:
    print("Wrong! ❌ The correct answer is Python.")

answer = input("What symbol is used to start a comment in Python? A) //  B) #  C) <!--  D) **: ")

if answer.lower() == "b":
    print("Correct! ✅")
    score += 1
else:
    print("Wrong! ❌ The correct answer is #.")

answer = input("Which function is used to display text in Python? A) show()  B) display()  C) print()  D) text(): ")

if answer.lower() == "c":
    print("Correct! ✅")
    score += 1
else:
    print("Wrong! ❌ The correct answer is print().")

print()
print("===== Quiz Finished =====")
print("Your score:", score, "/ 3")