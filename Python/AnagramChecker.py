Input = list(input("Enter a String: "))
Strng = list(input("Enter another String: "))

if len(Input)!=len(Strng):
    print("Not an Anagram")
else:
    Input.sort()
    Strng.sort()
    if (Input==Strng):
        print("Is a Anagram")
    else:
        print("Not an Anagram")