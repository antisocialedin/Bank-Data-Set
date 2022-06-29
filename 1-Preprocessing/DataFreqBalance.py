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
    
    ############################################################ Distribuição de Frequencia Saldo ##############################################################################
    #Atributo saldo 
    df_balance = (df['balance'])
    array_balance = df_balance.tolist()
    #print(array_balance)
    print(df_balance)
    
    #Idade Mínima e Máxima 
    balance_min = int(df.min()[['balance']])
    print(balance_min)
    balance_max = int(df.max()[['balance']])
    print(balance_max)

    #Definir o número de classess
    number_classes =  6

    #Calcular a amplitude de classe
    range = ceil((balance_max - balance_min)/number_classes)
    print ("range de teste", range)

    #Definir os limites inferiores e superiores das classes
    frequencias = []
    valor = balance_min
    while valor < balance_max:
        frequencias.append('{} - {}'.format(round(valor,1),round(valor+range,1)))
        valor += range

    print('frequencias', frequencias)

    #Rotular os valores dos atributos de acordo com sua classe
    freq_abs = pd.cut(df_balance, bins=[-8019, 10339, 28697, 47055, 65413, 83771]) # Discretização dos valores em k faixas, rotuladas pela lista criada anteriormente
    print("teste frenquencia abs", freq_abs)

    #quantidade de atributos idade que tem em cada classe
    qtd_atr = pd.value_counts(freq_abs) 
    print('Quantidade de atributos em cada classe\n', qtd_atr)

    #Histograma do atributo idade
    bin = []
    for number in frequencias:
        bin.append(int(number[0:3]))

    last_range = frequencias.pop()

    #bin.append(int(last_range[5:7]))
 
    plt.xlabel("Saldo")
    plt.ylabel("Quantidade de Amostras")
    plt.title("Distribuição de Saldo")
    #plt.xlim(35, 89)
    plt.xticks(bin)
    plt.hist(array_balance, bins=bin, edgecolor='black')
    plt.savefig('0-Datasets/DataFreqBalance.png', format='png')
    plt.show()
    
def ShowInformationDataFrame(df, message=""):
    print(message+"\n")
    print(df.info())
    print(df.describe())
    print(df.head(10))
    print("\n")
    
if __name__ == "__main__":
    main()