number = int(input(""))
if 1 <= number <= 9:
    for n in range(1, number):
        print(str(n) * n)
else:
    print("Wrong number")