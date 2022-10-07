import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def main():
    # Faz a leitura do arquivo
    input_file = '0-Datasets/bankConvert.csv'
    names = ['age','job','marital','education','default','balance','housing','loan','y']
    features = ['age','job','marital','education','default','balance','housing','loan']
    target = 'y'
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                     names = names) # Nome das colunas                                     
    #ShowInformationDataFrame(df,"Dataframe original")

"""     # Separating out the features
    x = df.loc[:, features].values

    # Separating out the target
    y = df.loc[:,[target]].values """

    # Separate X and y data
    X = df.drop('y', axis=1)
    y = df['y']

    # Standardizing the features (Z-Score normalization)
    x = StandardScaler().fit_transform(x)
    normalizedDf = pd.DataFrame(data = x, columns = features)
    normalizedDf = pd.concat([normalizedDf, df[[target]]], axis = 1)
    #ShowInformationDataFrame(normalizedDf,"Dataframe Z-Score Normalized")

    # create figure
    my_dpi=96
    plt.figure(figsize=(480/my_dpi, 480/my_dpi), dpi=my_dpi)

    df['wages']=pd.Categorical(df['wages'])
    my_color=df['wages'].cat.codes
    df = df.drop('wages', 1) 

    # Run The PCA
    pca = PCA(n_components=2)
    pca.fit(df)
    
    # Store results of PCA in a data frame
    result=pd.DataFrame(pca.transform(df), columns=['PCA%i' % i for i in range(3)], index=df.index)
    
    # Plot initialisation
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(result['PCA0'], result['PCA1'], result['PCA2'], c=my_color, cmap="Set2_r", s=60)
    
    # make simple, bare axis lines through space:
    xAxisLine = ((min(result['PCA0']), max(result['PCA0'])), (0, 0), (0,0))
    ax.plot(xAxisLine[0], xAxisLine[1], xAxisLine[2], 'r')
    yAxisLine = ((0, 0), (min(result['PCA1']), max(result['PCA1'])), (0,0))
    ax.plot(yAxisLine[0], yAxisLine[1], yAxisLine[2], 'r')
    zAxisLine = ((0, 0), (0,0), (min(result['PCA2']), max(result['PCA2'])))
    ax.plot(zAxisLine[0], zAxisLine[1], zAxisLine[2], 'r')
    
    # label the axes
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
    ax.set_zlabel("PC3")
    ax.set_title("PCA on the iris data set")
    plt.show()