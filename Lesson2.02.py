# Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004.
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек. 
# Какова вероятность,что ни одна из них не перегорит в первый день? 
# Какова вероятность, что перегорят ровно две?

# Поскольку в задаче вероятность наступления события мала, 
#а количество испытаний велико, для решения задачи воспользуемся формулой Пуассона

from math import factorial, exp
def poisson(m,p,n):
    lamb=p*n
    return exp(-lamb)*(lamb**m)/factorial(m)

print(f'P = {poisson(0,0.0004,5000): .4f}')

# Вероятность того, что ни одна из ламп не перегорит в первый день 13.53%

print(f'P = {poisson(2,0.0004,5000): .4f}')

# Вероятность того, что 2 лампы перегорят в первый день 27.07%