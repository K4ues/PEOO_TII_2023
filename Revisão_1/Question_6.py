nmr1 = int(input())
nmr2 = int(input())
nmr3 = int(input())
if nmr1 > nmr2 and nmr1 > nmr3:
  a = nmr1
elif nmr2 > nmr1 and nmr2 > nmr3:
  a = nmr2
else:
  a = nmr3
if nmr1 < nmr2 and nmr1 < nmr3:
  b = nmr1
elif nmr2 < nmr1 and nmr2 < nmr3:
  b = nmr2
else:
  b = nmr3
equation = a + b
print(f'A soma do maior com o menor número é {equation}')
