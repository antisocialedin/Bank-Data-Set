import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
# %matplotlib notebook

def main():    
    # Faz a leitura do arquivo
    input_file = '../0-Datasets/bankNormal.csv'
    names = ['age','job','marital','education','default','balance','housing','loan','duration','previous','poutcome','y']
    features = ['age','job','marital','education','default','balance','housing','loan','duration','previous','poutcome','y']
    target = 'y'
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                    names = names) # Nome das colunas                      
    ShowInformationDataFrame(df,"Dataframe original")
            
    x = df.loc[:, features].values

    y = df.loc[:,[target]].values
    
    y = df.loc[:,1].values

    sc = StandardScaler()

    # Standardizing the features
    x = StandardScaler().fit_transform(x)
    normalizedDf = pd.DataFrame(data = x, columns = features)
    normalizedDf = pd.concat([normalizedDf, df[[target]]], axis = 1)
    ShowInformationDataFrame(normalizedDf,"Dataframe Normalized")

    # PCA projection
    pca = PCA()    
    principalComponents = pca.fit_transform(x)
    print("Explained variance per component:")
    print(pca.explained_variance_ratio_.tolist())
    print("\n\n")

    principalDf = pd.DataFrame(data = principalComponents[:,0:3], 
                               columns = ['principal component 1', 
                                          'principal component 2',
                                          'principal component 3'])
    finalDf = pd.concat([principalDf, df[[target]]], axis = 1)    
    ShowInformationDataFrame(finalDf,"Dataframe PCA")
    
    VisualizePcaProjection(finalDf, target)

    
def ShowInformationDataFrame(df, message=""):
    print(message+"\n")
    print(df.info())
    print(df.describe())
    print(df.head(10))
    print("\n")

def VisualizePcaProjection(finalDf, targetColumn):
    fig = plt.figure(figsize = (8,8))
    ax = fig.add_subplot(1,1,1) 
    ax.set_xlabel('Principal Component 1', fontsize = 15)
    ax.set_ylabel('Principal Component 2', fontsize = 15)
    ax.set_zlabel('Principal Component 3', fontsize = 15)
    ax.set_title('3 component PCA', fontsize = 20)
    targets = [0, 1, ]
    colors = ['r', 'g', 'b']
    for target, color in zip(targets,colors):
        indicesToKeep = finalDf[targetColumn] == target
        ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'],
                   finalDf.loc[indicesToKeep, 'principal component 2'],
                   finalDf.loc[indicesToKeep, 'principal component 3'],
                   c = color, s = 50)
    ax.legend(targets)
    ax.grid()
    plt.show()


if __name__ == "__main__":
    main()