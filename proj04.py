# Function to encrypt a file


def encryption():
    words, s = input("Give me a string to encode:"), int(input("Give me a rotation:"))

    result = ""
    for i in range(len(words)):
        char = words[i]

        if char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char

    print("The encrypted text is:", result)


# Function to decrypt a file

def decryption():
    text, s = input("Give me a string to decode:"), input("Enter a word from the string:")
    words = 'abcdefghijklpmnopqrstuvwxyz'
    for keys in range(len(words)):
        result = ""
        for symbols in text:
            if symbols in words:
                num = words.find(symbols)
                num = num - keys
                if num < 0:
                    num = num + len(words)
                result = result + words[num]
            else:
                result = result + symbols
        if s in result:
            break
    print("The encryption key is: %s\n Plaintext: %s" % (keys, result))


while True:
    ch = input("\nEnter \n'e' to encrypt:\n'd' to decrypt:\n'q' to quit:\n")
    if ch == 'e':
        encryption()
    elif ch == 'd':
        decryption()
    elif ch == 'q':
        print("Thanks for playing")
        break
    else:
        print("Wrong choice try again:")
