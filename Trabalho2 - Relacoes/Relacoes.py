print("\n\n")

input("A seguir será pedido para que insira dois arquivos de texto, para isso irá pedir para cada um,"+
" o repositório e o nome do arquivo, para continuar, pressione Enter.")

print("\n\n")

sistema = input("Usuario, voce utiliza Linux ou Windows?(L / W) ")

if sistema.upper() == "W":
    print("\n\nConjunto A:")
    directory = input("Digite seu repositorio: ")
    directory = directory.replace("\\","\\\\" )
    nomeArquivo = input("Digite o nome do arquivo: ")
    nomeArquivo = nomeArquivo+".txt"
    directory = directory+"\\"+nomeArquivo
    arquivo = open(directory)
    textoArquivo = arquivo.read()


    print("\n\nConjunto B:")
    directory2 = input("Digite seu repositorio: ")
    directory2 = directory2.replace("\\","\\\\" )
    nomeArquivo2 = input("Digite o nome do arquivo: ")
    nomeArquivo2 = nomeArquivo2+".txt"
    directory2 = directory2+"\\"+nomeArquivo2
    arquivo2 = open(directory2)
    textoArquivo2 = arquivo2.read()

else:
    print("\n\nConjunto A:")
    directory = input("Digite seu repositorio: ")
    nomeArquivo = input("Digite o nome do arquivo: ")
    nomeArquivo = nomeArquivo+".txt"
    directory = directory+"/"+nomeArquivo
    arquivo = open(directory)
    textoArquivo = arquivo.read()
    
    print("\n\nConjunto B:")
    directory2 = input("Digite seu repositorio: ")
    nomeArquivo2 = input("Digite o nome do arquivo: ")
    nomeArquivo2 = nomeArquivo2+".txt"
    directory2 = directory2+"/"+nomeArquivo2
    arquivo2 = open(directory2)
    textoArquivo2 = arquivo2.read()

nomeConjunto = ["A","B","C","D","E","F","I","G","H","I","J","K","L","M","N","O",
                "P","Q","R","S","T","U","V","W","X","Y","Z"]

simbolos = ["=","{","}",",","\n","_", " ","[","]","'"]

conjuntos = []
    
def formataConjunto(conjunto):
    i = 0
    while i < simbolos.__len__():
        if conjunto.__contains__(simbolos[i]) and not simbolos[i] == "," :
            conjunto = conjunto.replace(simbolos[i],"")
        i+=1
    return conjunto

def RetiraNome(conjunto):
    i = 0
    while i < nomeConjunto.__len__():
        if conjunto.__contains__(nomeConjunto[i]):
            conjunto = conjunto.replace(nomeConjunto[i],"")
        i+=1
    return conjunto

def Elementos(conjunto):
    print("\n\nTotal de elementos = ", (conjunto.count(",")+1))
    print("Elementos: ")
    return PercorreConjunto(conjunto)

def PercorreConjunto(conjunto):
    conjuntoAux = []
    i = 0
    j = 0
    onlyNumbers = ""
    
    texto = RetiraNome(conjunto)
    texto = formataConjunto(texto)
    texto = texto.split(",")
  
    while i < texto.__len__():
        item = texto[i]
        if str.isdigit(item):
            onlyNumbers += item
            conjuntoAux.append(onlyNumbers)
            onlyNumbers = "" 
            i+=1
        else:
            while j < item.__len__():
                character = item[j]
                if str.isdigit(character):
                    onlyNumbers += character
                    conjuntoAux.append(onlyNumbers)
                    onlyNumbers = "" 
                    j+=1
                elif character == "-":
                    onlyNumbers = character
                    j+=1
                else:
                    j+=1
            j = 0
            i+=1

            onlyNumbers = "" 
    
    return conjuntoAux

