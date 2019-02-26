# Write a program that prompts the user to enter a score between 0 and 100 inclusive. The grading system is as follows:
# A: 70 - 100
# B: 60 - 69
# C: 55 - 59
# D: 50 - 54
# E: 45 - 49
# S: 35 - 44
# U: 0 - 34

# Sample sessions:

# Enter score: 73
# A

# Enter Score: -1
# Invalid! Score must be within 0 - 100.

x = int(input("enter score here: "))
if (70 <= x <= 100):
          print("A")
elif (60 <= x <= 69):
          print("B")
elif (55 <= x <= 59):
          print("C")
elif (50 <= x <= 54):
          print("D")
elif (45 <= x <= 49):
          print("E")
elif (35 <= x <= 44):
          print("S")
elif (0 <= x <= 34):
          print("U")
else:
        print("invalid! score must be within 0-100 boiii")
