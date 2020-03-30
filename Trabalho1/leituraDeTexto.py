directory = input("Digite seu repositorio: ")
directory = directory.replace("\\","\\\\" )
nomeArquivo = input("Digite o nome do arquivo: ")
nomeArquivo = nomeArquivo+".txt"
directory = directory+"\\"+nomeArquivo

arquivo = open(directory)
textoArquivo = arquivo.read()

directory2 = input("Digite seu repositorio: ")
directory2 = directory2.replace("\\","\\\\" )
nomeArquivo2 = input("Digite o nome do arquivo: ")
nomeArquivo2 = nomeArquivo2+".txt"
directory2 = directory2+"\\"+nomeArquivo2

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

def PercorreConjunto(conjunto):
    conjuntoAux = []
    i = 0
    j = 0
    print("Total de elementos = ", (conjunto.count(",")+1))
    print("Elementos: ")
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
    print(conjuntoAux)
    return conjuntoAux
         

def Pertence(numero, conjunto):
    if conjunto.__contains__(numero):
        mensagem = "O número "+numero+" pertence ao conjunto "+conjunto
        return mensagem
    else:
        return "O número "+numero+" não pertence ao conjunto "+conjunto
 
def ContidoOuIgual(conjuntoComparativo,conjuntoBase):
    if conjuntoBase == conjuntoComparativo and set(conjuntoComparativo).issubset(set(conjuntoBase)):
        mensagem = "O conjunto comparativo é contido ou igual ao conjunto base"
        return mensagem
    elif set(conjuntoComparativo).issubset(set(conjuntoBase)) and not conjuntoBase == conjuntoComparativo:
        return ContidoPropriamente(conjuntoComparativo,conjuntoBase)
    else:
        mensagem = "O conjunto comparativo não está contido no conjunto base"
        return mensagem

def ContidoPropriamente(conjuntoComparativo,conjuntoBase):
    if set(conjuntoComparativo).issubset(set(conjuntoBase)):
        mensagem = "O conjunto comparativo está contido propriamente no conjunto base."
        return mensagem
    else:
        mensagem = "O conjunto comparativo não está contido no conjunto base"
        return mensagem
   


def Uniao(conjuntoComparativo,conjuntoBase):
    conjuntoAuxBase = str(PercorreConjunto(conjuntoBase))
    conjuntoAuxBase = formataConjunto(conjuntoAuxBase)
    conjuntoAuxComparativo = str(PercorreConjunto(conjuntoComparativo))
    conjuntoAuxComparativo = formataConjunto(conjuntoAuxComparativo)   
    a = DiferencaDeConjuntos(conjuntoAuxBase, conjuntoAuxComparativo)
    nomeDaUniao = input("Digite a letra do nome do conjunto: ")
    if conjuntoAuxBase == conjuntoAuxComparativo:
        mensagem = "Conjunto "+nomeDaUniao+" = { "+conjuntoAuxBase+" }"
        return mensagem
    elif not a == [] :
        diferenca =  str(DiferencaDeConjuntos(conjuntoAuxBase, conjuntoAuxComparativo))
        diferenca = formataConjunto(diferenca)
        mensagem = "Conjunto "+nomeDaUniao+" = { "+conjuntoAuxBase+", "+diferenca+" }"
        return mensagem
    else:
        mensagem = "Conjunto "+nomeDaUniao+" = { "+conjuntoAuxBase+", "+conjuntoAuxComparativo+" }"
        return mensagem



def Intersecao(conjuntoComparativo,conjuntoBase):
    intersecao = []
    conjuntoAuxBase = PercorreConjunto(conjuntoBase)
    conjuntoAuxComparativo = PercorreConjunto(conjuntoComparativo)
    i = 0
    while i < conjuntoAuxBase.__len__():
        if conjuntoAuxComparativo.__contains__(conjuntoAuxBase[i]):
            intersecao.append(conjuntoAuxBase[i])
        
        i+=1
    
    return intersecao

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
    
    
def DiferencaDeConjuntos(conjuntoComparativo, conjuntoBase):
    intersecao = str(Intersecao(conjuntoComparativo, conjuntoBase))
    i = 0
    conjuntoBaseAux = str(PercorreConjunto(conjuntoBase))
    conjuntoBaseAux = formataConjunto(conjuntoBaseAux)
    conjuntoBaseAux = conjuntoBaseAux.split(",")

    intersecao = formataConjunto(intersecao)
    intersecao = intersecao.split(",")

    while i < conjuntoBaseAux.__len__():
        j = 0
        while j < intersecao.__len__():
            if not intersecao[j] == conjuntoBaseAux[i] and conjuntoBaseAux.__contains__(intersecao[j]):
                conjuntoBaseAux.remove(intersecao[j])
            j += 1
        i +=1
    return conjuntoBaseAux


def Menu(conjuntoComparativo, conjuntoBase):
    print("**************************************\n")
    print("OPERAÇÕES:\n")
    print("0 - Percorre\n")
    print("1 - Pertence/ Não pertence\n")
    print("2 - Contido ou igual/ Não contido ou igual \n")
    print("3 - Contido propriamente/ Não contido propriamente\n")
    print("4 - União\n")
    print("5 - Interseção\n")
    print("6 - Produto Cartesiano\n")
    print("7 - Diferença de conjuntos\n")
    print("**************************************\n")

    valorMenu = int(input("Digite o valor correspondente a operação desejada: "))

    if valorMenu == 0:
        print(PercorreConjunto(conjuntoBase))
    elif valorMenu == 1:
        valor = input("Digite o valor que deseja procurar no conjunto: ")
        print(Pertence(valor, textoArquivo))        
    elif valorMenu == 2:
        print(ContidoOuIgual(conjuntoComparativo, conjuntoBase))
    elif valorMenu == 3:
        print(ContidoOuIgual(conjuntoComparativo, conjuntoBase))
    elif valorMenu == 4:
        print(Uniao(conjuntoComparativo,conjuntoBase))
    elif valorMenu == 5:
        print(Intersecao(conjuntoComparativo, conjuntoBase))
    elif valorMenu == 6:
        print(ProdutoCartesiano(conjuntoComparativo,conjuntoBase))
    elif valorMenu == 7:
        print("Diferença de conjunto:",DiferencaDeConjuntos(conjuntoComparativo,conjuntoBase))

Menu(textoArquivo2, textoArquivo)