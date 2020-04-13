import OperacoesDoisConjuntos as Operacoes


def PegaTresConjuntos(sistema,textoArquivo):
    if sistema.upper() == "W":
        Operacoes.PerguntaWindows(textoArquivo)

        print("\n\nConjunto C:")
        directory3 ="D:\\Projetos\\MatematicaDiscreta" #input("Digite seu repositorio: ")
        nomeArquivo3 = "texto2" #input("Digite o nome do arquivo: ")
        nomeArquivo3 = nomeArquivo3+".txt"
        directory3 = directory3+"\\"+nomeArquivo3
        arquivo3 = open(directory3)
        textoArquivo[2] = arquivo3.read()

    else:
        Operacoes.PerguntaLinux(textoArquivo)
        
        print("\n\nConjunto C:")
        directory3 = "/home/igorbaio/Documentos/MatematicaDiscreta/" #input("Digite seu repositorio: ")
        nomeArquivo3 = "texto2"#input("Digite o nome do arquivo: ")
        nomeArquivo3 = nomeArquivo3+".txt"
        directory3 = directory3+"/"+nomeArquivo3
        arquivo3 = open(directory3)
        textoArquivo[2] = arquivo3.read()


def PreparaTerceiroConjunto(conjuntoAuxBase, conjuntoPrimeiroElementoBase, conjuntoSegundoElementoBase):
    conjuntoElementos = []
    k = 0
    while k < conjuntoAuxBase.__len__():
        l=0
        conjuntoElementos = str(conjuntoAuxBase[k]).split(",")
        while l < conjuntoElementos.__len__():
            elemento = Operacoes.formataConjunto(conjuntoElementos[l])
            if l == 0:
                conjuntoPrimeiroElementoBase.append(elemento)
                l+=1
            else:
                conjuntoSegundoElementoBase.append(elemento)
                l+=1
        k+=1
    
def PreparaComparativo(conjuntoComp):
    conjuntoAuxComparativo = str(Operacoes.PercorreConjunto(conjuntoComp))
    conjuntoAuxComparativo = Operacoes.formataConjunto(conjuntoAuxComparativo)
    conjuntoAuxComparativo = conjuntoAuxComparativo.split(",")
    return conjuntoAuxComparativo

def MaiorQue(conjuntoComparativo1, conjuntoComparativo2,conjuntoBase,indicadorBase):
    
    
    conjuntoAuxBase = Operacoes.MaiorQue(conjuntoComparativo1, conjuntoBase)
    conjuntoAuxComparativo = PreparaComparativo(conjuntoComparativo2)
    
    conjuntoPrimeiroElementoBase = []
    conjuntoSegundoElementoBase = []

    PreparaTerceiroConjunto(conjuntoAuxBase, conjuntoPrimeiroElementoBase, conjuntoSegundoElementoBase)


    

    conjuntoMaiorQue = []
    i = 0
    while i < conjuntoSegundoElementoBase.__len__():
        j = 0
        while j < conjuntoAuxComparativo.__len__():
            if float(conjuntoSegundoElementoBase[i]) > float(conjuntoAuxComparativo[j]):
                conjuntoMaiorQue.append(Operacoes.ProdutoCartesiano(conjuntoAuxComparativo[j], conjuntoPrimeiroElementoBase[i]))
                j += 1
            else:
                j += 1
        i += 1
    return conjuntoMaiorQue

def MenorQue(conjuntoComparativo1, conjuntoComparativo2,conjuntoBase):
    conjuntoAuxBase = Operacoes.MenorQue(conjuntoComparativo1, conjuntoBase)
    conjuntoAuxComparativo = PreparaComparativo(conjuntoComparativo2)
    
    conjuntoPrimeiroElementoBase = []
    conjuntoSegundoElementoBase = []

    PreparaTerceiroConjunto(conjuntoAuxBase, conjuntoPrimeiroElementoBase, conjuntoSegundoElementoBase)

    conjuntoMenorQue = []
    i = 0
    while i < conjuntoSegundoElementoBase.__len__():
        j = 0
        while j < conjuntoAuxComparativo.__len__():
            if float(conjuntoSegundoElementoBase[i]) < float(conjuntoAuxComparativo[j]):
                conjuntoMenorQue.append(Operacoes.ProdutoCartesiano(conjuntoAuxComparativo[j], conjuntoPrimeiroElementoBase[i]))
                j += 1
            else:
                j += 1
        i += 1
    return conjuntoMenorQue


