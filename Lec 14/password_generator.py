## 
#  This program creates passwords of a given length.
#  

def main() :
    pw_length = input("Password length: ")
    password = createPassword(pw_length)
    print("Password:", password)
   
## Returns a random password of the given length.
#  A generated password should contain at least one digit and one
#  special symbol.
#  @param pwLength an integer specifying the password length
#  @return the created password   
#
def createPassword(pwLength) :
    #ALGORITHM
    # 1. Starts with an empty string representing the password.
    # 2. Append pwLength-2 number of randomly selected letters to 
    #    the password.
    # 3. Select a random digit and insert it to a random position
    #    of the password.
    # 4. Select a random special character and insert it to a 
    #    random position of the password
    
    # DEFINE CHARACTER SOURCES
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    special_chars = '+-*/?!@#$%&'
    
    
    
    return "password"    

    
# Start the program.
main()   

