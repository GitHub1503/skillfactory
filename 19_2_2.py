def multiplicator(*nums):
    mult_ = 1
    for n in nums:
        mult_ *= n

    return mult_


print(multiplicator())  # 0
print(multiplicator(1))  # 1
print(multiplicator(1, 2))  # 3
print(multiplicator(1, 2, 3))  # 6
print(multiplicator(1, 2, 3, 4))  # 6