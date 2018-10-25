li = []

num = int(input("enter the number of elements"))

print("enter the numbers")

for i in range(num):

    elem = int(input())

    li.append(elem)

print("Given list: \t ",li)

sorted = sorted(li)

print("sorted list: \t", sorted)
