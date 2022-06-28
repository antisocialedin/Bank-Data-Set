from math import ceil
from tracemalloc import stop
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from names import names, features
plt.style.use('ggplot')

def main():
    input_file = '0-Datasets/BankConvert.csv'
    df = pd.read_csv(input_file, names = names)                    

    ############################################################ Distribuição de Frequencia Idade ##############################################################################
    #Atributo idade 
    df_age = (df['age'])
    array_age = df_age.tolist()
    #print(array_age)
    print(df_age)
    
    #Idade Mínima e Máxima 
    age_min = int(df.min()[['age']])
    print(age_min)
    age_max = int(df.max()[['age']])
    print(age_max)

    #Definir o número de classess
    number_classes =  6

    #Calcular a amplitude de classe
    range = ceil((age_max - age_min)/number_classes)
    print ("range de teste", range)

    #Definir os limites inferiores e superiores das classes
    frequencias = []
    valor = age_min
    while valor < age_max:
        frequencias.append('{} - {}'.format(round(valor,1),round(valor+range,1)))
        valor += range

    print('frequencias', frequencias)

    #Rotular os valores dos atributos de acordo com sua classe
    freq_abs = pd.cut(df_age, bins=[18,31,44,57,70,83]) # Discretização dos valores em k faixas, rotuladas pela lista criada anteriormente
    print("teste frenquencia abs", freq_abs)

    #quantidade de atributos idade que tem em cada classe
    qtd_atr = pd.value_counts(freq_abs) 
    print('Quantidade de atributos em cada classe\n', qtd_atr)

    #Histograma do atributo idade
    bin = []
    for number in frequencias:
        bin.append(int(number[0:3]))

    last_range = frequencias.pop()

    bin.append(int(last_range[5:7]))
 
    plt.xlabel("Idade")
    plt.ylabel("Quantidade de Amostras")
    plt.title("Distribuição de idade")
    #plt.xlim(35, 89)
    plt.xticks(bin)
    plt.hist(array_age, bins=bin, edgecolor='black')
    plt.savefig('0-Datasets/DataFreqAge.png', format='png')
    plt.show()

def ShowInformationDataFrame(df, message=""):
    print(message+"\n")
    print(df.info())
    print(df.describe())
    print(df.head(10))
    print("\n")
    
if __name__ == "__main__":
    main()