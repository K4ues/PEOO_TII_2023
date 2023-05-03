num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

soma = 0

if num1 % 2 == 0:
    soma = +num1
if num2 % 2 == 0:
    soma += num2
if num3 % 2 == 0:
    soma += num3
if num4 % 2 == 0:
    soma += num4
print(f'Soma dos pares = {soma}')

subtract = 0

if num1 % 2 != 0:
    subtract += num1
if num2 % 2 != 0:
    subtract += num2
if num3 % 2 != 0:
    subtract += num3
if num4 % 2 != 0:
    subtract += num4
print(f'Soma dos ímpares = {subtract}')
