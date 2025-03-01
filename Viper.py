#Viper

alphabet = "abcdefghijklmnopqrstuvwxyz"
number = "0123456789"
symbol = "~!@#$%^&*()_+-=[]\\{}|;':\",./<>?"

def encrypt(password, key):
    res = ""
    for i in range(len(password)):
        char_type = ""
        pw = password[i]

        j = i
        while j > len(key) -1:
            j -= len(key)
        k = key[j]

        i_pw = 0
        if pw in alphabet:
            i_pw = alphabet.index(pw)
            char_type = alphabet
        elif pw in alphabet.upper():
            i_pw = alphabet.upper().index(pw)
            char_type = alphabet.upper()
        elif pw in number:
            i_pw = number.index(pw)
            char_type = number
        elif pw in symbol:
            i_pw = symbol.index(pw)
            char_type = symbol
        else:
            res += pw
            continue

        i_k = 0
        if k in alphabet:
            i_k = alphabet.index(k)
        elif k in alphabet.upper():
            i_k = alphabet.upper().index(k)
        elif k in number:
            i_k = number.index(k)
        elif k in symbol:
            i_k = symbol.index(k)

        i_res = i_pw + i_k
        while i_res > len(char_type) -1:
            i_res -= len(char_type)
    
        res += char_type[i_res]
    
    return res

def decrypt(password, key):
    res = ""
    for i in range(len(password)):
        char_type = ""
        pw = password[i]

        j = i
        while j > len(key) -1:
            j -= len(key)
        k = key[j]

        i_pw = 0
        if pw in alphabet:
            i_pw = alphabet.index(pw)
            char_type = alphabet
        elif pw in alphabet.upper():
            i_pw = alphabet.upper().index(pw)
            char_type = alphabet.upper()
        elif pw in number:
            i_pw = number.index(pw)
            char_type = number
        elif pw in symbol:
            i_pw = symbol.index(pw)
            char_type = symbol
        else:
            res += pw
            continue

        i_k = 0
        if k in alphabet:
            i_k = alphabet.index(k)
        elif k in alphabet.upper():
            i_k = alphabet.upper().index(k)
        elif k in number:
            i_k = number.index(k)
        elif k in symbol:
            i_k = symbol.index(k)

        i_res = i_pw - i_k
        while i_res < 0:
            i_res += len(char_type)
        res += char_type[i_res]
    
    return res    


print("This is VIPER made by Lolpotch")
print()

while True:
    print('Type "q" to quit')
    option = input("Encrypt or Decrypt? (E/D): ")

    #Quit
    if option == 'q' or option == 'Q':
        break

    #If user didn't choose "e" or "d"
    if option != 'd' and option != 'D' and option != 'E' and option != 'e':
        print("Please answer the option!")
        print()
        continue
    
    print()
    message = input("Message: ")
    key = input("Password: ")
    if len(key) == 0:
        print("Password shouldn't be empty!")
        print()
        continue

    print()
    print("=======================================RESULT=============================================")
    if option == 'e' or option == 'E':
        print(encrypt(message, key))
    elif option == 'd' or option == 'D':
        print(decrypt(message, key))
    print("==========================================================================================")
    print()

print()
input("Thank you for using this service! (Press enter to quit)")