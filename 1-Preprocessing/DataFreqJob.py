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

    ############################################################ Distribuição de Frequencia Job ##############################################################################
    #Atributo job 
    df_job = (df['job'])
    array_job = df_job.tolist()
    #print(array_job)
    print(df_job)
    
    #Job Mínima e Máxima 
    job_min = int(df.min()[['job']])
    print(job_min)
    job_max = int(df.max()[['job']])
    print(job_max)

    #Definir o número de classess
    number_classes =  11

    #Calcular a amplitude de classe
    range = ceil((job_max - job_min)/number_classes)
    print ("range de teste", range)

    #Definir os limites inferiores e superiores das classes
    frequencias = []
    valor = job_min
    while valor < job_max:
        frequencias.append('{} - {}'.format(round(valor,1),round(valor+range,1)))
        valor += range

    print('frequencias', frequencias)

    #Rotular os valores dos atributos de acordo com sua classe
    freq_abs = pd.cut(df_job, bins=[0,1,2,3,4,5,6,7,8,9,10]) # Discretização dos valores em k faixas, rotuladas pela lista criada anteriormente
    print("teste frenquencia abs", freq_abs)

    #quantidade de atributos idade que tem em cada classe
    qtd_atr = pd.value_counts(freq_abs) 
    print('Quantidade de atributos em cada classe\n', qtd_atr)

    #Histograma do atributo idade
    bin = []
    for number in frequencias:
        bin.append(int(number[0:1]))

    last_range = frequencias.pop()

    bin.append(int(last_range[5:7]))

    label = ['Gestão','Técnico','Empresário','Colarinho-Azul','Aposentado','Administrador','Serviços Gerais','Autônomo','Desempregado','Dona de Casa','Estudante']
    #cores = ['r','b','g']
    emp0 = df['job'].value_counts()[0]
    emp1 = df['job'].value_counts()[1]
    emp2 = df['job'].value_counts()[2]
    emp3 = df['job'].value_counts()[3]
    emp4 = df['job'].value_counts()[4]
    emp5 = df['job'].value_counts()[5]
    emp6 = df['job'].value_counts()[6]
    emp7 = df['job'].value_counts()[7]
    emp8 = df['job'].value_counts()[8]
    emp9 = df['job'].value_counts()[9]
    emp10 = df['job'].value_counts()[10]
    total = emp0 + emp1 + emp2 + emp3 + emp4 + emp5 + emp6 + emp7 + emp8 + emp9 + emp10
    y = np.array([emp0,emp1,emp2,emp3,emp4,emp5,emp6,emp7,emp8,emp9,emp10])
    plt.pie(y , labels=label, autopct= lambda x: '{:.0f}'.format(x*y.sum()/100, startangle=90))
    plt.title("Gráfico de Distribuição de Empregos")
    plt.savefig('0-Datasets/DataFreqJob.png', format='png')
    plt.show() 
    print("Total: {}\n".format(total) )
    print("Gestão: {:.2f}%\n".format((emp0*100)/total))
    print("Técnico: {:.2f}%\n".format((emp1*100)/total))
    print("Empresário: {:.2f}%\n".format((emp2*100)/total))
    print("Colarinho-Azul: {:.2f}%\n".format((emp3*100)/total))
    print("Aposentado: {:.2f}%\n".format((emp4*100)/total))
    print("Administrador: {:.2f}%\n".format((emp5*100)/total))
    print("Serviços Gerais: {:.2f}%\n".format((emp6*100)/total))
    print("Autônomo: {:.2f}%\n".format((emp7*100)/total))
    print("Desempregado: {:.2f}%\n".format((emp8*100)/total))
    print("Dona de Casa: {:.2f}%\n".format((emp9*100)/total))
    print("Estudante: {:.2f}%\n".format((emp10*100)/total))
    

def ShowInformationDataFrame(df, message=""):
    print(message+"\n")
    print(df.info())
    print(df.describe())
    print(df.head(10))
    print("\n")
    
if __name__ == "__main__":
    main()