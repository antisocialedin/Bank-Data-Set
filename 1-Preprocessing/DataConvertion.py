import pandas as pd

# from sklearn.preprocessing import MinMaxScaler

def main():
  input_file = '0-Datasets/bankClear.csv'
  output_file = '../0-Datasets/bankConvert.csv'
  names = ['age','job','marital','education','default','balance','housing','loan','contact','day','month','duration','campaign','pdays','previous','poutcome','y'] 
  
  df = pd.read_csv(input_file,          # Nome do arquivo com dados
                     names = names,       # Nome das colunas 
                     na_values='unknown')
  print(df.head(10))

  #identify all categorical variables
  cat_columns = df.select_dtypes(['object']).columns
  print (cat_columns)
  #convert all categorical variables to numeric
  df[cat_columns] = df[cat_columns].apply(lambda x: pd.factorize(x)[0])
  print(df.head(10))
  
"""   #Discretização -> simbolos numéricos para números
  df = df.apply(lambda x: pd.factorize(x, sort=True)[0])
  
  #Normalização Min-Max
  x = df.loc[:, features].values
  x_minmax = MinMaxScaler().fit_transform(x)
  normalizedDf = pd.DataFrame(data=x_minmax, columns=features)
  normalizedDf = pd.concat([normalizedDf, df[[target]]], axis=1)
  print(normalizedDf.info())
  print(normalizedDf.describe())
  print(normalizedDf.head(15))

  normalizedDf.to_csv(output_file, header=False, index=False) """

if __name__ == "__main__":
  main()

