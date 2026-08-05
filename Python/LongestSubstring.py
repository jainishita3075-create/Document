string = input("Enter a string: ")
longest = ""
current = ""
for ch in string:
    if ch in current:
        current = current[current.index(ch)+1:]
        # .index is used to return index of 1st element with specified value
    current += ch

    if len(current)>len(longest):
        longest = current

print(longest)