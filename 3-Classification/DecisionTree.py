from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import pandas as pd
from sklearn.preprocessing import StandardScaler

def main():
    
    # Faz a leitura do arquivo
    input_file = '0-Datasets/bankConvert.csv'
    names = ['age','job','marital','education','default','balance','housing','loan','y']
    features = ['age','job','marital','education','default','balance','housing','loan']
    target = 'y'
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                     names = names) # Nome das colunas                      
    #ShowInformationDataFrame(df,"Dataframe original")            
   
    # Separating out the features
    X = df.loc[:, features].values
    print(X.shape)

    # Separating out the target
    y = df.loc[:,[target]].values

    # Standardizing the features
    X = StandardScaler().fit_transform(X)
    normalizedDf = pd.DataFrame(data = X, columns = features)
    normalizedDf = pd.concat([normalizedDf, df[[target]]], axis = 1)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
    print(X_train.shape)
    print(X_test.shape)

    clf = DecisionTreeClassifier(max_leaf_nodes=10)
    clf.fit(X_train, y_train)
    tree.plot_tree(clf)
    plt.show()
    
    predictions = clf.predict(X_test)
    print(predictions)
    
    result = clf.score(X_test, y_test)
    print('Acuraccy:')
    print(result)


if __name__ == "__main__":
    main()