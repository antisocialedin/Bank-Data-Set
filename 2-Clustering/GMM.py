#Implementation of Kmeans from scratch and using sklearn
#Loading the required modules 
import numpy as np
import pandas as pd 
from scipy.spatial.distance import cdist 
from sklearn.decomposition import PCA
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
from sklearn.metrics import silhouette_samples
import matplotlib.pyplot as plt

def show_digitsdataset(digits):
    fig = plt.figure(figsize=(6, 6))  # figure size in inches
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

    for i in range(64):
        ax = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
        ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')
        # label the image with the target value
        ax.text(0, 7, str(digits.target[i]))

    #fig.show()

def plot_samples(projected, labels, title):    
    fig = plt.figure()
    u_labels = np.unique(labels)
    for i in u_labels:
        plt.scatter(projected[labels == i , 0] , projected[labels == i , 1] , label = i,
                    edgecolor='none', alpha=0.5, cmap=plt.cm.get_cmap('tab10', 10))
    plt.xlabel('component 1')
    plt.ylabel('component 2')
    plt.legend()
    plt.title(title)

def ShowInformationDataFrame(df, message=""):
    print(message+"\n")
    print(df.info())
    print(df.describe())
    print(df.head(10))
    print("\n")
    
def main():
    # Faz a leitura do arquivo
    input_file = '../0-Datasets/bankNormal(z-score).csv'
    names = ['age','job','marital','education','default','balance','housing','loan','duration','previous','poutcome','y']
    labels = ['age','job','marital','education','default','balance','housing','loan','duration','previous','poutcome']
    target = 'y'
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                     names = names) # Nome das colunas                      
    ShowInformationDataFrame(df,"Dataframe original")

    #Transform the data using PCA
    pca = PCA(2)
    projected = pca.fit_transform(df)
    print(pca.explained_variance_ratio_)
    print(df.shape)
    print(projected.shape)    
    plot_samples(projected, target, 'Original Labels') 
    
    #Applying sklearn GMM function
    gm  = GaussianMixture(n_components=3).fit(projected)
    print(gm.weights_)
    print(gm.means_)
    x = gm.predict(projected)

    #Visualize the results sklearn
    plot_samples(projected, x, 'Clusters Labels GMM')

    plt.show()

if __name__ == "__main__":
    main()