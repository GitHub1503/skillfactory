def rec_mult_num(x):
    if x == 0:
        return 0
    else:
        return (x % 10) + rec_mult_num(x//10)


print(rec_mult_num(764543218))