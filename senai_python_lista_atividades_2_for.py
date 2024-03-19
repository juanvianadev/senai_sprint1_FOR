# -*- coding: utf-8 -*-
"""SENAI-Python-Lista-Atividades-2-FOR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KpdvrzDQpvi5xk7NMQazlaAl55F5GyDb

## 1. Faça um programa que leia 5 números e informe o maior número.
"""

maior_numero = float('-inf')

for i in range(5):
 numero = float(input(f"Digite o {i+1} numero: "))
 if numero > maior_numero:
  maior_numero = numero

print()
print(f"Maior numero digitado e: {maior_numero}")

"""## 2. Faça um programa que verifique e mostre os números entre 1.000 e 2.000 (inclusive) que, quando divididos por 11 produzam resto igual a 2."""

for numero in range(1000, 2001):
 if numero % 11 == 2:
  print(numero)

"""## 3. Faça um programa que leia 5 números e informe a soma e a média dos números."""

soma = 0

for numero in range(5):
  numero = float(input("insira um valor: "))
  soma += numero

print(f"A soma dos valores fica em {soma} e a media fica {soma/5}")

"""## 4. Faça um programa que receba um número e usando laços de repetição calcule e mostre a tabuada desse número."""

numero = int(input("Digite um numero que vc nao sabe a tabuada: "))
print(f"Tabuada de {numero}")

for contador in range(1, 11):
  print(f"{numero} x {contador} = {numero * contador}")

"""## 5. Faça um programa que mostre as tabuadas dos números de 1 a 10 usando laços de repetição."""

for i in range(1, 11):
    print(f"Tabuada do {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()

"""## 6. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro."""

for i in range(1, 21):
  print(i)
print(list(range(1,21)))

"""## 7. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

"""

for numero in range(1,51):
 if numero % 2 == 1:
  print(numero)

"""## 8. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

"""

n1 = int(input("insira um valor: "))
n2 = int(input("insira outro valor: "))

for i in range(n1 + 1, n2):
  print({i})

"""## 9. Uma loja deseja cadastrar 5 clientes e verificar se o faturamento da loja foi superior a loja B (faturamento = 54000). Se o faturamento atingir esse valor mostre na tela uma mensagem contendo em quanto foi superado o faturamento."""

faturamentoLojaB = 54000
soma = 0

for faturamentoLojaA in range(5):
  faturamentoLojaA = float(input("insira um valor: "))
  soma += faturamentoLojaA

if faturamentoLojaA > faturamentoLojaB:
   print(f"O faturamento da loja A e {soma}, foi maior que o da loja B")
elif faturamentoLojaB > faturamentoLojaA:
  print(f"O faturamento da loja A e {soma}, nao foi maior que o da loja B")
else:
   print(f"O faturamento da loja A e {soma}, foi igual que o da loja B")

"""## 10. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares."""

contadorPar = 0
contadorImpar = 0

for numero in range(1, 11):
 numero = int(input("insira um valor: "))

 if numero % 2 == 0:
  contadorPar += 1
 else:
  contadorImpar += 1

print('')
print(f"Sao {contadorPar} pares")
print(f"Sao {contadorImpar} impares")

"""## 11. Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que: Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00; Em 1996 recebeu aumento de 1,5% sobre seu salário inicial; A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário."""

salario = float(input("Digite o salario inicial do funcionario: "))
percentual = 0.015

for i in range(1996, 2024 + 1):
  percentual *= 2
  aumento = salario * percentual
  salario += aumento
  print(f"Salario em {i} = {salario: .2f}")

"""## 12. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

"""

for i in range(999):
  nota = int(input("Digite a nota: "))
  if nota >= 0 and nota <= 10:
    break
else:
  print("Valor e invalido")

"""## 13. Uma loja tem tem uma política de descontos de acordo com o valor da compra do cliente. Os descontos começam acima dos R$500. A cada 100 reais acima dos RS500,00 o cliente ganha 1% de desconto cumulativo até 25%.

- Por exemplo: R$500 = 1% || R$600,00 = 2% … etc…
Faça um programa que exiba essa tabela de descontos no seguinte formato:
Valordacompra – porcentagem de desconto – valor final

"""

valor = float(input("Digite um valor do produto: "))

if valor >= 600:

"""## 14. Faça um programa que receba a idade de 15 pessoas e que calcule e mostre:

a) A quantidade de pessoas em cada faixa etária;

b) A percentagem de pessoas na primeira e na última faixa etária, com relação
ao total de pessoas:

- Até 15 anos
- De 16 a 30 anos
- De 31 a 45 anos
- De 46 a 60 anos
- Acima de 61 anos
"""

ate15 = 0
de16a30 = 0
de31a45 = 0
de46a60 = 0
ate61 = 0

for pessoa in range(15)
  idade = int(input(f"Digite a idade da {pessoa+1}: "))
  if idade <= 15:
    ate15 += 1
  elif 16 <= idade <= 30
    de16a30 += 1
  elif 31 <= idade <= 45
    de31a45 += 1
  elif 46 <= idade <= 60
    de46a60 += 1
  else:
    ate61 += 1

print(f"\nQuantidade de pessoas por faixa etária\nAté 15 anos: {ate15} pessoas\nDe 16 a 30 anos: {de16a30} pessoas\nDe 31 a 45 anos: {de31a45} pessoas\nDe 46 a 60 anos: {de46a60} pessoas\nAcima de 60 anos: {mais60} pessoas\n{((100 * ate15) / 15):.2f}% das pessoas tem até 15 anos\n{((100 * mais60) / 15):.2f}% das pessoas tem mais de 60")

"""## 15. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem."""

base = int(input("insira a base: "))
expoente = int(input("insira o expoente: "))
resultado = 1

for i in range(expoente):
  if base == 1:
    resultado == base
  else:
    resultado *= base

print(f"Resultado: {resultado}")

"""## 16. Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados."""

n = int(input("Digite um numero: "))

for numeroTestado in range(2, n + 1):
  for numeroDivisor in range(1,numeroTestado):
    print(f"{numeroTestado} / {numeroDivisor} = {numeroTestado/(numeroDivisor/+1)} com o resto {numeroTestado%(numeroDivisor + 1)}")
    if numeroTestado % (numeroDivisor+1) == 0:
      if 1 != numeroDivisor+1 != numeroTestado:
        print("Nao e primo")
        break
      elif numeroDivisor + 1 == numeroTestado:
        print("Numero primo")