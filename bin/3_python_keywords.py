# import python keywords module
import keyword

# List of python keywords
print("Python Keywords:", keyword.kwlist)
#Python Keywords: 
# ['False', 'None', 'True', 'and', 'as', 
# 'assert', 'async', 'await', 'break', 
# 'class', 'continue', 'def', 'del', 
# 'elif', 'else', 'except', 'finally', 
# 'for', 'from', 'global', 'if', 
# 'import', 'in', 'is', 'lambda', 
# 'nonlocal', 'not', 'or', 'pass', 'raise', 
# 'return', 'try', 'while', 'with', 'yield']

print("#" * 40)

#Dat types of python keywords
print(type(keyword.kwlist)) # <class 'list'>

print("#" * 40)

# No of python keywords
print(len(keyword.kwlist)) # 36
print("#" * 40)


# is_valid_variable function
def is_valid_variable(name):
    # Block comment achieving the same as docstring
    """_summary_

    Args:
        name (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Check if the name is a keyword
    if name in keyword.kwlist:
        return False
    # Check if the name is a valid identifier
    if not name.isidentifier():
        return False
    return True

# Test Cases
test_names = ["my_var", "for", "2nd_var", "valid_name", "class", "var-name"]

for name in test_names:
    if is_valid_variable(name):
        print(f"'{name}' is a valid variable name.")
    else:
        print(f"'{name}' is NOT a valid variable name.")
        
#'my_var' is a valid variable name.
#'for' is NOT a valid variable name.
#'2nd_var' is NOT a valid variable name.
#'valid_name' is a valid variable name.
#'class' is NOT a valid variable name.
#'var-name' is NOT a valid variable name.

# indentation in python

def example_function():
    print("This is an example function.")
    if True:
        print("This line is indented inside the if block.")
    print("This line is still inside the function but outside the if block." \
    "......................................................................" \
    "............")