def IgualA(conjuntoComparativo1, conjuntoComparativo2, conjuntoBase):
    conjuntoAuxBase = Operacoes.IgualA(conjuntoComparativo1, conjuntoBase)
    conjuntoAuxComparativo = PreparaComparativo(conjuntoComparativo2)
    
    conjuntoPrimeiroElementoBase = []
    conjuntoSegundoElementoBase = []

    PreparaTerceiroConjunto(conjuntoAuxBase, conjuntoPrimeiroElementoBase, conjuntoSegundoElementoBase)

    conjuntoIgualA = []
    i = 0
    while i < conjuntoSegundoElementoBase.__len__():
        j = 0
        while j < conjuntoAuxComparativo.__len__():
            if float(conjuntoSegundoElementoBase[i]) < float(conjuntoAuxComparativo[j]):
                conjuntoIgualA.append(Operacoes.ProdutoCartesiano(conjuntoAuxComparativo[j], conjuntoPrimeiroElementoBase[i]))
                j += 1
            else:
                j += 1
        i += 1
    return conjuntoIgualA

def SerQuadradoDe(conjuntoComparativo1, conjuntoComparativo2, conjuntoBase):
    conjuntoAuxBase = Operacoes.SerQuadradoDe(conjuntoComparativo1, conjuntoBase)
    conjuntoAuxComparativo = PreparaComparativo(conjuntoComparativo2)
    
    conjuntoPrimeiroElementoBase = []
    conjuntoSegundoElementoBase = []

    PreparaTerceiroConjunto(conjuntoAuxBase, conjuntoPrimeiroElementoBase, conjuntoSegundoElementoBase)

    conjuntoSerQuadradoDe = []
    i = 0
    while i < conjuntoSegundoElementoBase.__len__():
        j = 0
        while j < conjuntoAuxComparativo.__len__():
            if int(conjuntoSegundoElementoBase[i]) == int(conjuntoAuxComparativo[j])*int(conjuntoAuxComparativo[j]):
                conjuntoSerQuadradoDe.append(Operacoes.ProdutoCartesiano(conjuntoAuxComparativo[j], conjuntoSegundoElementoBase[i]))
                j += 1
            else:
                j += 1
        i += 1
    return conjuntoSerQuadradoDe

def SerRaizDe(conjuntoComparativo1, conjuntoComparativo2, conjuntoBase):
    conjuntoAuxBase = Operacoes.SerRaizDe(conjuntoComparativo1, conjuntoBase)
    conjuntoAuxComparativo = PreparaComparativo(conjuntoComparativo2)
    
    conjuntoPrimeiroElementoBase = []
    conjuntoSegundoElementoBase = []

    PreparaTerceiroConjunto(conjuntoAuxBase, conjuntoPrimeiroElementoBase, conjuntoSegundoElementoBase)


    conjuntoSerRaizDe = []
    i = 0
    while i < conjuntoSegundoElementoBase.__len__():
        j = 0
        while j < conjuntoAuxComparativo.__len__():
            if conjuntoSegundoElementoBase[i].__contains__("-") or conjuntoAuxComparativo[j].__contains__("-"):
                j += 1
            elif float(conjuntoSegundoElementoBase[i]) == float(float(conjuntoAuxComparativo[j])**0.5):
                conjuntoSerRaizDe.append(Operacoes.ProdutoCartesiano(conjuntoAuxComparativo[j], conjuntoAuxBase[i]))
                j +=1
            else:
                j += 1
        i += 1
    return conjuntoSerRaizDe
  

