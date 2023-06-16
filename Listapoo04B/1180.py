N = int(input())
values = list(map(int, input().split()))
#list vai trasnformar em uma lista
#map coloca as variavéis como inteiro por causa do int
menor = min(values)
posicao = values.index(min(values))
#index 
print(f'Menor valor: {menor}')
print(f'Posicao: {posicao}')
