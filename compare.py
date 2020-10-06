import pandas as pd

def comparacao(a, b):
     if (a == b): 
         return 'a linha E igual' 
     else: 
         return 'a linha NAO e igual'


df = pd.read_csv('arq.csv', ';', header=0, usecols=["Titulo", "titulo"])

countTitulo1 = pd.DataFrame(df).count()[0]
countTitulo2 = pd.DataFrame(df).count()[1]

file = open("resultado_comparacao.txt", "w")
file.write("textoTitulo;resultadoDaComparacao\n")  

string1 = df.iat[0,0]
string2 = df.iat[0,1]


for linha in range(countTitulo1):
    retorno = comparacao(df.iat[linha,0], df.iat[linha,1])
    file.write(df.iat[linha,0] + ";" + retorno + "\n")  

file.close() 
