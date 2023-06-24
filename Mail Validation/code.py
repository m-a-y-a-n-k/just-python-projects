email = input("Enter your email address : ")

INVALID_EMAIL_MESSAGE = "Email is not valid."

def hasCharacter(email, ch):
    for e in email:
        if e == ch:
            return True
    return False

def hasUpper(email):
    for e in email:
        if e.isalpha() and e == e.upper():
            return True
    return False

def hasSpecialChars(email):
    for e in email:
        if e.isalpha() == False and e.isdigit() == False and e != "_" and e != "@" and e != ".":
            return True        
    return False

if len(email) < 6:
    print(INVALID_EMAIL_MESSAGE)
elif email[0].isalpha() == False:
    print(INVALID_EMAIL_MESSAGE)
elif "@" not in email:
    print(INVALID_EMAIL_MESSAGE)
elif email.count("@") > 1:
    print(INVALID_EMAIL_MESSAGE)
elif ((email[-4] == ".") ^ (email[-3] == ".")) == False:
    print(INVALID_EMAIL_MESSAGE)
elif hasCharacter(email,' '):
    print(INVALID_EMAIL_MESSAGE)
elif hasUpper(email):
    print(INVALID_EMAIL_MESSAGE)
elif hasSpecialChars(email):
    print(INVALID_EMAIL_MESSAGE)
else:
    print("Email is valid")    