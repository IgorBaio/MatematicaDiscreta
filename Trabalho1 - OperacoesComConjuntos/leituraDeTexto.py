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
            a = item.__len__()
            while j < item.__len__():
                character = item[j]
                if str.isdigit(character):
                    onlyNumbers += character
                    #Aqui, ele so pegava o primeiro numero após o sinal de "-"
                    if j == (item.__len__() - 1):
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

def Pertence(numero, conjunto):
    conjuntoAux = str(PercorreConjunto(conjunto))
    conjuntoAux = formataConjunto(conjuntoAux)
    conjuntoAux = conjuntoAux.split(",")
    i = 0
    while i < conjuntoAux.__len__():
        if conjuntoAux[i] == numero:
            mensagem = "O número "+numero+" pertence ao conjunto "+conjunto
            return mensagem
        else:
            i += 1
    mensagem = "O número "+numero+" não pertence ao conjunto "+conjunto
    return mensagem
    

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
    diferenca = DiferencaDeConjuntos(conjuntoAuxBase, conjuntoAuxComparativo)
    nomeDaUniao = input("Digite a letra do nome do conjunto: ")
    if conjuntoAuxBase == conjuntoAuxComparativo or diferenca == [] :
        mensagem = "Conjunto "+nomeDaUniao.upper()+" = { "+conjuntoAuxBase+" }"
        return mensagem
    elif not diferenca == [] :
        diferenca =  str(diferenca)
        diferenca = formataConjunto(diferenca)
        mensagem = "Conjunto "+nomeDaUniao.upper()+" = { "+conjuntoAuxBase+", "+diferenca+" }"
        return mensagem
    else:
        mensagem = "Conjunto "+nomeDaUniao.upper()+" = { "+conjuntoAuxBase+", "+conjuntoAuxComparativo+" }"
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
            if intersecao[j] == conjuntoBaseAux[i]:
                conjuntoBaseAux.remove(intersecao[j])
            j += 1
        i +=1
    return conjuntoBaseAux

def ConjuntoPartes(conjunto):
    
    conjuntoPartes = []
    conjunto = str(PercorreConjunto(conjunto))
    conjunto = formataConjunto(conjunto)
    conjunto = conjunto.split(",")
    conjuntoPartes.append("{}")
    i = 0
    while i < conjunto.__len__():
        aux = "{" + conjunto[i] + "}"
        conjuntoPartes.append(aux)
        i += 1

    x = 0
    if conjunto.__len__() >= 2:
        while x < conjunto.__len__():
            y = x+1
            while y < conjunto.__len__():
                conj = "{"+conjunto[x]+","+conjunto[y]+"}"
                conjuntoPartes.append(conj)
                y+=1
            x+=1

    x = 0
    if conjunto.__len__() >= 3:
        while x < conjunto.__len__():
            y = x+1
            while y < conjunto.__len__():
                z = y+1
                while z < conjunto.__len__():
                    conj = "{"+conjunto[x]+","+conjunto[y]+","+conjunto[z]+"}"
                    conjuntoPartes.append(conj)
                    z+=1
                y+=1
            x+=1
    
    x = 0
    if conjunto.__len__() >= 4:
        while x < conjunto.__len__():
            y = x+1
            while y < conjunto.__len__():
                z = y+1
                while z < conjunto.__len__():
                    a = z+1
                    while a < conjunto.__len__():
                        conj = "{"+conjunto[x]+","+conjunto[y]+","+conjunto[z]+","+conjunto[a]+"}"
                        conjuntoPartes.append(conj)
                        a+=1
                    z+=1
                y+=1
            x+=1

    x = 0
    if conjunto.__len__() >= 5:
        while x < conjunto.__len__():
            y = x+1
            while y < conjunto.__len__():
                z = y+1
                while z < conjunto.__len__():
                    a = z+1
                    while a < conjunto.__len__():
                        b = a+1
                        while b < conjunto.__len__():
                            conj = "{"+conjunto[x]+","+conjunto[y]+","+conjunto[z]+","+conjunto[a]+","+conjunto[b]+"}"
                            conjuntoPartes.append(conj)
                            b+=1
                        a+=1
                    z+=1
                y+=1
            x+=1

    x = 0
    if conjunto.__len__() >= 6:
        while x < conjunto.__len__():
            y = x+1
            while y < conjunto.__len__():
                z = y+1
                while z < conjunto.__len__():
                    a = z+1
                    while a < conjunto.__len__():
                        b = a+1
                        while b < conjunto.__len__():
                            c = b+1
                            while c < conjunto.__len__():
                                conj = "{"+conjunto[x]+","+conjunto[y]+","+conjunto[z]+","+conjunto[a]+","+conjunto[b]+","+conjunto[c]+"}"
                                conjuntoPartes.append(conj)
                                c+=1
                            b+=1
                        a+=1
                    z+=1
                y+=1
            x+=1

    x = 0
    if conjunto.__len__() >= 7:
        while x < conjunto.__len__():
            y = x+1
            while y < conjunto.__len__():
                z = y+1
                while z < conjunto.__len__():
                    a = z+1
                    while a < conjunto.__len__():
                        b = a+1
                        while b < conjunto.__len__():
                            c = b+1
                            while c < conjunto.__len__():
                                d = c+1
                                while d < conjunto.__len__():
                                    conj = "{"+conjunto[x]+","+conjunto[y]+","+conjunto[z]+","+conjunto[a]+","+conjunto[b]+","+conjunto[c]+","+conjunto[d]+"}"
                                    conjuntoPartes.append(conj)
                                    d+=1
                                c+=1
                            b+=1
                        a+=1
                    z+=1
                y+=1
            x+=1
    
    return conjuntoPartes


