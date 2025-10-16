def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
    
    
inval = input("Enter the value: ")

try:
    inval = is_integer(inval)  # Convert input to integer
    if inval < 0:
        print("Negative value")
    elif inval == 0:
        print("Zero value")
    else:
        print("Positive value")
except ValueError:
    print("Invalid input. Please enter an integer.")
except TypeError:
    print("Type error occurred.")