def ProdutoCartesiano(conjuntoComparativo, conjuntoBase):
    conjuntoComparativoAux = str(PercorreConjunto(conjuntoComparativo))
    conjuntoComparativoAux = formataConjunto(conjuntoComparativoAux)
    conjuntoComparativoAux = conjuntoComparativoAux.split(",")
    

    conjuntoBaseAux = str(PercorreConjunto(conjuntoBase))
    conjuntoBaseAux = formataConjunto(conjuntoBaseAux)
    conjuntoBaseAux = conjuntoBaseAux.split(",")
    
    produtoCartesiano = []
    onlyNumbersBase = ""
    onlyNumbersComp = ""
    i = 0
    
    while i < conjuntoBaseAux.__len__():
        j = 0
        itemBase = conjuntoBaseAux[i]
        if itemBase.__contains__("-"):
            while j < conjuntoComparativoAux.__len__():
                onlyNumbersBase += itemBase
                itemComp = conjuntoComparativoAux[j]
                if str.isdigit(itemComp): 
                    onlyNumbersComp += itemComp
                    produtoCartesiano.append(onlyNumbersBase+","+onlyNumbersComp)
                    j+=1
                elif itemComp.__contains__("-"):
                    onlyNumbersComp = itemComp
                    produtoCartesiano.append(onlyNumbersBase+","+onlyNumbersComp)
                    j += 1
                onlyNumbersComp = ""
                onlyNumbersBase = ""

        else:    
            while j < conjuntoComparativoAux.__len__():
                onlyNumbersBase += itemBase
                itemComp = conjuntoComparativoAux[j]
                if str.isdigit(itemBase) and str.isdigit(itemComp): 
                    onlyNumbersComp += itemComp
                    produtoCartesiano.append(onlyNumbersBase+","+onlyNumbersComp)
                    j+=1
                elif itemComp.__contains__("-"):
                    onlyNumbersComp = itemComp
                    produtoCartesiano.append(onlyNumbersBase+","+onlyNumbersComp)
                    j += 1
                onlyNumbersComp = ""
                onlyNumbersBase = ""
    
            j += 1
            onlyNumbersComp = ""
            onlyNumbersBase = ""
        i += 1
    return produtoCartesiano
  
def MenorQue(conjuntoComparativo,conjuntoBase):
    conjuntoAuxBase = str(PercorreConjunto(conjuntoBase))
    conjuntoAuxBase = formataConjunto(conjuntoAuxBase)
    conjuntoAuxBase = conjuntoAuxBase.split(",")

    conjuntoAuxComparativo = str(PercorreConjunto(conjuntoComparativo))
    conjuntoAuxComparativo = formataConjunto(conjuntoAuxComparativo)
    conjuntoAuxComparativo = conjuntoAuxComparativo.split(",")

    conjuntoMenorQue = []
    i = 0
    while i < conjuntoAuxBase.__len__():
        j = 0
        a = conjuntoAuxBase[i]
        while j < conjuntoAuxComparativo.__len__():
            b = conjuntoAuxComparativo[j]
            if float(conjuntoAuxBase[i]) < float(conjuntoAuxComparativo[j]):
                conjuntoMenorQue.append(ProdutoCartesiano(conjuntoAuxComparativo[j], conjuntoAuxBase[i]))
                j += 1
            else:
                j += 1
        i += 1
    return conjuntoMenorQue


def MaiorQue(conjuntoComparativo,conjuntoBase):
    conjuntoAuxBase = str(PercorreConjunto(conjuntoBase))
    conjuntoAuxBase = formataConjunto(conjuntoAuxBase)
    conjuntoAuxBase = conjuntoAuxBase.split(",")

    conjuntoAuxComparativo = str(PercorreConjunto(conjuntoComparativo))
    conjuntoAuxComparativo = formataConjunto(conjuntoAuxComparativo)
    conjuntoAuxComparativo = conjuntoAuxComparativo.split(",")

    conjuntoMaiorQue = []
    i = 0
    while i < conjuntoAuxBase.__len__():
        j = 0
        while j < conjuntoAuxComparativo.__len__():
            if float(conjuntoAuxBase[i]) > float(conjuntoAuxComparativo[j]):
                conjuntoMaiorQue.append(ProdutoCartesiano(conjuntoAuxComparativo[j], conjuntoAuxBase[i]))
                j += 1
            else:
                j += 1
        i += 1
    return conjuntoMaiorQue

