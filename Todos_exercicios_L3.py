#1 - fds a 1 
import random
n = random.randint(0,10)
r = int(input("Estou pensando em um numero entre 0 e 10, tente adivinhar-lo! "))
while r !=n:
  if r > n:
    print("seu numero é maior do qual estou pensando")
  else:
    print("seu numero é menor do qual estou pensando")
  r = int(input("Tente novamente! "))
print("Parabens! eu estava pensando no número",r)

#2-blz valeu
%reset -f
n = int(input('ei, me diz um número de 0 a 10 ai rapidão namoralzinha na humilds'))
while n < 0 or n > 10:
  n = int(input('EU DISSE DE ZERO A DEZ HUMANO IMBECIL (/)= _ =(/).'))
print('blz, valeu.')

#3- Ultrapassagem de População
%reset -f
anos = 0
PA = 80000
PB = 200000
print('População A:',PA,'habitantes.')
print('População B:',PB,'habitantes.')
print('Taxa de aumento de população país A: 3% ao ano')
print('Taxa de aumento de população país B: 1,5% ao ano')
while PA < PB:
  PA = PA+PA*0.03
  PB = PB+PB*0.015
  anos = anos + 1
PA = int(PA)
PB = int(PB)
print('Numa estimativa de',anos,'anos, A ultrapassará B')
print('População A:',PA,'habitantes.')
print('População B:',PB,'habitantes.')

#5-Maior numero da sequencia
%reset -f
n1 = 0
i = 1
while i <= 10:
  print('Diga-me seu',i,'º número')
  n2 = int(input())
  if n2 > n1:
    n1 = n2
  i = i + 1
print('O maior número que voçe me disse foi',n1)

#7-Impares
%reset -f
n = int(input('quantos imapares queres ver (em sequencia)'))
i = 1
while i <= n:
  print(2*i-1)
  i = i + 1

#8-Hamburger de números
%reset -f
n1 = int(input('me diz um numero'))
n2 = int(input('me diz outro numero'))
if n1 > n2:
  n2 = n2 + 1
  while n1 > n2:  
    print(n2) 
    n2 = n2 + 1  
else:
  n1 = n1 + 1
  while n2 > n1: 
    print(n1)
    n1 = n1 + 1

#10-É a potência >W< UwU 
%reset -f
n1 = float(input('Diga-me a base da potência.'))
n2 = int(input('Diga-me a potência.          '))
i = 1
n3 = 1
while i <= n2:
  n3 = n3 * n1
  i = i + 1
print(n3)

#11-par impar
%reset -f
n1 = 0
i = 1
pares = 0
impares = 0
while i <= 10:
  print('Diga-me seu',i,'º número')
  n2 = int(input())
  if n2 % 2 == 0:
    pares = pares + 1
  else:
    impares = impares + 1
  i = i + 1
print('quantidade de pares digitados:   ',pares)
print('quantidade de impares digitados: ',impares)

#12-FIB
%reset -f
n = int(input("Quantos termos queres da sequencia Fib?"))
x = 0
y = 1
i = 0
while i < n:
  z = x + y
  y = x
  x = z
  i = i + 1
  print(z)

#13-Fatorial
%reset -f
print('Diga-me o numero que queres o fatorial')
n = int(input())
f = 1
i = 0
while i < n:
  f = f * (n - i)
  i = i + 1
print(f)

#14-dado conjunto
%reset -f
conj = [-1,4,1,1,2]
g = conj[0]#numero com index 0 na lista
l = conj[0]
sum = 0
for x in conj:#x irá automaticamente assumir o valor do numero no index 0, 1, etc 
  if x > g:
    g = x
  if x < l:
    l = x
  sum = sum + x
print(g)
print(l)
print(sum)

#15-Primo
%reset -f
n = int(input('diga-me um numero e checarei se ele é primo'))
i = 2
primo = True
while i < n:
  r = n % i
  i = i + 1
  if r == 0:
    primo = False
if primo:
  print('é primo')
else:
  print('n primo')

