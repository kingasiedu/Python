def letter_grade(score):

    if int(score) >= 90:
        letter = "A"
    else: # grade msut be B, C, D, or F
        if int(score) >= 80:
            letter = "B"
        elif int(score) >= 70:
            letter = "C"
        elif int(score) >= 60:
            letter = "D"
        elif int(score) < 60:
            letter = "F"

    return letter

with open("C://Users//Debra Asante//OneDrive - VCCS Student Advantage//Python//scores.txt") as inputFile:
    score_list = inputFile.readline()
for score in score_list:
    score = int(input("Enter score:"))
    print("score: %d" % int(score) and letter_grade(score))







