num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
a = num1
if num1 == num2 == num3 == num4:
  print('Try again with different numbers')
if num2 > a:
  a = num2
if num3 > a:
  a = num3
if num4 > a:
  a = num4
print(f'Maior valor = {a}')
b = num1
if num2 < b:
  b = num2
if num3 < b:
  b = num3
if num4 < b:
  b = num4
print(f'Menor valor = {b}')
if a or b == num1 or num2:
  equation = num3 + num4
if a or b == num1 or num3:
  equation = num2 + num4
if a or b == num1 or num4:
  equation = num2 + num3
if a or b == num2 or num3:
  equation = num1 + num4
if a or b == num2 or num4:
  equation = num1 + num3
if a or b == num3 or num4:
  equation = num1 + num2
print(f'A soma do segundo maior com o segundo menor = {equation}')