#16-ok Boomer ou ok Zoomer
%reset -f
npessoas = int(input('Diga-me o numero de pessoas que participarão do cálculo'))
n = 1
sumage = 0
while n <= npessoas:
  print('Diga-me quantos anos a',n,'º pessoa tem')
  age = int(input())
  sumage = sumage + age
  n = n + 1
media = int(sumage / npessoas)
print('a idade média dessas pessoas é de:',media)
if media < 26:
  print('Ok coletivo zoomer')
elif media < 61:
  print('Ok coletivo boomer')
elif media < 0:
  print('Ok coletivo viajante do tempo')
else:
  print('Ok coletivo boomer velho')

#20-20 só que "melhor" (entre aspas)
%reset -f 
print('1-Maçã                - R$2,11 o Kg')
print('2-Banana              - R$1,69 o Kg')
print('3-Cartela 12 ovos     - R$6,59')
print('4-Garrafa de Leite 2L - R$3,20')
print('5-Biscoito Mary       - R$4,31')
listaprodutos = ['Maçã','Banana','Cartela 12 ovos','2L garrafa de leite','Biscoito Mary']
produto = int(input('qual produto será comprado? 0 para sair da soma'))
total = 0
q1 = 0
q2 = 0
q3 = 0
q4 = 0
q5 = 0
while produto != 0: 
  if produto <= 2 and produto > 0:#2 é a quantidade de produtos vendidos por Kg
    print('Diga-me a quantidade de Kg de',listaprodutos[produto - 1])
    q = float(input())  
  elif produto > 0 and produto <= 5:#5 é a quantidade de produtos
    print('Diga-me quantas unidades de',listaprodutos[produto - 1])
    q = int(input())    
  elif produto == 0:
    print('EU NUNCA SEREI PRINTADO MINHA VIDA N TEM VALOR ALGUEM ME AJUDA AAAA')
  else:
    print('produto inválido')
  if produto == 1:
    total = total + q * 2.11
    q1 = q1 + q
  elif produto == 2:
    total = total + q * 1.69
    q2 = q2 + q
  if produto == 3:
    total = total + q * 6.59
    q3 = q3 + q
  elif produto == 4:
    total = total + q * 3.2
    q4 = q4 + q  
  elif produto == 5:
    total = total + q * 4.31 
    q5 = q5 + q 
  print('qual produto será comprado? 0 para sair da soma ')
  produto = int(input())
if q1 > 0:
  print(q1,'Kg X R$2.11 = ', q1 * 2.11)
if q2 > 0:
  print(q2,'Kg X R$1.69 = ', q2 * 1.69)
if q3 > 0:
  print(q3,'u X R$6.59 = ', q3 * 6.59)
if q4 > 0:
  print(q4,'u X R$3.2 = ', q4 * 3.2)
if q5 > 0:
  print(q5,'u X R$4.3 = ', q5 * 4.31)
print(total)

#21-numeros primos entre 1 e n
n = int(input('Diga-me um número e direi os primos entre ele e 1 '))
i = 2
j = 2
primo = True
while i < n:
  while j < i:
    r = i % j
    j = j + 1
    if r == 0:
      primo = False
  if primo:
    print(i)
  primo = True
  j = 2
  i = i + 1

#23-Juros por parcela
v = float(input('Diga-me o valor da compra'))
print('1- +0%')
print('3- +10%')
print('6- +15%')
print('9- +20%')
print('12- +25%')
p = int(input('Diga-me a quantidade de parcelas a serem pagas'))

if p % 3 != 0 and p !=1 and (p > 13 or p < 0):#não sei se os parenteses fazem efeito mas servem para ilustrar
  print('valor de parcelas invalido')
else:
  if p == 1:
    vv = v
  elif p == 3:
    v = v + v * 0.1
    vv = v / 3
  elif p == 6:
    v = v + v*0.15
    vv = vv / 6
  elif p == 9:
    v = v + v*0.2
    vv = v / 9
  elif p == 12:
    v = v + v*0.25
    vv = v / 12
  print('valor a ser pago:  ',v)
  print('valor das parcelas:',vv)

