# Global variable
a = 10

#func: local_example
def local_example():
    #local variable
    b=20
    print("Inside local_example:")
    print("Global variable a:", a) #accessing global variable
    print("Local variable b:", b) # Accessing local variable
    


# func: another_function
def another_function():
    print("Inside another_function:")
    print("Global variable a:", a) #accessing global variable
    #print("Local variable b:", b) # This will raise an error as b is not defined here
    try:
        print("Local variable b:", b) # This will raise an error as b is not defined here
    except NameError as e:
        print("Error:", e)
        
    
#usage
#By locally local_example
local_example()
print("-" * 40)

#By another_function
another_function()
