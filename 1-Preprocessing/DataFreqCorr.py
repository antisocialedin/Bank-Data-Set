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
                     names = names) # Nome das colunas

    """ ################### IDADE X SALDO #####################
    plt.subplots(figsize=(10, 5))
    plt.scatter(df['age'],df['balance'])
    plt.xlabel('idade')
    plt.ylabel('saldo')
    plt.title("Idade X Saldo")
    plt.show() """

    ################### EMPREGO X SALDO #####################
    plt.subplots(figsize=(10, 5))
    plt.scatter(df['job'],df['balance'])
    plt.xlabel('Emprego')
    plt.ylabel('Saldo')
    plt.title("Emprego X Saldo")
    plt.show()

    ################### IDADE X EMPRESTIMO RESIDENCIAL #####################
    plt.subplots(figsize=(10, 5))
    plt.scatter(df['housing'],df['age'])
    plt.xlabel('Empréstimo Residencial')
    plt.ylabel('Idade')
    plt.title("Emprestimo Residêncial X Idade")
    plt.show()

    ################### IDADE X EMPRESTIMO #####################
    plt.subplots(figsize=(10, 5))
    plt.scatter(df['loan'],df['age'])
    plt.xlabel('Empréstimo')
    plt.ylabel('Idade')
    plt.title("Empréstimo X Idade")
    plt.show()
    
"""     ################### job X y #####################
    plt.subplots(figsize=(10, 5))
    plt.scatter(df['y'],df['job'])
    plt.xlabel('y')
    plt.ylabel('Emprego')
    plt.title("y X Emprego")
    plt.show() """

if __name__ == "__main__":
    main()