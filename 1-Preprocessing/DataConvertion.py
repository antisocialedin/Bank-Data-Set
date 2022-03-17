import pandas as pd

from sklearn.preprocessing import MinMaxScaler

def main():
  input_file = '../0-Datasets/bankClear.csv'
  output_file = '../0-Datasets/bankConvert.csv'
  names = ['age','job','marital','education','default','balance','housing','loan','contact','day','month','duration','campaign','pdays','previous','poutcome','y'] 
  target = names[0]
  features = names[1:]
  
  df = pd.read_csv(input_file, names=names, na_values='unknown')

  #Discretização -> simbolos numéricos para números
  df = df.apply(lambda x: pd.factorize(x, sort=True)[0])
  
  #Normalização Min-Max
  x = df.loc[:, features].values
  x_minmax = MinMaxScaler().fit_transform(x)
  normalizedDf = pd.DataFrame(data=x_minmax, columns=features)
  normalizedDf = pd.concat([normalizedDf, df[[target]]], axis=1)
  print(normalizedDf.info())
  print(normalizedDf.describe())
  print(normalizedDf.head(15))

  normalizedDf.to_csv(output_file, header=False, index=False)

if __name__ == "__main__":
  main()

