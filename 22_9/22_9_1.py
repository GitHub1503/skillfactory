try:
    array = list(map(int, input("Введите числа через пробел: ").split()))
    element = int(input("Введите любое число из предыдущего диапазона: "))
except ValueError:
    print('Необходимо вводить только числа!')
else:
    def sorting_elements(array):
        for i in range(len(array)):
            for j in range(len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array


    def searching_elements(array, element, left, right):
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] >= element and array[middle - 1] < element:
            return middle - 1
        elif element < array[middle]:
            return searching_elements(array, element, left, middle - 1)
        else:
            return searching_elements(array, element, middle + 1, right)


    print(f'Список отсортированный по возрастанию {sorting_elements(array)}')
    left = array[0]
    right = array[-1]
    if element < left or element > right:
        print('Введеное число выходит за пределы диапазона')
    else:
        print(f'Индекс ближайшего меньшего элемента {searching_elements(array, element, 0, len(array) - 1)} содержит значение {array[searching_elements(array, element, 0, len(array) - 1)]}')
        print(f'Значение большего элемента равно {array[searching_elements(array, element, 0, len(array) - 1)+1]}')