while True:
  continuar = input('Deseja jogar o jogo da forca(s/n)? ')
  if continuar.lower() == 'n':
    break


  
  
  import random as rnd
  npalavra = rnd.randint(0, 7)
  nlista = rnd.randint(0, 2)
  guess = 0
  palavra1 = ''
  error = 0
  guesses = []
  
  frutas= ['maça', 'pera', 'laranja', 'uva', 'banana', 'manga', 'melancia', 'morango']
  animal=['cachorro', 'gato','papagaio', 'cavalo', 'camelo', 'girafa', 'rato', 'tigre']
  objeto=['cadeira', 'mesa', 'bolsa', 'fone', 'celular', 'notebook', 'lapis', 'tênis']
  
  if nlista == 0:
    palavra1 = frutas[npalavra]
  
  if nlista == 1:
    palavra1 = animal[npalavra]
  
  if nlista == 2:
    palavra1 = objeto[npalavra]
  
  incognita = '_' * len(palavra1)
  
  if nlista == 0:
    print('Sua palavra é da categoria FRUTAS')
  
  if nlista == 1:
    print('Sua palavra é da categoria ANIMAIS')
  
  if nlista == 2:
    print('Sua palavra é da categoria OBJETOS')
  
  print(incognita)
    
  while guess != 10:
    backup = '_' * len(palavra1)
    letra = input('Digite uma letra: ')
    if letra in guesses:
      print('Você já tentou essa letra')
      print()

    else:
      guesses.append(letra)
      for i in range(len(palavra1)):
        if letra == palavra1[i]:
          incognita = incognita[:i] + letra + incognita[i+1:]
          if incognita == palavra1:
            print(f'Parabéns, você acertou a palavra {palavra1.upper()}!')
            break
  
        else:
          error += 1
    
      if error == len(palavra1):
        guess += 1
        print('Você errou, tente novamente!')
        print(f'Você tem {10 - guess} tentativas')
    
      if palavra1 == incognita:
        break
    
      if guess == 10:
        print(f'Você perdeu, a palavra era {palavra1.upper()}')

      print(incognita)
  
      print('Você já tentou as seguintes letras: ', end = ' ')
      for element in guesses:
        print(element, end = ' ')
  
      print()
      print()
      error = 0   