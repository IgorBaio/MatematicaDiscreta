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

sistema = "l" #input("Usuario, voce utiliza Linux ou Windows?(L / W) ")

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
# Foi atualizado, testado, porem so de um lado e evitei de que algum elemento se repita, 
# fazer uma verificacao com maior qualidade
# #