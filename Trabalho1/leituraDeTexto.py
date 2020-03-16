
nomeArquivo = "test"
directory = "C:\\Users\\Igori\\Documents\\Projects\\MatDiscreta\\Trabalho1\\"+nomeArquivo+".txt"

arquivo = open(directory)
textoArquivo = arquivo.read()
print(textoArquivo)

listaDeConjuntos = []
'''
for conjunto in textoArquivo:
    if conjunto == "}":
        print("Número de elementos do conjunto",conjuntos, "é:" ,conjuntos.__len__())
        listaDeConjuntos.append(conjuntos)
        print("Número de conjuntos é:", listaDeConjuntos.__len__())
        break;
    elif conjunto != "," and conjunto != " " and conjunto != "{" and conjunto != re.match(r'(\w)',conjunto):
        conjuntos.append(conjunto)
'''
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

switcher = {
        ",":"",
        "{":"",
        "}":""        
        }

    
def PercorreConjunto(textoArquivo):
       # a=""
    conjuntoAux = []
    i = 0
    print("total de elementos = ", (textoArquivo.count(",")+1))
    print("ELementos: ")
    onlyNumbers = ""
    texto = textoArquivo.replace("}", "")
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

def ContidoOuIgual(conjuntoComparativo,conjuntoBase):
    if conjuntoBase == conjuntoComparativo and set(conjuntoComparativo).issubset(set(conjuntoBase)):
        print("O conjunto compartivo é contido ou igual ao conjunto base")
    elif conjuntoBase == conjuntoComparativo:
        print("O conjunto comparativo é igual ao conjunto base.")
    elif set(conjuntoComparativo).issubset(set(conjuntoBase)):
        print("O conjunto comparativo está contido no conjunto base.")

def ContidoPropriamente(conjuntoComparativo,conjuntoBase):
    if set(conjuntoComparativo).issubset(set(conjuntoBase)):
        print("O conjunto comparativo está contido propriamente no conjunto base.")

def Uniao(conjuntoComparativo,conjuntoBase):
    print()


def Intersecao(conjuntoComparativo,conjuntoBase):
    intersecao = []
    for elementoComparativo in conjuntoComparativo:
        for elementoBase in conjuntoBase:
            if elementoComparativo.__contains__(elementoBase) and not simbolos.intersection(elementoComparativo) and not nomeConjunto.intersection(elementoComparativo):
                intersecao.append(elementoComparativo)
    print(intersecao)  



'''        


def ProdutoCartesiano():
    
def ConjuntoDasPartes():
    
def DiferençaDeConjuntos():
    
'''

'''
def PercorreNomeConjunto(nomeConjunto):
    for letraMaiuscula in nomeConjunto:
           return letraMaiuscula
'''

def Menu(conjuntoComparativo, conjuntoBase):
    print("**************************************\n")
    print("OPERAÇÕES:\n")
    print("0 - Percorre\n")
    print("1 - Pertence\n")
    print("2 - Não pertence\n")
    print("3 - Contido ou igual \n")
    print("4 - Não contido ou igual\n")
    print("5 - Contido propriamente\n")
    print("6 - Não contido propriamente\n")
    print("7 - União\n")
    print("8 - Interseção\n")
    print("9 - Produto Cartesiano\n")
    print("10 - Conjunto das partes\n")
    print("11 - Diferença de conjuntos\n")
    print("**************************************\n")

    valorMenu = int(input("Digite o valor correspondente a operação desejada: "))

    if valorMenu == 0:
        PercorreConjunto(textoArquivo)
    elif valorMenu == 1:
        Pertence("1", textoArquivo)
    elif valorMenu == 2:
        Pertence("2", textoArquivo)
    elif valorMenu == 3:
        ContidoOuIgual(conjuntoComparativo, textoArquivo)
    elif valorMenu == 4:
        ContidoOuIgual(conjuntoComparativo2, textoArquivo)
'''
    elif valorMenu == 5:

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


    
    
    
        
        