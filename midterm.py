# FamousPhrase = "Python Object Wont Ever Reset State"
# words = FamousPhrase.split(" ")
# new_word = ""
# for word in words:
#    new_word += word[0]
# print(new_word)


# lines = []
# try:
#    with open("somefile.txt") as f:
#       lines = f.readline()
# except IOError:
#    print("cannot open file")

# print("text: %d" % len(lines))


# def xxx(text_string, search_string):
#    hits = text_string.upper().count(search_string.upper())
#    return hits


# def xxy(text_string, search_string):
#   hits = xxx(text_string, search_string)
#   print("'%s' has %d matches for '%s'" % (text_string, hits, search_string))


# line = input("Enter a series of letter:")
# user_input = input("Enter a character:")
# xxy(line, user_input)


def xxy():
    x = input("Enter amount:")

    with open("xxy.txt") as f:
        lines = f.readlines()
        for line in lines:
            sum = 0
            nums = line.split(",")
            for num in nums:
                sum += int(num) + int(x)
            ave = sum / len(nums)

            print("%s average: %.2f" % (line, ave))


xxy()

# import string


# def xxx(phrase):
#   returnphrase = "";
#  lower = string.ascii_lowercase
# upper = string.ascii_uppercase
# for char in phrase:
#    if char in lower:
#      returnphrase += lower[(lower.index(char)+13)%26]
#  elif char in upper:
#        returnphrase += upper[(upper.index(char)+13)%26]
# else:
#  returnphrase += char
#
#           return returnphrase


# output = xxx(input("phrase: "))
# print("output %s" % output)
