i = 0
while True:
    n0 = int(input())
    if n0 == 0:
        break
    n1 = 3*n0
    if n1 % 2 == 0:
        n2 = n1//2
    else:
        n2 = (n1+1)//2
    n3 = 3*n2
    n4 = n3//9
    i += 1
    if n0 == 2*n4:
        print(f"{i}. even {n4}")
    else:
        print(f"{i}. odd {n4}")
