# -*- coding: utf-8 -*-
"""SENAI-Python-Aula3-FOR-e-WHILE.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ET7ac5Y2Vp29qbtTlpvqGMmzc5J07FH9

## 1. Solicitar um numero inteiro positivo N ao usuario. Imprimir os numeros de N a 1. Realizar o exercicio usando for e while.
"""

T = int(input("Entre com numero inteiro maior que 1: "))

#FOR
print("For: ")
for t in range(T):
  print(f"{T - t}", end = " ")
print("\n")

#WHILE
print("While: ")
i = 0

while i < T:
  print(f"{T - i}", end = " ")
  i += 1

"""## 2. Solicitar um número inteiro positivo N ao usuário. Imprimir os números de N a 1 trocando o sinal dos números. Realizar o exercício usando loops for e while. Exemplo para N igual a 5:"""

#T = int(input("Entre com numero inteiro maior que 1: "))

#FOR
#print("For: ")
#for t in range(T):
#  print(f"{t - T}", end = " ")
#print("\n")

#WHILE
#print("While: ")
#i = 0

#while i < T:
#  print(f"{i - T}", end = " ")
#  i += 1
#=============================================================

N = 5
mult = -1
fat = 1
for n in range(N):
  print(fat * (N - n), end=" ")
  fat *= mult

"""## 3. Solicitar um numero inteiro positivo N ao usuario e imprimir i² para 0 < i < N. Por exemplo, para N = 5, serao impressos."""

#T = int(input("Entre com numero inteiro maior que 1: "))
#FOR
#print("For: ")
#for i in range(1, T):
#  print(f"{i*i}")

#WHILE
#print("While: ")
#i = 1

#while i < T:
#  print(f"{i*i}")
#  i += 1

N = int(input("Entre com numero inteiro maior que 1: "))

for i in range (N):
  print(i , i*i)

"""## 4. Solicitar uma palavra ao usuário e dizer se a palavra é um palíndromo, isto é, pode ser lida igualmente da esquerda para a direita e vice-versa. Exemplos de palavras que são palíndromos: ovo, radar, mirim, arara, reviver. Algumas dicas:"""

palavra = input("Digite uma palavra palíndromo: ").upper().strip()

#FOR
inverte = ''
for c in range(len(palavra)-1, -1, -1):
  inverte += palavra[c]
  print(inverte)

if palavra == inverte:
  print("E uma palindrome")
else:
  print("Nao e uma palindrome")

#WHILE

"""## 5. Fazer um programa que solicita um número inteiro positivo N ao usuário e imprime o seguinte padrão na tela. Por exemplo, para"""

N = int(input("Entre com numero inteiro maior que 1: "))

#FOR
print(" " + "-" * (N))

for teste in range(N):
  print("|" + " " * (N) + "|")

print(" " + "-" * (N))

#WHILE
i = 0
print(" " + "-" * (N))

while i < N:
    print("|" + " " * (N) + "|")
    i += 1

print(" " + "-" * (N))

"""## 6. Fazer um programa que solicita um número inteiro positivo N ao usuário e imprime o seguinte padrão na tela. Por exemplo, para N = 5:"""

N = int(input("Entre com numero inteiro maior que 1: "))

#FOR
for i in range(N + 1):
  print("+" * i)
  i += 1

i2 = 0
print()

#WHILE
while i2 < N:
  i2 += 1
  print("+" * i2)