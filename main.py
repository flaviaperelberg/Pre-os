# Um vendedor necessita de um algoritmo que calcule o preço total devido por um cliente. O algoritmo deve receber o código de um produto, a quantidade comprada e calcular o preço total, usando a tabela abaixo: Código do Produto 1001, Preço Unitário 5,32, Código do Produto 1324, Preço Unitário 6,45, Código do Produto 6548, Preço Unitário 2,37, Código do Produto 987, Preço Unitário 5,32, Código do Produto 7623, Preço Unitário 6,45.

print('''Referência - Código dos produtos: 1001, 1324, 6548, 987, 7623

''')

codigo = int(input('Para saber o preço total devido por um cliente, digite o código do produto: \n' ))

quantidade = int(input('Digite a quantidade: \n'))

if int(codigo == 1001):
  print('O valor é de:', +5.32 * quantidade)
elif int(codigo == 1324):
  print('O valor é de:', +6.45 * quantidade)
elif int(codigo == 6548):
  print('O valor é de:', +2.37 * quantidade)
elif int(codigo == 987):
  print('O valor é de:', +5.32 * quantidade)
elif int(codigo == 7623):
  print('O valor é de:', +6.45 * quantidade)
else:
  print('Código não cadastrado')