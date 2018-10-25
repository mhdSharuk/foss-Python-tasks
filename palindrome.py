li = []

num = 12

print('Enter 12 strings')

for i in range(num):

    data = input()

    li.append(data)

first = li[0:2]

scnd = li[3:5]

third = li[6:8]

concat = first+scnd+third

revconcat = reversed(concat)

print("Concated word: \t", concat)

print("Reversed concat:\t", revconcat)

if concat == revconcat:

    print("its a palindrome")

else:

    print("its not a palindrome")
