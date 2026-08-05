from utils import input_validator

try:
    num = int(input("Enter number: "))

    if num<0:
        print("Negative Number, please enter a valid positive Number")
    else:
        fact = 1
        for i in range(1,num+1):
            fact *= i

    print(fact)

except OverflowError:
    print("Number too large") 

except ValueError:
    print("Invalid Data type, please enter a valid integer value")

except  Exception:
    print("An unaccepted error occured")