def IgualA(conjuntoComparativo,conjuntoBase):
    conjuntoAuxBase = str(PercorreConjunto(conjuntoBase))
    conjuntoAuxBase = formataConjunto(conjuntoAuxBase)
    conjuntoAuxBase = conjuntoAuxBase.split(",")

    conjuntoAuxComparativo = str(PercorreConjunto(conjuntoComparativo))
    conjuntoAuxComparativo = formataConjunto(conjuntoAuxComparativo)
    conjuntoAuxComparativo = conjuntoAuxComparativo.split(",")

    conjuntoIgualA = []
    i = 0
    while i < conjuntoAuxBase.__len__():
        j = 0
        while j < conjuntoAuxComparativo.__len__():
            if conjuntoAuxBase[i] == conjuntoAuxComparativo[j]:
                conjuntoIgualA.append(ProdutoCartesiano(conjuntoAuxComparativo[j], conjuntoAuxBase[i]))
                j += 1
            else:
                j += 1
        i += 1
    return conjuntoIgualA

def SerQuadradoDe(conjuntoComparativo,conjuntoBase):
    conjuntoAuxBase = str(PercorreConjunto(conjuntoBase))
    conjuntoAuxBase = formataConjunto(conjuntoAuxBase)
    conjuntoAuxBase = conjuntoAuxBase.split(",")

    conjuntoAuxComparativo = str(PercorreConjunto(conjuntoComparativo))
    conjuntoAuxComparativo = formataConjunto(conjuntoAuxComparativo)
    conjuntoAuxComparativo = conjuntoAuxComparativo.split(",")

    conjuntoSerQuadradoDe = []
    i = 0
    while i < conjuntoAuxBase.__len__():
        j = 0
        while j < conjuntoAuxComparativo.__len__():
            if int(conjuntoAuxBase[i]) == int(conjuntoAuxComparativo[j])*int(conjuntoAuxComparativo[j]):
                conjuntoSerQuadradoDe.append(ProdutoCartesiano(conjuntoAuxComparativo[j], conjuntoAuxBase[i]))
                j += 1
            else:
                j += 1
        i += 1
    return conjuntoSerQuadradoDe

def SerRaizDe(conjuntoComparativo,conjuntoBase):
    conjuntoAuxBase = str(PercorreConjunto(conjuntoBase))
    conjuntoAuxBase = formataConjunto(conjuntoAuxBase)
    conjuntoAuxBase = conjuntoAuxBase.split(",")

    conjuntoAuxComparativo = str(PercorreConjunto(conjuntoComparativo))
    conjuntoAuxComparativo = formataConjunto(conjuntoAuxComparativo)
    conjuntoAuxComparativo = conjuntoAuxComparativo.split(",")

    conjuntoSerRaizDe = []
    i = 0
    while i < conjuntoAuxBase.__len__():
        j = 0
        while j < conjuntoAuxComparativo.__len__():
            if conjuntoAuxBase[i].__contains__("-") or conjuntoAuxComparativo[j].__contains__("-"):
                j += 1
            elif float(conjuntoAuxBase[i]) == float(float(conjuntoAuxComparativo[j])**0.5):
                conjuntoSerRaizDe.append(ProdutoCartesiano(conjuntoAuxComparativo[j], conjuntoAuxBase[i]))
                j +=1
            else:
                j += 1
        i += 1
    return conjuntoSerRaizDe
    



