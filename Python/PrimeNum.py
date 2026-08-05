from utils import input_validator

try:
    num = int(input("Enter a Number: "))

    if num<=1:
        print("Not a Prime Number")
    else:
        for i in range(2,num):
            if (num%i)==0:
                print("Not a Prime Number")
                break
            else:
                print("Prime Number")  
                break

except ValueError:
    print("Invalid value, please enter a Valid Integer Number")

except  Exception:
    print("An unaccepted error occured")