def Menu(conjuntoComparativo1, conjuntoComparativo2 , conjuntoBase):
    print("**************************************\n")
    print("OPERAÇÕES:\n")
    print("0 - Percorre\n")
    print("1 - Maior que\n")
    print("2 - Menor que\n")
    print("3 - Igual a\n")
    print("4 - Ser o quadrado de\n")
    print("5 - Ser a raiz quadrada de\n")
    print("**************************************\n")

    valorMenu = int(input("Digite o valor correspondente a operação desejada: "))

    if valorMenu == 0:
        print("************************************")
        opcao = input("1 - Percorre A:\n2 - Percorre B:\n2 - Percorre C: ")
        if opcao == "1":
            print("\nConjunto Percorrido: A = ",Operacoes.PercorreConjunto(conjuntoBase))
        elif opcao == "2":
            print("\nConjunto Percorrido: B = ",Operacoes.PercorreConjunto(conjuntoComparativo1))
        elif opcao == "3":
            print("\nConjunto Percorrido: C = ",Operacoes.PercorreConjunto(conjuntoComparativo2))
    elif valorMenu == 1:
        print("************************************")
        opcao = input("1 - A > C:\n2 - C > A: ")
        if opcao == "1":
            print("\n\nConjunto A",Operacoes.PercorreConjunto(conjuntoBase),"é Dominio e apresenta relacao Total.")
            print("\nConjunto B",Operacoes.PercorreConjunto(conjuntoComparativo1),"é Imagem e apresenta relacao Sobrejetora.")
            print("\nMaior que:",MaiorQue(conjuntoComparativo1, conjuntoComparativo2, conjuntoBase,"A"))
        if opcao == "2":
            print("\n\nConjunto B",Operacoes.PercorreConjunto(conjuntoBase),"é Dominio e apresenta relacao Total.")
            print("\nConjunto A",Operacoes.PercorreConjunto(conjuntoComparativo1),"é Imagem e apresenta relacao Sobrejetora.")
            print("\nMaior que:",MaiorQue(conjuntoComparativo1, conjuntoBase, conjuntoComparativo2,"C"))
    elif valorMenu == 2:
        opcao = input("1 - A < B:\n2 - B < A: ")
        if opcao == "1":
            print("\n\nConjunto A",Operacoes.PercorreConjunto(conjuntoBase),"é Dominio e apresenta relacao Total.")
            print("\nConjunto B",Operacoes.PercorreConjunto(conjuntoComparativo1),"é Imagem e apresenta relacao Sobrejetora.")
            print("\nMenor que:",MenorQue(conjuntoComparativo1, conjuntoComparativo2, conjuntoBase))
        if opcao == "2":
            print("\n\nConjunto B",Operacoes.PercorreConjunto(conjuntoBase),"é Dominio e apresenta relacao Total.")
            print("\nConjunto A",Operacoes.PercorreConjunto(conjuntoComparativo1),"é Imagem e apresenta relacao Sobrejetora.")
            print("\nMenor que:",MenorQue(conjuntoComparativo1, conjuntoBase, conjuntoComparativo2))
    elif valorMenu == 3:
        opcao = input("1 - A = B:\n2 - B = A: ")
        if opcao == "1":
            print("\n\nConjunto A",Operacoes.PercorreConjunto(conjuntoBase),"é Dominio e apresenta relacao Total.")
            print("\nConjunto B",Operacoes.PercorreConjunto(conjuntoComparativo1),"é Imagem e apresenta relacao Sobrejetora.")
            print("\nIgual a:",IgualA(conjuntoComparativo1, conjuntoComparativo2, conjuntoBase))
        if opcao == "2":
            print("\n\nConjunto B",Operacoes.PercorreConjunto(conjuntoBase),"é Dominio e apresenta relacao Total.")
            print("\nConjunto A",Operacoes.PercorreConjunto(conjuntoComparativo1),"é Imagem e apresenta relacao Sobrejetora.")
            print("\nIgual a:",IgualA(conjuntoComparativo1, conjuntoBase, conjuntoComparativo2))
    elif valorMenu == 4:
        opcao = input("1 - A ser quadrado de B:\n2 - B ser quadrado de A: ")
        if opcao == "1":
            print("\n\nConjunto A",Operacoes.PercorreConjunto(conjuntoBase),"é Dominio e apresenta relacao Funcional.")
            print("\nConjunto B",Operacoes.PercorreConjunto(conjuntoComparativo1),"é Imagem e apresenta relacao Injetora.")
            print("\nConjuntos de quadrados:",SerQuadradoDe(conjuntoComparativo1, conjuntoComparativo2, conjuntoBase))
        if opcao == "2":
            print("\n\nConjunto B",Operacoes.PercorreConjunto(conjuntoBase),"é Dominio e apresenta relacao Funcional.")
            print("\nConjunto A",Operacoes.PercorreConjunto(conjuntoComparativo1),"é Imagem e apresenta relacao Injetora.")
            print("\nConjuntos de quadrados:",SerQuadradoDe(conjuntoComparativo1, conjuntoBase, conjuntoComparativo2))
    elif valorMenu == 5:
        opcao = input("1 - A ser raiz de B:\n2 - B ser raiz de A: ")
        if opcao == "1":
            print("\n\nConjunto A",Operacoes.PercorreConjunto(conjuntoBase),"é Dominio e apresenta relacao Funcional.")
            print("\nConjunto B",Operacoes.PercorreConjunto(conjuntoComparativo1),"é Imagem e apresenta relacao Injetora.")
            print("\nConjuntos de raizes:",SerRaizDe(conjuntoComparativo1, conjuntoComparativo2, conjuntoBase))
        if opcao == "2":
            print("\n\nConjunto B",Operacoes.PercorreConjunto(conjuntoBase),"é Dominio e apresenta relacao Funcional.")
            print("\nConjunto A",Operacoes.PercorreConjunto(conjuntoComparativo1),"é Imagem e apresenta relacao Injetora.")
            print("\nConjuntos de raizes:",SerRaizDe(conjuntoComparativo1, conjuntoBase, conjuntoComparativo2))
  