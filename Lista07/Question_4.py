def aprovado(nota1, nota2):
  avarage = (nota1 + nota2) / 2
  status = ''
  if avarage >= 60:
    return 'Aprovado'
  else:
    return 'Reprovado'
    
nota1 = int(input())
nota2 = int(input())

print (f'{aprovado(nota1, nota2)}')
