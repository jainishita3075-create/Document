import argparse

# initalizing the parsing, for arguments
# two types of arguments:-
# 1. position
# 2. optional


# positional argument:-
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # creation of object(by adding arguments to parser)
    # first the argument is passed and then the help is passed
    parser.add_argument("number1", help="first number")
    parser.add_argument("number2", help="second number")
    parser.add_argument("operation", help="operation")
    args = parser.parse_args()
    print(args.number1)
    print(args.number2)
    print(args.operation)

    # when ever input passed in command line it comes back as string instead of integer so we need to convert it 
    n1 = int(args.number1)
    n2 = int(args.number2)
    result = None
    if args.operation == "add":
        result = n1+n2
    elif args.operation == "sub":
        result = n1-n2
    elif args.operation == "mul":
        result = n1*n2
    elif args.operation == "div":
        result = n1/n2

    print(result)



# optional arguments:- allows user to leave argument as blank by adding -- sign in front of argumentname
# works in key-value pairs, arguments can be passed in any sequence

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     # creation of object(by adding arguments to parser)
#     # first the argument is passed and then the help is passed
#     parser.add_argument("--number1", help="first number")
#     parser.add_argument("--number2", help="second number")
#     parser.add_argument("--operation", help="operation", \
#                          choices=["add","sub","mul","div"])
#     # choices helps to restrict the user to use only the defined operations 
#     args = parser.parse_args()
#     print(args.number1)
#     print(args.number2)
#     print(args.operation)

#     # when ever input passed in command line it comes back as string instead of integer so we need to convert it 
#     n1 = int(args.number1)
#     n2 = int(args.number2)
#     result = None
#     if args.operation == "add":
#         result = n1+n2
#     elif args.operation == "sub":
#         result = n1-n2
#     elif args.operation == "mul":
#         result = n1*n2
#     elif args.operation == "div":
#         result = n1/n2
#     else:
#         print("Operation not defined")

#     print(result)





""" Automation Script """
# To rename a file

# import os
# files=["photo1.png","photo2.png","photo3.png"]
# for i, f in enumerate(files,start=1):
#     new_name = f"image_{i}.png"
#     print(f"{new_name}")