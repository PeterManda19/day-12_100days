print("100 Days of Code QUIZ")
print()
print("How many can you answer correctly?")
print()

while True:
  ans1 = input("What language are we writing in? ")
  print()
  if ans1.lower() == "python":
    print("Correct")
    print()
    break
  elif ans1.isnumeric() == True:
    print("I am expecting a name not numbers.")
    print()
    continue
  else:
    print("Nope🙈")
    print()
    continue

while True:
  ans2 = input("Which lesson number is this? ")
  print()
  if(ans2.isnumeric()==True and int(ans2) > 12):
    print("We're not quite that far yet")
    print()
    continue
  elif ans2.isalpha() == True:
    print("I am expecting a number not words and special characters.")
    print()
    continue
  elif(ans2.isnumeric() == True and int(ans2) == 12):
    print("That's right!")
    print()
    break
  elif(ans2.isnumeric() == True and int(ans2) < 12):
    print("We've gone well past that!")
    print()
    continue
  else:
    print("I am expecting a number not words and special characters.")
    continue


while True:
  input()
  print("The quiz has ended. Thank you for participating.")
  print("To start over click on stop on top right of the console and run again.")