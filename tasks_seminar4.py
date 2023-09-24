# Task 22
n = int(input("Введите кол-во элементов первого множества: "))
m = int(input("Введите кол-во элементов второго множества: "))

list_1 = [int(input("Введите элемент первого множества: ")) for i in range(n)]
list_2 = [int(input("Введите элемент второго множества: ")) for i in range(m)]

print(sorted(set(list_1).intersection(set(list_2))))

# Task 24
n = int(input("Введите кол-во кустов: "))
list_1 = [int(input("Введите кол-во ягод на кусте: ")) for i in range(n)]

value = 0
max_value = 0

for i in range(len(list_1)):
    if i == 0:
        value = (list_1[len(list_1) - 1] + list_1[i] + list_1[i + 1])
    elif i == len(list_1) - 1:
        value = (list_1[i - 1] + list_1[i] + list_1[0])
    else:
        value = (list_1[i - 1] + list_1[i] + list_1[i + 1])

    if value > max_value:
        max_value = value
    i += 1

print(max_value)