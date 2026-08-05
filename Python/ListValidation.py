from utils import input_validator

try:
    n = list(map(int,input("Enter a number: ").split()))

    if (len(n)==0):
        print("Empty list")
    else:
        print("Maximum:", max(n))
        
except ValueError:
    print("Invalid Data Type, enter a valid integer value")

except  Exception:
    print("An unaccepted error occured")