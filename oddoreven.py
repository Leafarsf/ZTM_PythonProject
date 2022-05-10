def is_odd_or_even(num):
    return num % 2 == 0

n = int(input("Insira um número inteiro para descobrir se este é par ou ímpar: "))
if is_odd_or_even(n) == True:
    print(f" O número {n} é par!")
else:
    print(f"O número {n} é ímpar!")