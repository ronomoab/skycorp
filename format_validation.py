import re 

while True:
    username = input("Enter username: ")
    pattern = r"^[a-zA-Z]+_[0-9]+$"
    if re.match(pattern, username):
        while True:
            password = input("Enter password: ")
            pattern2 = r"^[a-zA-Z0-9_@.+-]+$"      
            if re.match(pattern2, password) and len(password)>= 8:
                print("Sign up successful")
            break
        else:
            print("Invalid password")
        break
    else:
        print("Invalid username")


