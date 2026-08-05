from utils import input_validator

try: 
    value = input("Enter Value: ")

    count = {} #empty dictionary

    for val in value:
        count[val] = count.get(val,0)+1

    print(count)

except ValueError:
    print("Invalid Data Type, enter a valid string")
except  Exception:
    print("An unaccepted error occured")