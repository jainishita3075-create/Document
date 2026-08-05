str = input("Enter a String: ")
print(str[::-1])


str = input("Enter a String: ")
st = ""
for i in range(len(str)-1,-1,-1):
    st += str[i]
print(st)

str = input("Enter a String: ")
i = 0
j = len(str)-1
temp = ""
while(i<len(str)):
    j = len(str)-1-i
    temp += str[j]
    i+=1

print(temp)