def Menu(conjuntoComparativo, conjuntoBase):
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
        opcao = input("1 - Percorre A:\n2 - Percorre B: ")
        if opcao == "1":
            print("\nConjunto Percorrido: A = ",PercorreConjunto(conjuntoBase))
        elif opcao == "2":
            print("\nConjunto Percorrido: B = ",PercorreConjunto(conjuntoComparativo))
    elif valorMenu == 1:
        print("************************************")
        opcao = input("1 - A > B:\n2 - B > A: ")
        if opcao == "1":
            print("\n\nConjunto A",PercorreConjunto(conjuntoBase),"é Dominio e apresenta relacao Total.")
            print("\nConjunto B",PercorreConjunto(conjuntoComparativo),"é Imagem e apresenta relacao Sobrejetora.")
            print("\nMaior que:",MaiorQue(conjuntoComparativo, conjuntoBase))
        if opcao == "2":
            print("\n\nConjunto B",PercorreConjunto(conjuntoBase),"é Dominio e apresenta relacao Total.")
            print("\nConjunto A",PercorreConjunto(conjuntoComparativo),"é Imagem e apresenta relacao Sobrejetora.")
            print("\nMaior que:",MaiorQue(conjuntoBase, conjuntoComparativo))
    elif valorMenu == 2:
        opcao = input("1 - A < B:\n2 - B < A: ")
        if opcao == "1":
            print("\n\nConjunto A",PercorreConjunto(conjuntoBase),"é Dominio e apresenta relacao Total.")
            print("\nConjunto B",PercorreConjunto(conjuntoComparativo),"é Imagem e apresenta relacao Sobrejetora.")
            print("\nMenor que:",MenorQue(conjuntoComparativo, conjuntoBase))
        if opcao == "2":
            print("\n\nConjunto B",PercorreConjunto(conjuntoBase),"é Dominio e apresenta relacao Total.")
            print("\nConjunto A",PercorreConjunto(conjuntoComparativo),"é Imagem e apresenta relacao Sobrejetora.")
            print("\nMenor que:",MenorQue(conjuntoBase, conjuntoComparativo))
    elif valorMenu == 3:
        opcao = input("1 - A = B:\n2 - B = A: ")
        if opcao == "1":
            print("\n\nConjunto A",PercorreConjunto(conjuntoBase),"é Dominio e apresenta relacao Total.")
            print("\nConjunto B",PercorreConjunto(conjuntoComparativo),"é Imagem e apresenta relacao Sobrejetora.")
            print("\nIgual a:",IgualA(conjuntoComparativo, conjuntoBase))
        if opcao == "2":
            print("\n\nConjunto B",PercorreConjunto(conjuntoBase),"é Dominio e apresenta relacao Total.")
            print("\nConjunto A",PercorreConjunto(conjuntoComparativo),"é Imagem e apresenta relacao Sobrejetora.")
            print("\nIgual a:",IgualA(conjuntoComparativo, conjuntoBase))
    elif valorMenu == 4:
        opcao = input("1 - A ser quadrado de B:\n2 - B ser quadrado de A: ")
        if opcao == "1":
            print("\n\nConjunto A",PercorreConjunto(conjuntoBase),"é Dominio e apresenta relacao Funcional.")
            print("\nConjunto B",PercorreConjunto(conjuntoComparativo),"é Imagem e apresenta relacao Injetora.")
            print("\nConjuntos de quadrados:",SerQuadradoDe(conjuntoComparativo, conjuntoBase))
        if opcao == "2":
            print("\n\nConjunto B",PercorreConjunto(conjuntoBase),"é Dominio e apresenta relacao Funcional.")
            print("\nConjunto A",PercorreConjunto(conjuntoComparativo),"é Imagem e apresenta relacao Injetora.")
            print("\nConjuntos de quadrados:",SerQuadradoDe(conjuntoBase, conjuntoComparativo))
    elif valorMenu == 5:
        opcao = input("1 - A ser raiz de B:\n2 - B ser raiz de A: ")
        if opcao == "1":
            print("\n\nConjunto A",PercorreConjunto(conjuntoBase),"é Dominio e apresenta relacao Funcional.")
            print("\nConjunto B",PercorreConjunto(conjuntoComparativo),"é Imagem e apresenta relacao Injetora.")
            print("\nConjuntos de raizes:",SerRaizDe(conjuntoComparativo, conjuntoBase))
        if opcao == "2":
            print("\n\nConjunto B",PercorreConjunto(conjuntoBase),"é Dominio e apresenta relacao Funcional.")
            print("\nConjunto A",PercorreConjunto(conjuntoComparativo),"é Imagem e apresenta relacao Injetora.")
            print("\nConjuntos de raizes:",SerRaizDe(conjuntoBase, conjuntoComparativo))
   

Menu(textoArquivo2, textoArquivo)
contador = 0
while contador < 25:
    resposta = input("\n\nDeseja fazer uma nova operação? (S/N) ")
    if resposta.lower() == "s":
        Menu(textoArquivo2,textoArquivo)
        contador += 1
    else:
        input("\n\nPressione enter para finalizar.\n\n")
        break