#Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

# # Для решения данной задачи воспользуемся формулой Бернулли

from math import factorial, exp
def ber(n, k, p):
    combinations=factorial(n)/(factorial(k)*factorial(n-k))
    return combinations*(p**k)*(1-p)**(n-k)

print(f'P = {ber(144,70,0.5): .4f}')

# Вероятность того, что при 144-х кратном подбрасывании монетки орёл выпадет ровно 70 раз: 0.0628