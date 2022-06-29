from math import ceil
from tracemalloc import stop
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def main():
    # Faz a leitura do arquivo
    input_file = '0-Datasets/bankConvert.csv'
    names = ['age','job','marital','education','default','balance','housing','loan','y']
    features = ['age','job','marital','education','default','balance','housing','loan']
    target = 'y'
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                    usecols = features,
                     names = names) # Nome das colunas                   

    ############################################################ Distribuição de Frequencia Marital ##############################################################################
    #Atributo marital 
    df_marital = (df['marital'])
    array_marital = df_marital.tolist()
    #print(array_marital)
    print(df_marital)
    
    #Job Mínima e Máxima 
    marital_min = int(df.min()[['marital']])
    print(marital_min)
    marital_max = int(df.max()[['marital']])
    print(marital_max)

    #Definir o número de classess
    number_classes =  3

    #Calcular a amplitude de classe
    range = ceil((marital_max - marital_min)/number_classes)
    print ("range de teste", range)

    #Definir os limites inferiores e superiores das classes
    frequencias = []
    valor = marital_min
    while valor < marital_max:
        frequencias.append('{} - {}'.format(round(valor,1),round(valor+range,1)))
        valor += range

    print('frequencias', frequencias)

    #Rotular os valores dos atributos de acordo com sua classe
    freq_abs = pd.cut(df_marital, bins=[0,1,2]) # Discretização dos valores em k faixas, rotuladas pela lista criada anteriormente
    print("teste frenquencia abs", freq_abs)

    #quantidade de atributos idade que tem em cada classe
    qtd_atr = pd.value_counts(freq_abs) 
    print('Quantidade de atributos em cada classe\n', qtd_atr)

    #Histograma do atributo idade
    bin = []
    for number in frequencias:
        bin.append(int(number[0:1]))

    last_range = frequencias.pop()

    #bin.append(int(last_range[5:7]))

    label = ['Casado(a)','Solteiro(a)','Divorciado(a) ou Viúvo(a)']
    #cores = ['r','b','g']
    emp0 = df['marital'].value_counts()[0]
    emp1 = df['marital'].value_counts()[1]
    emp2 = df['marital'].value_counts()[2]
    total = emp0 + emp1 + emp2
    y = np.array([emp0,emp1,emp2])
    plt.pie(y, labels=label, autopct= lambda x: '{:.0f}'.format(x*y.sum()/100, startangle=90))
    plt.title("Distribuição de Estado Civil")
    plt.savefig('0-Datasets/DataFreqMarital.png', format='png')
    plt.show() 
    print("Total: {}\n".format(total) )
    print("Casado(a): {:.2f}%\n".format((emp0*100)/total))
    print("Solteiro(a): {:.2f}%\n".format((emp1*100)/total))
    print("Divorciado(a) ou Viúvo(a): {:.2f}%\n".format((emp2*100)/total))
    

def ShowInformationDataFrame(df, message=""):
    print(message+"\n")
    print(df.info())
    print(df.describe())
    print(df.head(10))
    print("\n")
    
if __name__ == "__main__":
    main()