# Задача №10
# Решение 1
n = int(input('Введите количество монет: '))
coins = []
eagle = 0

for i in range(n):
    coin = int(input('Положите монетку 0 - решка, 1 - орел: ')) 
    if coin > 1:
        print('Положите монетку заново!')
        coin = int(input('Положите монетку 0 - решка, 1 - орел: ')) 
    coins.append(coin)

for i in coins:
    if i != 0:
        eagle +=1
        
# Решение 2
# for i in range(n):
#     coin = int(input('Положите монетку 0 - решка, 1 - орел: ')) 
#     if coin > 1:
#         print('Положите монетку заново!')
#         coin = int(input('Положите монетку 0 - решка, 1 - орел: ')) 
#     if coin == 1:
#          eagle +=1
                
print(f'Количество монет которые нужно перевернуть: {eagle}')

# Задача №12
x = int(input("Введите целое положительное число - сумму чисел:"))
y = int(input("Введите целое положительное число - произведение чисел:"))
z = True 
if x > 1000 or y > 1000 or x > y:
    print('Введите числа повторно x или y не могут быть больше 1000 и x < y')
    x = int(input("Введите целое положительное число:"))
    y = int(input("Введите целое положительное число:"))
for i in range(y):
    if (x * i - (i**2)) == y:
        print(f' Первое число: {i} \n Второе число: {x - i}')
        z = False
        break
if z:
    print('решения нет')

# Задача №14
N = int(input('Введите степень числа 2: '))
k = 1
count = 0
while count < N + 1:
    print (k)  
    k *= 2
    count += 1
    
