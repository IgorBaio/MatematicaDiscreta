import OperacoesDoisConjuntos
import OperacoesTresConjuntos

print("\n\n")

input("A seguir será pedido para que insira dois arquivos de texto, para isso irá pedir para cada um,"+
" o repositório e o nome do arquivo, para continuar, pressione Enter.")

print("\n\n")

def PerguntaNovaOperacao(menu):
    contador = 0
    while contador < 25:
        resposta = input("\n\nDeseja fazer uma nova operação? (S/N) ")
        if resposta.lower() == "s":
            print(menu)
            contador += 1
        else:
            input("\n\nPressione enter para finalizar.\n\n")
            break

sistema = "w" #input("Usuario, voce utiliza Linux ou Windows?(L / W) ")

quantConjuntos = "3"#input("Deseja utilizar quantos conjuntos?(2 / 3) ")

textoArquivo = {}

if quantConjuntos == "2":
    OperacoesDoisConjuntos.PegaDoisConjuntos(sistema,textoArquivo)
    OperacoesDoisConjuntos.Menu(textoArquivo[1], textoArquivo[0])    
    contador = 0
    while contador < 25:
        resposta = input("\n\nDeseja fazer uma nova operação? (S/N) ")
        if resposta.lower() == "s":
            OperacoesDoisConjuntos.Menu(textoArquivo[1], textoArquivo[0])
            contador += 1
        else:
            input("\n\nPressione enter para finalizar.\n\n")
            break
else:
    OperacoesTresConjuntos.PegaTresConjuntos(sistema,textoArquivo)
    OperacoesTresConjuntos.Menu(textoArquivo[1], textoArquivo[2], textoArquivo[0])
    contador = 0
    while contador < 25:
        resposta = input("\n\nDeseja fazer uma nova operação? (S/N) ")
        if resposta.lower() == "s":
            OperacoesTresConjuntos.Menu(textoArquivo[1], textoArquivo[2], textoArquivo[0])
            contador += 1
        else:
            input("\n\nPressione enter para finalizar.\n\n")
            break
    

##
# Demais metodos ja estao com a logica atualizada, porem falta testa-los ainda
# #