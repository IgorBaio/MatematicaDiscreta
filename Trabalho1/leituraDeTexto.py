
nomeArquivo = "test"
directory = "C:\\Users\\Igori\\Documents\\Projects\\MatDiscreta\\Trabalho1\\"+nomeArquivo+".txt"

arquivo = open(directory)
textoArquivo = arquivo.read()
print(textoArquivo)
texto = textoArquivo.replace("}","")
print(texto.split(","))

listaDeConjuntos = []

nomeConjunto = {"A","B","C","D","E","F","I","G","H","I","J","K","L","M","N","O",
                "P","Q","R","S","T","U","V","W","X","Y","Z"}

simbolos = {"=","{","}",",","\n","_", " "}
simboloSinal = {"-","+"}
numeros = {"1","2","3","4","5","6","7","8","9","0"}

print("\n\n",nomeConjunto)
teste = {textoArquivo}
print("\n\n",teste)

conjuntos = []
conjuntoComparativo = "A = {1,87,4,-1,43}"
conjuntoComparativo2 = "{1,87,4,-1,43}"
conjuntoComparativo3 = "{87,0,-1}"


switcher = {
        ",":"",
        "{":"",
        "}":""        
        }

    
def PercorreConjunto(textoArquivo):
    conjuntoAux = []
    i = 0
    j = 0
    print("total de elementos = ", (textoArquivo.count(",")+1))
    print("Elementos: ")
    onlyNumbers = ""
    texto = textoArquivo.replace("{", "")
    texto = texto.replace("}", "")
    texto = texto.split(",")
    #tirar o in e colocar while
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
    '''
    for item in texto.split(","):
        if str.isdigit(item):
            onlyNumbers += item
            conjuntoAux.append(onlyNumbers)
            onlyNumbers = "" 
        else:
            for character in item:
                if str.isdigit(character):
                    onlyNumbers += character
                    conjuntoAux.append(onlyNumbers)
                    onlyNumbers = "" 
                elif character == "-":
                    onlyNumbers = character

            onlyNumbers = "" 
    print(conjuntoAux)
    '''
    '''while i < textoArquivo.__len__():
        #virgula = simbolos.intersection(textoArquivo[i])
        letraConjunto = nomeConjunto.intersection(textoArquivo[i])
        valorDuplo1 = textoArquivo[i+1]
        valorDuplo2 = textoArquivo[i+2]
        if not nomeConjunto.intersection(textoArquivo[i]):
            if textoArquivo[i] == "}":
                print("Número de elementos do conjunto",conjuntoAux, "é:" ,textoArquivo.count(",")+1)
                
                listaDeConjuntos.append(conjuntos)
                #if textoArquivo[i].__eq__("_"):
                 #   print("Número de conjuntos é:", listaDeConjuntos.__len__())
                break 
            elif not simbolos.intersection(textoArquivo[i]):
                conjuntos.append(textoArquivo[i])
            elif switcher.get(simbolos.intersection(textoArquivo[i])):
                if textoArquivo[i+1] == numeros.intersection(textoArquivo[i+1]).__str__() and textoArquivo[i+2] == numeros.intersection(textoArquivo[i+2]).__str__():
                     valorDuplo = textoArquivo[i+1]+textoArquivo[i+2]
                     conjuntoAux.append(valorDuplo)
        ''' '''
            elif simboloSinal.intersection(conjunto):
                a += conjunto
                if not simboloSinal.intersection(a):
                    conjuntos.append(a)'''
            
            #i +=1
          
        #else:
            
        #    if not conjuntos.__contains__(letraConjunto):
        #          conjuntoAux.append(letraConjunto)
        #          i += 1
        
'''
    for conjunto in textoArquivo:
        letraConjunto = nomeConjunto.intersection(conjunto)
        if not nomeConjunto.intersection(conjunto):
            if conjunto == "}":
                print("Número de elementos do conjunto",conjuntoAux, "é:" ,conjuntos.__len__())
                listaDeConjuntos.append(conjuntos)
                if conjunto == "_":
                    print("Número de conjuntos é:", listaDeConjuntos.__len__())
                    break 
                continue
            elif not simbolos.intersection(conjunto):
                conjuntos.append(conjunto)
            #elif simboloSinal.intersection(conjunto):
            #    a += conjunto
            #    if not simboloSinal.intersection(a):
            #        conjuntos.append(a)
        else:
            
            if not conjuntos.__contains__(letraConjunto):
                  conjuntoAux.append(letraConjunto)
   '''           

