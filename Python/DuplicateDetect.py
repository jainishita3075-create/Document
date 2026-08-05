value = input("Enter Value: ")
count = {} #empty dictionary

for val in value:
    count[val] = count.get(val,0)+1

print(count)

for val in count:
    if count[val]>1:
        print(val)