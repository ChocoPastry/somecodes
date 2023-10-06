lst1 = []
while True:
    A = input("Enter a word or a number to be added in the first array: ")
    B = input("Do you wanna continue adding?(Y/N) ") 
    C = B.upper()
    D = lst1.append(A)
    if C == 'Y':
        continue
    else:
        break
print(lst1)
lst2 = []
while True:
    A1 = input("Enter a word or a number to be added in the second array: ")
    B1 = input("Do you wanna continue adding?(Y/N) ") 
    C1 = B1.upper()
    D1 = lst2.append(A1)
    if C1 == 'Y':
        continue
    else:
        break
print(lst2)
E = lst1.sort()
F = lst2.sort()
if E == F:
    print("Yes, they are equal")
else:
    print("No, they are not equal")