#24-Provas, notas, gabaritos.
%reset -f
r1 = "A"
r2 = "B"
r3 = "C"
r4 = "D"
r5 = "E"
r6 = "E"
r7 = "D"
r8 = "C"
r9 = "B"
r10= "A"
inp = ''
alunos = 0
acertost = 0
acertosg = 0
acertosl = 10
print('Olá professor!')
print('(caso tenha preguiça de apertar o botão que FIXA as letras para maiusculo, podes dar inputs minusculos tbm)')

while inp != 'R': 
  print('digite "A" para adicionar aluno e suas respostas')
  print('digite "M" para mudar as respostas do gabarito base (dados como acertos e n alunos serão apagados)')
  print('digite "R" para os resultados serem mostrados')
  inp = input()
  inp = inp.upper()
  if inp == 'M':
    acertost = 0
    alunos = 0
    print('Diga-me as novas respostas das quetões:')
    r1 = input('Questão 1:')
    r1 = r1.upper()
    r2 = input('Questão 2:')
    r2 = r2.upper()
    r3 = input('Questão 3:')
    r3 = r3.upper()
    r4 = input('Questão 4:')
    r4 = r4.upper()
    r5 = input('Questão 5:')
    r5 = r5.upper()
    r6 = input('Questão 6:')
    r6 = r6.upper()
    r7 = input('Questão 7:')
    r7 = r7.upper()
    r8 = input('Questão 8:')
    r8 = r8.upper()
    r9 = input('Questão 9:')
    r9 = r9.upper()
    r10 = input('Questão 10:')
    r10 = r10.upper()
  elif inp == 'A':
    alunos = alunos + 1
    print("Diga-me as respostas desse aluno:")
    r = input("Questão 1: ")
    r = r.upper()
    acertosa = 0
    if r == r1:
      acertosa = acertosa + 1
      acertost = acertost + 1
    r = input("Questão 2: ")
    r = r.upper()
    if r == r2:
      acertosa = acertosa + 1
      acertost = acertost + 1
    r = input("Questão 3: ")
    r = r.upper()
    if r == r3:
      acertosa = acertosa + 1
      acertost = acertost + 1
    r = input("Questão 4: ")
    r = r.upper()
    if r == r4:
      acertosa = acertosa + 1
      acertost = acertost + 1
    r = input("Questão 5: ")
    r = r.upper()
    if r == r5:
      acertosa = acertosa + 1
      acertost = acertost + 1
    r = input("Questão 6: ")
    r = r.upper()
    if r == r6:
      acertosa = acertosa + 1
      acertost = acertost + 1
    r = input("Questão 7: ")
    r = r.upper()
    if r == r7:
      acertosa = acertosa + 1
      acertost = acertost + 1
    r = input("Questão 8: ")
    r = r.upper()
    if r == r8:
      acertosa = acertosa + 1
      acertost = acertost + 1
    r = input("Questão 9: ")
    r = r.upper()
    if r == r9:
      acertosa = acertosa + 1
      acertost = acertost + 1
    r = input("Questão 10: ")
    r = r.upper()
    if r == r10:
      acertosa = acertosa + 1
      acertost = acertost + 1
    print('Este aluno acertou',acertosa,'questões')
    if acertosa > acertosg:
      acertosg = acertosa
    if acertosa < acertosl:
        acertosl = acertosa
if alunos > 0:
  print('número de alunos:',alunos)
  print('Quantidade de questões acertadas pelo aluno que mais acertou:',acertosg)
  print('Quantidade de questões acertadas pelo aluno que menos acertou:',acertosl)
  print('Média de acertos da turma:',acertost/alunos)
else:
  print('erro: dados não informados')

#25-oi io
%reset -f
n = str(input())
i = len(n)#pega a "largura" da string ou lista
while i > 0:
  i = i - 1
  print(n[i] ,end = '')

#26-somatoria 1/1 + 2/3 + 3/5 + 4/7 ... n/m
%reset -f
print('diga me n')
n = int(input())
sum = 0
i = 1
while i <= n:
  sum = sum + (i/(2 * i - 1))
  i = i + 1
print(sum)

#27-somatoria 1/1 + 1/2 + 1/3 ... 1/n
%reset -f
print('diga me n')
n = int(input())
sum = 0
i = 1
while i <= n:
  sum = sum + 1/i
  i = i + 1
print(sum)
