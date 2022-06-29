from matplotlib import pyplot as plt
import numpy as np
from sklearn.model_selection import cross_validate, train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import recall_score
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

    clf = DecisionTreeClassifier(max_leaf_nodes=3)
    clf.fit(X_train, y_train)
    tree.plot_tree(clf)
    plt.show()
    
    predictions = clf.predict(X_test)
    print(predictions)
    
    cv_results = cross_validate(clf, X, y, cv=10)
    sorted(cv_results.keys())
    sorted(cv_results['test_score'])
    print("Cross Validation Decision Tree: {:.2f}%".format(np.mean(cv_results['test_score'])*100))
    
    result = clf.score(X_test, y_test)
    print('Acuraccy:')
    print(result)


if __name__ == "__main__":
    main()