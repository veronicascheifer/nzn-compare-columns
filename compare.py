import pandas as pd

def comparison(a, b):
     if (a == b): 
         return 'the row is equal' 
     else: 
         return 'the row is not equal'


df = pd.read_csv('file.csv', ';', header=0, usecols=["Title", "title"])

countTitle1 = pd.DataFrame(df).count()[0]
countTitle2 = pd.DataFrame(df).count()[1]

file = open("comparison_results.txt", "w")
file.write("textTitle;comparisonResults\n")  

string1 = df.iat[0,0]
string2 = df.iat[0,1]


for line in range(countTitle1):
    return1 = comparison(df.iat[line,0], df.iat[line,1])
    file.write(df.iat[line,0] + ";" + return1 + "\n")  

file.close() 
