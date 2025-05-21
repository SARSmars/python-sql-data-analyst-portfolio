# Example to understand local variable and scope of a variable

def my_function():
    local_variable = 10  # This is a local variable
    print("Inside the function, local_variable =", local_variable)

# Calling the function
my_function()

# Trying to access the local variable outside the function
try:
    print("Outside the function, local_variable =", local_variable)
except NameError as e:
    print("Error:", e)