def dividers(n):
    counter = 0
    for i in range(n):
        if n % (i+1) == 0:
            counter += 1
    return counter

print(dividers(int(input())))