import pandas as pd
#from sklearn.preprocessing import MinMaxScaler

def main():
  input_file = '../0-Datasets/bankClear.csv'
  output_file = '../0-Datasets/bankConvert.csv'
  names = ['age','job','marital','education','default','balance','housing','loan','contact','day','month','duration','campaign','pdays','previous','poutcome','y'] 
  features = ['age','job','marital','education','default','balance','housing','loan','contact','day','month','duration','campaign','pdays','previous','poutcome','y']
  
  df = pd.read_csv(  input_file,          # Nome do arquivo com dados
                     names = names,       # Nome das colunas 
                     usecols = features,  # Define as colunas que serão utilizadas
                     na_values='unknown')
  print(df.head(10))

  #identify all categorical variables
  cat_columns = df.select_dtypes(['object']).columns
  
  #convert all categorical variables to numeric
  df[cat_columns] = df[cat_columns].apply(lambda x: pd.factorize(x)[0])
  print(df.head(10))

  df.to_csv(output_file, header=False, index=False) 

if __name__ == "__main__":
  main()

