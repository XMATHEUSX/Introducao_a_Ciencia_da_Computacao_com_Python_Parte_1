def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada?"))
    if n%(m+1):
        print("\n Você começa! \n")
        n = usuario_escolhe_jogada(n,m)
        usuario_jogando = True
    else:
        print("\n Computador começa! \n")
        n = computador_escolhe_jogada(n,m)
        usuario_jogando = False
    while n != 0:
        if  usuario_jogando = False:
            n = usuario_escolhe_jogada(n,m)
            usuario_jogando = True
        else:
            n = computador_escolhe_jogada(n,m)
            usuario_jogando = False



def computador_escolhe_jogada(n,m): 
    deixar = m + 1
    tirar = n - deixar 
    print("\n Agora resta apenas ,"n-tirar", peça no tabuleiro. \n")
    n = n- tirar 
    return n
    

def usuario_escolhe_jogada(n,m):
    while True:
        tirar = int(input("Quantas peças você vai tirar ? "))
        if tirar > m or tirar > n :
            print("\n Oops! Jogada inválida! Tente de novo. \n")
        else:
            print("\n Você tirou" ,tirar," peça \n")
            break
    print("\n Agora resta apenas ,"n-tirar", peça no tabuleiro. \n")
    n = n- tirar 
    return n
