num = int(input("Кол-во билетов: "))
cost = 0
for i in range (0, num):
    print("Возраст посетителя с билетом", i+1)
    age = int(input(": "))
    if age >= 18 and age < 25:
        cost = cost + 990
    elif age >= 25:
        cost = cost + 1390
if num > 3:
    num = num*0.9
print(cost)