def Menu(conjuntoComparativo, conjuntoBase):
    print("**************************************\n")
    print("OPERAÇÕES:\n")
    print("0 - Percorre\n")
    print("1 - Pertence/ Não pertence\n")
    print("2 - Contido ou igual/ Não contido ou igual \n")
    print("3 - Contido propriamente/ Não contido propriamente\n")
    print("4 - União\n")
    print("5 - Interseção\n")
    print("6 - Produto Cartesiano (AXB)\n")
    print("7 - Diferença de conjuntos\n")
    print("8 - Exibir elementos\n")
    print("9 - Conjunto das Partes\n")
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
        opcao = input("1 - Pertence ao Conjunto A:\n2 - Pertence ao Conjunto B: ")
        if opcao == "1":
            valor = input("\nDigite o valor que deseja procurar no conjunto: ")
            print(Pertence(valor, conjuntoBase))
        if opcao == "2":
            valor = input("\nDigite o valor que deseja procurar no conjunto: ")
            print(Pertence(valor, conjuntoComparativo))
    elif valorMenu == 2:
        print("************************************")
        opcao = input("1 - B C A:\n2 - A C B: ")
        if opcao == "1":
            print(ContidoOuIgual(conjuntoComparativo, conjuntoBase))
        if opcao == "2":
            print(ContidoOuIgual(conjuntoBase,conjuntoComparativo))
    elif valorMenu == 3:
        print("************************************")
        opcao = input("1 - B C A:\n2 - A C B: ")
        if opcao == "1":
            print(ContidoOuIgual(conjuntoComparativo, conjuntoBase))
        if opcao == "2":
            print(ContidoOuIgual(conjuntoBase,conjuntoComparativo))
    elif valorMenu == 4:
        print("************************************")
        opcao = input("1 - A U B:\n2 - B U A: ")
        if opcao == "1":
            print("\n\nUnião:",Uniao(conjuntoComparativo,conjuntoBase))
        if opcao == "2":
            print("\n\nUnião:",Uniao(conjuntoBase,conjuntoComparativo))
    elif valorMenu == 5:
        print("\n\nInterseção:",Intersecao(conjuntoComparativo, conjuntoBase))
    elif valorMenu == 6:
        print("************************************")
        opcao = input("1 - (AxB)\n2 - (BxA) ")
        if opcao == "1":
            print("\n\nProduto Cartesiano:",ProdutoCartesiano(conjuntoComparativo,conjuntoBase))
        elif opcao == "2":
            print("\n\nProduto Cartesiano:",ProdutoCartesiano(conjuntoBase,conjuntoComparativo))
    elif valorMenu == 7:
        print("************************************")
        opcao = input("1 - (A - B)\n2 - (B - A) ")
        if opcao == "1":
            print("\n\nDiferença de conjunto:",DiferencaDeConjuntos(conjuntoComparativo,conjuntoBase))
        elif opcao == "2":
            print("\n\nDiferença de conjunto:",DiferencaDeConjuntos(conjuntoBase,conjuntoComparativo))
    elif valorMenu == 8:
        print("************************************")
        opcao = input("1 - Elementos de A:\n2 - Elementos de B: ")
        if opcao == "1":
            print("\n\nElementos",Elementos(conjuntoBase))
        elif opcao == "2":
            print("\n\nElementos:",Elementos(conjuntoComparativo))
    elif valorMenu == 9:
        print("************************************")
        opcao = input("1 - Conjunto das partes de A:\n2 - Conjunto das partes de B: ")
        if opcao == "1":
            print("\n\nElementos",Elementos(conjuntoBase))
            print("\n\nConjunto das partes de A:",ConjuntoPartes(conjuntoBase))
        if opcao == "2":
            print("\n\nElementos",Elementos(conjuntoComparativo))
            print("\n\nConjunto das partes de B:",ConjuntoPartes(conjuntoComparativo))

Menu(textoArquivo2, textoArquivo)
contador = 0
while contador < 45:
    resposta = input("\n\nDeseja fazer uma nova operação? (S/N) ")
    if resposta.lower() == "s":
        Menu(textoArquivo2,textoArquivo)
        contador += 1
    else:
        input("\n\nPressione enter para finalizar.\n\n")
        break