def validate_password(password):
    
    print("1. Easy    2. Medium    3. Hard")

difficulty = int(input("Choose difficulty level: "))
password = input("Enter password: ")
    
has_lower = False 
has_upper = False 
has_digit = False 
has_symbol = False 
   
symbols = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"


if(difficulty == 1):
    if (len(password) > 5):
        print("Password accepted")
    else:
        print("The password should be at least 6 characters")
    

if(difficulty == 2):
    
        if (len(password) > 7):
        
            if character.islower():
                has_lower = True
        
                if character.isupper():
                    has_upper = True
            
                    if character.isdigit():
                        has_digit = True
                        print("Password accepted.")
                    else:
                        print("The password should be containing at least one digit.")
                else:
                    print("The password should be containing at least one uppercase letter and one digit.")
            else:
                print("The password should be containing at least one lowercase letter.")
        
        else:
            print("The password should be at least 8 characters")


if(difficulty == 3):
    if (len(password) > 7):
        if character.islower():
            has_lower = True
        
            if character.isupper():
                has_upper = True
            
                if character.isdigit():
                    has_digit = True
                 
                    if character in symbols:
                        has_symbol = True
                        print("Password Accepted.")
                    else:
                        print("The password should be containing at least one special character.")
                        
                else:
                    print("The password should be containing at least one digit and one special character.")
            else:
                print("The password should be containing at least one uppercase letter, one digit, and one special character.")
        else:
            print("The password should be containing at least one lowercase letter.") 
        
    else:
        print("The password should be at least 8 characters")   