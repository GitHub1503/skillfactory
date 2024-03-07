def par_checker(string):
    stack = []  # инициализируем стек

    for s in string:  # читаем строку посимвольно
        if s == "(" or s == "{":  # если открывающая скобка,
            stack.append(s)  # добавляем её в стек
        elif s == ")" or s == "}":
            # если встретилась закрывающая скобка, то проверяем
            # пуст ли стек и является ли верхний элемент — открывающей скобкой
            if len(stack) > 0 and (stack[-1] == "(" or stack[-1] == "{"):
                stack.pop()  # удаляем из стека
            else:  # иначе завершаем функцию с False
                return False
    # если стек пустой, то незакрытых скобок не осталось
    # значит, возвращаем True, иначе — False
    return len(stack) == 0


pars = {")": "(", "]": "["}


def par_checker_mod(string):
    stack = []

    for s in string:
        if s in "([":
            stack.append(s)
        elif s in ")]":
            if len(stack) > 0 and stack[-1] == pars[s]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

rest = -1

if par_checker('{((string)(({string_2)))}'):
    print('True')
else:
    print('False')

if par_checker_mod('{((string)(({string_2)))}'):
    print('True')
else:
    print('False')