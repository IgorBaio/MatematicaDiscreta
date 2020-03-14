
nomeArquivo = "texto"
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

simbolos = {"=","{","}",",","\n","_"}
simboloSinal = {"-","+"}
print("\n\n",nomeConjunto)
teste = {textoArquivo}
print("\n\n",teste)

'''
def PercorreNomeConjunto(nomeConjunto):
    for letraMaiuscula in nomeConjunto:
       return letraMaiuscula
'''


conjuntos = []
def PercorreConjunto(textoArquivo):
   # a=""
    conjuntoAux = []
    for conjunto in textoArquivo:
        letraConjunto =nomeConjunto.intersection(conjunto)
        if not nomeConjunto.intersection(conjunto):
           if conjunto == "}":
                print("Número de elementos do conjunto",conjuntoAux, "é:" ,conjuntos.__len__())
                listaDeConjuntos.append(conjuntos)
                if conjunto == "_":
                    print("Número de conjuntos é:", listaDeConjuntos.__len__())
                    break 
                continue
           elif conjunto != " " and not simbolos.intersection(conjunto):
               conjuntos.append(conjunto)
           '''elif simboloSinal.intersection(conjunto):
               a += conjunto
               if not simboloSinal.intersection(a):
                   conjuntos.append(a)'''
        else:
            
            if not conjuntos.__contains__(letraConjunto):
              conjuntoAux.append(letraConjunto)
              


PercorreConjunto(textoArquivo)
        
print("\n\nConjuntos:",conjuntos)
print("\n\nLista de conjuntos:",listaDeConjuntos,"\n\n\n")


'''        
def Pertence():
    
def ContidoOuIgual():
    
def ContidoPropriamente():

def Uniao():

def Intersecao():

def ProdutoCartesiano():

def ConjuntoDasPartes():
    
def DiferençaDeConjuntos():

'''
        
        