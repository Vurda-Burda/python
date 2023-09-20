# Задача 22
n = int(input('Введите число n: '))
m = int(input('Введите число m: '))

def my_func_create_list(list_len_number):
    lst = []
    for i in range(list_len_number):
        n = int(input(f'Введите множество состоящие из {list_len_number} элементов: '))
        lst.append(n)
    print("Множество введено.")
    return lst

n_list = my_func_create_list(n)
m_list = my_func_create_list(m)

res = []
for m in m_list:
    for n in n_list:
        if n == m and (n not in res or m not in res):
            res.append(m)
            
res.sort()
print(' '.join(map(str, list(res))))

# Задача 24
k_quantity = int(input('Введите число кустов: '))
b_quantity = my_func_create_list(k_quantity) #использовал функцию из задачи выше

def berries_collect(number_of_bushes):
    res = []
    for i in range(len(number_of_bushes)):
        if i - 1 < 0:
            res.append(number_of_bushes[len(number_of_bushes) - 1] + number_of_bushes[i] + number_of_bushes[i + 1])
        elif i + 1 == len(number_of_bushes):
            res.append(number_of_bushes[i - 1] + number_of_bushes[i] + number_of_bushes[len(number_of_bushes) - (i + 1)])
        else:
            res.append(number_of_bushes[i - 1] + number_of_bushes[i] + number_of_bushes[i +1])
    return max(res)

print(berries_collect(b_quantity))