def Pertence(numero, conjunto):
    if conjunto.__contains__(numero):
        print("O número",numero,"pertence ao conjunto",conjunto)
        
    else:
        print("O número",numero,"não pertence ao conjunto",conjunto)

#a terceira comparação eu acho que equivale ao contido propriamente 
def ContidoOuIgual(conjuntoComparativo,conjuntoBase):
    if conjuntoBase == conjuntoComparativo and set(conjuntoComparativo).issubset(set(conjuntoBase)):
        print("O conjunto comparativo é contido ou igual ao conjunto base")
    elif conjuntoBase == conjuntoComparativo:
        print("O conjunto comparativo é igual ao conjunto base.")
    elif set(conjuntoComparativo).issubset(set(conjuntoBase)) and not conjuntoBase == conjuntoComparativo:
        print("O conjunto comparativo está contido no conjunto base.")

def ContidoPropriamente(conjuntoComparativo,conjuntoBase):
    if set(conjuntoComparativo).issubset(set(conjuntoBase)):
        print("O conjunto comparativo está contido propriamente no conjunto base.")

def formataConjunto(conjunto):
    conjunto = conjunto.replace("[","") 
    conjunto = conjunto.replace("]","")
    conjunto = conjunto.replace("'","")
    conjunto = conjunto.replace(" ","")
    return conjunto

def Uniao(conjuntoComparativo,conjuntoBase):
    conjuntoAuxBase = str(PercorreConjunto(conjuntoBase))
    conjuntoAuxBase = formataConjunto(conjuntoAuxBase)
    conjuntoAuxComparativo = str(PercorreConjunto(conjuntoComparativo))
    conjuntoAuxComparativo = formataConjunto(conjuntoAuxComparativo)   
    print()
    nomeDaUniao = input("Digite a letra do nome do conjunto: ")
    if conjuntoAuxBase == conjuntoAuxComparativo:
        print("Conjunto",nomeDaUniao,"= {",conjuntoAuxBase,"}")
    else:
        print("Conjunto",nomeDaUniao,"= {",conjuntoAuxBase,",",conjuntoAuxComparativo,"}")



def Intersecao(conjuntoComparativo,conjuntoBase):
    intersecao = []
    conjuntoAuxBase = PercorreConjunto(conjuntoBase)
    conjuntoAuxComparativo = PercorreConjunto(conjuntoComparativo)
    i = 0
    while i < conjuntoAuxBase.__len__():
        if conjuntoAuxComparativo.__contains__(conjuntoAuxBase[i]):
            intersecao.append(conjuntoAuxBase[i])
        
        i+=1
    print(intersecao)

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
    
    
'''
    

def ConjuntoDasPartes():
    
def DiferençaDeConjuntos():
'''


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
    print("7 - Conjunto das partes\n")
    print("8 - Diferença de conjuntos\n")
    print("**************************************\n")

    valorMenu = int(input("Digite o valor correspondente a operação desejada: "))

    if valorMenu == 0:
        PercorreConjunto(textoArquivo)
    elif valorMenu == 1:
        Pertence("1", textoArquivo)
        #Pertence("2", textoArquivo)
    elif valorMenu == 2:
        ContidoOuIgual(conjuntoComparativo, textoArquivo)
        #ContidoOuIgual(conjuntoComparativo2, textoArquivo)
    elif valorMenu == 3:#nao sei se esse ta dentro do anterior ou nao, ou se tenho que fazer um a parte
        ContidoOuIgual(conjuntoComparativo2, textoArquivo)
    elif valorMenu == 4:
        Uniao(conjuntoComparativo3,textoArquivo)
    elif valorMenu == 5:
        Intersecao(conjuntoComparativo3, textoArquivo)
    elif valorMenu == 6:
        print(ProdutoCartesiano(conjuntoComparativo3,textoArquivo))
        
'''

    elif valorMenu == 6:

    elif valorMenu == 7:

    elif valorMenu == 8:

    elif valorMenu == 9:

    elif valorMenu == 10:
'''


Menu(conjuntoComparativo, textoArquivo)

'''
PercorreConjunto(textoArquivo)

Pertence("1", textoArquivo)

Pertence("2", textoArquivo)



ContidoOuIgual(conjuntoComparativo2, textoArquivo) 

Intersecao(conjuntoComparativo, textoArquivo)
'''

print("\n\nConjuntos:",conjuntos)
print("\n\nLista de conjuntos:",listaDeConjuntos,"\n\n\n")


    
    
        
        