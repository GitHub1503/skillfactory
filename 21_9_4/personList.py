from classPersAcc import PersAcc

pers_1 = PersAcc("Иван", "Иванов", "Санкт-Петербург", 450)
pers_2 = PersAcc("Антон", "Петров", "Санкт-Петербург", 350)
pers_3 = PersAcc("Игорь", "Агапов", "Москва", 750)
pers_4 = PersAcc("Егор", "Сидоров", "Саратов", 330)
pers_5 = PersAcc("Кирилл", "Новиков", "Смоленск", 980)
persons = [pers_1, pers_2, pers_3, pers_4, pers_5]
for person in persons:
    print(person.persinfo())
