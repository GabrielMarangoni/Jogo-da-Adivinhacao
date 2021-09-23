from random import randint
print('-' * 40)

print('JOGO DA ADIVINHAÇÃO')

print('-' * 40)

print('Olá! Eu sou o computador :)')
print('Estou pensando em um número entre 1 e 100')
print('Consegue adivinhar qual é ?')
print()

palpites = 0 

cpu = randint(0,100)

acertou = False

while not acertou:
  jogador = int(input(' Seu Palpite : '))
  palpites += 1 

  if jogador == cpu:
    acertou = True
  else:
    if jogador < cpu:
      print('MAIOR...')
    elif jogador > cpu:
          print('MENOR...')

print('Parabéns você acertou !!')    
print(f'Total de tentativas: {palpites}')
print('-' * 40)

print('FIM! Obrigado por jogar :D')

print('-' * 40)
