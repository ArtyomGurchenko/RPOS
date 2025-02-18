number = int(input(""))
if 0 < number < 10:
    for n in range (1, number + 1):
        print(''.join(str(j) for j in range(1, n + 1)) + ''.join(str(j) for j in range(n - 1, 0, -1)))
else:
    print("Wrong number")