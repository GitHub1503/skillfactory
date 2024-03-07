class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

piter = User('Piter Petrov', 'piterpetrov@mail.ru')
julia = User('Julia Robertson', 'juliarobertson@mail.ru')

#julia.name = 'Julia Patrikson'

print(piter.name)
print(julia.name)
print(piter.email)
print(julia.email)

