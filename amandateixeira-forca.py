import random
#O módulo random implementa geradores de números ou palavras aleatórios.

palavras = []
#Criamos uma lista de palavras 
letrasErradas = ''
letrasCertas = ''
#Agora, temos uma variáel que mostrará o número de letras erradas e outra que mostraas letras acertadas.
FORCAIMG = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
#Aqui criamos nossa estrutura de jogo. A cada letra errada uma parte do bonequinho é adicionada e quando o mesmo é completado você perde o jogo.

#função que definirá as palavras serem recebidas.
def receberPalavras():
    global palavras
    while True:
        p = input("Digite as palavras desejadas: ")
        if p == '':
            break
        palavras.append(p)


def principal():
#Os blocos da função começam com a palavra-chave def seguida do nome da função e dos parênteses (()). Todos os argumentos devem ser colocados dentro dos parênteses.

    """
    Função Princial do programa
    """
    print('F O R C A')
#A função print serve para mostrar mensagens no programa.

    receberPalavras()
    palavraSecreta = sortearPalavra()
    palpite = ''
#Aqui você coloca seu palpite 
    desenhaJogo(palavraSecreta,palpite)

    while True:
#Executa um conjunto de instruções várias vezes enquanto verdade
        palpite = receberPalpite() 
        desenhaJogo(palavraSecreta,palpite)
        if perdeuJogo():
            print('Voce Perdeu!!!')
            break
        if ganhouJogo(palavraSecreta):
            print('Voce Ganhou!!!')
            break
#O if é uma estrutura que permite avaliar uma expressão. Já o break, faz com que o programa pare e retorne para a próxima situação.

       
def perdeuJogo():
    global FORCAIMG
#Global é um comando que indica que uma variável vale para todo o comando função.
    if len(letrasErradas) == len(FORCAIMG):
#A função len retorna o número de caracteres em uma lista.
        return True
#Nesse caso a função return true vai se referir ao número de letras erradas e ao desenho, se os mesmos estiverem correspondentes o programa me retorna que a função está correta
    else:
#false, se não.
        return False

    
def ganhouJogo(palavraSecreta):
    global letrasCertas
    ganhou = True
    for letra in palavraSecreta:
#for e in gera um loop dentro da lista ou seja vai procurar num loop uma letra dentro de palavraSecreta.
        if letra not in letrasCertas:
            ganhou = False
    return ganhou        
#se a letra estiver na palavra secreta você ganhou



def receberPalpite():
    
    palpite = input("Adivinhe uma letra: ")
#A função input() espera o usuário digitar um textos no teclado e pressionar ENTER.
    palpite = palpite.upper()
    if len(palpite) != 1:
        print('Coloque um unica letra.')
    elif palpite in letrasCertas or palpite in letrasErradas:
        print('Voce ja disse esta letra.')
#O elif será execultado somente quando todas as condições anteriores forem Falsas.
    elif not "A" <= palpite <= "Z":
        print('Por favor escolha apenas letras')
#O elif será execultado somente quando todas as condições anteriores não forem Falsas.
    else:
        return palpite
    
    
def desenhaJogo(palavraSecreta,palpite):
    global letrasCertas
    global letrasErradas
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)])
#Forma o desenho do homenzinho, de acordo com a quantidade de erros.
    
     
    vazio = len(palavraSecreta)*'-'
#Indica a quantidade de tracinhos '-'
    
    if palpite in palavraSecreta:
        letrasCertas += palpite
    else:
        letrasErradas += palpite

#Se o palpite estiver certo ele adiciona a letra no lugar do '-', caso esteja errado adiciona uma parte do bonequinho de acordo com seu erro.

    for letra in letrasCertas:
        for x in range(len(palavraSecreta)):
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]

#Percorre toda a palavra observando se tem a letra em algum dos espaços, indicado por um traço '-'
                
    print('Acertos: ',letrasCertas )
    print('Erros: ',letrasErradas)
    print(vazio)
     

def sortearPalavra():
    global palavras
    return random.choice(palavras).upper()
#"choice" sortea palavras e o "upper" coloca as letras em maiúsculo.

    
principal()
