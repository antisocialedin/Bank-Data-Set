import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
        input_file = '../0-Datasets/bankNormal.csv'
        names = ['age']
        df = pd.read_csv(input_file, 
                        names=names, 
                        na_values='?')

        #df = df.apply(lambda x: pd.factorize(x, sort=True)[0])

        #df.sort_values(ascending=True)
        df.sort_values(by=['age']) 

        at = df.max() - df.min()

        # Lembrando que k = raiz quadrada do total de registros/amostras
        k = math.sqrt(len(df))
        # O valor de amplitude de classe pode ser arredondado para um número inteiro, geralmente para facilitar a interpretação da tabela.
        h = at/k 
        h = math.ceil(h)

        frequencias = []

        # Menor valor da série
        menor = round(df.min(),1)

        # Menor valor somado a amplitude
       # menor_amp = round(menor+h,1)

        valor = menor
        while valor < df.max():
                frequencias.append('{} - {}'.format(round(valor,1),round(valor+h,1)))
                valor += h

        freq_abs = pd.qcut(df,len(frequencias),labels=frequencias) # Discretização dos valores em k faixas, rotuladas pela lista criada anteriormente
        print(pd.value_counts(freq_abs))

        """ # Distribuição de frequência de cap-shape
        cap_shape = df['age']
        labels = ['bell','conical','flat','sunken','knobbed','convex']
        sizes, x = np.histogram(cap_shape, bins=np.arange(7))
        plt.pie(sizes, labels=labels)
        plt.show() 

        # Distribuição de frequência de odor
        odor = df['odor']
        labels =  ['almond','creosote','foul','anise','musty','none','pungent','spicy','fishy']
        sizes, x = np.histogram(odor, bins=np.arange(10))
        plt.bar(np.arange(9), height=sizes, tick_label=labels)
        plt.show()  """

        #Distribuição de frequência de y
        y = df['age']
        labels =  ['age']
        sizes, x = np.histogram(y, bins=np.arange(11))
        plt.bar(np.arange(10), height=sizes, tick_label=labels)
        plt.show()

if __name__ == "__main__":
        main()