import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
#import seaborn as sns

def main():

    # Faz a leitura do arquivo
    input_file = '../0-Datasets/bankNormal.csv'
    names = ['age','job','marital','education','default','balance','housing','loan','duration','previous','poutcome','y']
    features = ['age','job','marital','education','default','balance','housing','loan','duration','previous','poutcome','y']
    target = 'y'
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                                names=names)  # Nome das colunas  

    # Get the iris dataset
    """ sns.set_style("white")
    df = sns.load_dataset('../0-Datasets/bankNormal.csv') """

    # create figure
    my_dpi = 96
    plt.figure(figsize=(480/my_dpi, 480/my_dpi), dpi=my_dpi)

    df['y'] = pd.Categorical(df['y'])
    my_color = df['y'].cat.codes
    df = df.drop('y', 1)

    # Run The PCA
    pca = PCA(n_components=3)
    pca.fit(df)

    # Store results of PCA in a data frame
    result = pd.DataFrame(pca.transform(df), columns=[
        'PCA%i' % i for i in range(3)], index=df.index)

    # Plot initialisation
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(result['PCA0'], result['PCA1'],
            result['PCA2'], c=my_color, cmap="Set2_r", s=60)

    # make simple, bare axis lines through space:
    xAxisLine = ((min(result['PCA0']), max(result['PCA0'])), (0, 0), (0, 0))
    #ax.plot(xAxisLine[0], xAxisLine[1], xAxisLine[2], 'r')
    yAxisLine = ((0, 0), (min(result['PCA1']), max(result['PCA1'])), (0, 0))
    #ax.plot(yAxisLine[0], yAxisLine[1], yAxisLine[2], 'g')
    zAxisLine = ((0, 0), (0, 0), (min(result['PCA2']), max(result['PCA2'])))
    #ax.plot(zAxisLine[0], zAxisLine[1], zAxisLine[2], 'b')

    # label the axes
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
    ax.set_zlabel("PC3")
    ax.set_title("PCA Bank Dataset")

    plt.show()


if __name__ == "__main__":
    main()
