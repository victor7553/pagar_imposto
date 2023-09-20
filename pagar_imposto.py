# Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que R$ 1.200,00.

salario = int(input('digite o seu salario: '))

if salario > 1200:
  print(f'Seu salário é {salario} você deve pagar imposto')
else:
  print('está livre de imposto')

