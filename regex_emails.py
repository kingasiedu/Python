import re 
pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|gov)"
user_input = input("Enter an email: ")
if (re.search(pattern, user_input)):
    print("valid email")
else:
    print("invalid email") 