# Write a program that prompts the user to enter the number of students and each student's name and score
# finally displays the student with the highest score and the student with the second-highest score

list = {}

choice = input("are there anymore entries? (Y/N): ")

while choice.lower() == "y":
    name = input("enter student's name here: ")
    score = int(input("enter student's score here: "))
    list[score] = name
    choice = input("are there anymore entries? (Y/N): ")
    if choice.lower() == "y":
        True
    else:
        break


print(list[max(list.keys())] + " got the highest score, " + str(max(list.keys())) + ". yay!!" )
del list[max(list.keys())]
print(list[max(list.keys())] + " got the second highest score, " + str(max(list.keys())) + ".")
