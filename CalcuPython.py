import os

os.system("cls" if os.name == "nt" else "clear")

#Calculadora

#Cores

vermelho = ('\033[1;31m')

verde = ('\033[1;32m')

ciano = ('\033[1;90m')

branco = ('\033[1;97m')

azul = ('\033[1;34m')

#Começo do código

print(f'''

░▐█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▌
░░█▒▄▀▀▀▀▀▄▒▒▄▀▀▀▀▀▄▒▐███▌
░░░▐░░░▄▄░░▌▐░░░▄▄░░▌▐███▌
░▄▀▌░░░▀▀░░▌▐░░░▀▀░░▌▒▀▒█▌
░▌▒▀▄░░░░▄▀▒▒▀▄░░░▄▀▒▒▄▀▒▌
░▀▄▐▒▀▀▀▀▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒█
░░░▀▌▒▄██▄▄▄▄████▄▒▒▒▒█▀
░░░░▄██████████████▒▒▐▌
░░░▀███▀▀████▀█████▀▒▌
░░░░░▌▒▒▒▄▒▒▒▄▒▒▒▒▒▒▐▌
░░░░░▌▒▒▒▒▀▀▀▒▒▒▒▒▒▒▐▌
░░░▄▄▄▓▀▀░░░░░░░▒▒▒▀▀▀█▄
░░▐█░▄▀░░░░░░░░░░░░░░▀▄░░█▌
░░▐░▐░░░░░░░░░░░░░░░░░░▐░░▌
░░▐▐░░░░░░░▀▄▒▄▀░░░░░░░▐░░▌
░░▐▐░░░░░░░▒▒▐▒▒░░░░░░░▐░░▌
░░▐▐░░░▄░░░░▒▐▒░░░▄░░░░▐░░▌
░░▐▐▒░░░░░▒▒▒▐▒▒▒░░░░░░▐░░▌
░░▐░▀▄▒▒▒▒▒▄▀▒▀▄▒▒▒▒▒▄▀▌░░▌

''')

print('''
╔════•ೋೋ•════╗ 
 Calculadora
╚════•ೋೋ•════╝
''')

nome = str(input('Qual é seu nome?: '))

print(f'Bem vindo {nome}, fiz essa calculadora básica pra testar meus conhecimentos sobre python.')

print('Vamos começar!')

print(f'''{verde}
1 = Adição (+)
2 = Subtração (-)
3 = Multiplicação (×)
4 = Divisão (÷)
5 = Calcular raíz quadrada
6 = Dúvidas
7 = sair
''')

pg = int(input(f'{vermelho}Escolha uma das opções acima (escolha em forma de numero): '))

import time

if pg == (1):
	print('========= Adição ==========')
	a1 = int(input(f'{branco}Digite um valor: {branco}'))
	a2 = int(input(f'{branco}Digite outro valor: {branco}'))
	ra = (a1 + a2)
	print(f'{azul}O resultado dá: {ra}{azul}')
#End (1)
if pg == (2):
	print('========= Subtração ==========')
	s1 = int(input(f'{branco}Digite um valor: {branco}'))
	s2 = int(input(f'{branco}Digite outro valor: {branco}'))
	rs = (s1 - s2)
	print(f'{azul}O resultado deu {rs}{azul}')
#End (2)
if pg == (3):
	print('========= Multiplicação ==========')
	m1 = int(input(f'{branco}Digite um valor: {branco}'))
	m2 = int(input(f'{branco}Digite outro valor: {branco}'))
	rm = (m1 * m2)
	print(f'{azul}O resultado deu: {rm}{azul}')
#End (3)
if pg == (4):
	print('========= Divisão ==========')
	d1 = int(input(f'{branco}Digite um valor: {branco}'))
	d2 = int(input(f'{branco}Digite outro valor: {branco}'))
	rd = (d1 // d2)
	rd1 = (d1 % d2)
	print(f'{azul}O resultado dá: {rd}, e tem como resto: {rd1}{azul}')
#End (5)
if pg == (7):
	print(f'{ciano}Obg por usar! ;){ciano}')
	exit()
#End(6)

if pg == (5):
	print(f'{vermelho}PROCESSANDO...')
	time.sleep (3)
	print(f'{verde}========= Raíz Quadrada =========')
	import math
	num = int(input('Digite um número: '))
	raíz = math.sqrt(num)
	print(f'A raíz quadrada de {num} é: {raíz}')
if pg == (6):
	print('{azul}===== DÚVIDAS ======{azul}')
	print(f'Olá {nome}, Essa script não tem muitas opções, pois eu estou começando agora e ainda não sei quase nada, apenas ifs, prints, cores, variaveis, tipos primitivos, operadores aritmeticos e mais um pouquinho que eu não sei agora..')
	print('=== FIM ===')
	