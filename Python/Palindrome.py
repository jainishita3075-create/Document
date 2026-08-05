from utils import input_validator

try:
    num = input("Enter a String: ")
    num=num.replace(" ","").lower()

    if (num == (num[::-1])):
        print("Is a Palindrome")
    else:
        print("Is Not a Palindrome")

# except ValueError:
#     print("Invalid Data Type, please enter a string")

except  Exception as e:
    print("An unaccepted error occured:" , e)