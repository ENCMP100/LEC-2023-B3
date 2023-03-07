# Scope of a variable determines where that variable 
# is visible (or can be accessed).

# LOCAL VARIABLES
# ===============

# A variable defined inside a function is called a 
# "local variable". It's scope extends from where it is 
# declared to the end of the function.
# A loop varable in a for loop is also visible to the end of
# the function in which it is defined.
def test1():
    total = 0;
    for i in range(11):
        total = total + i ** 2
    
    print("total:", total)
    print("i:", i)
    
# calling the function
test1()

# total and i are not visible outside of teh function.
# Therefore, the following statements produce syntax errors
## print("total:", total)
## print("i:", i)


# GLOBAL VARIABLES
# ================

# Varialbles declared outside of functions are have "global scope".
# They are visible inside the funtions. However, if a function
# needs to modify a global variable and make that modification
# visible to outside of the function, the function should re-declare
# that variable with "global" keyword.

balance = 1000 # a global variable
x = 123 # another global variable
print()
def withdraw(amount):
    global balance # This function intends to update the balance
                   # and make that change effective outside of the
                   # function.
    if balance >= amount:
        balance = balance - amount
    
    # You can see the global variable x here.
    y = x + 1
    print("y:", y)
    
    # But you cannot modify the global variable x below since
    # it is not declared as global inside the function
    ## x = x + 1
    ## print("x:", x)

print("Initial balance:", balance)
withdraw(100)
print("new balance after withdrawing 100:", balance)
    
    
                 

