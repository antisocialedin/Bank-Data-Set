# Importing
import sklearn
from sklearn.datasets import load_boston
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
# Load the dataset
bos_hou = load_boston()
 
# Create the dataframe
column_name = bos_hou.feature_names
df_boston = pd.DataFrame(bos_hou.data)
df_boston.columns = column_name
df_boston.head()

########### 1 Método - detectar com Quartil ###########
# Box Plot
import seaborn as sns
sns.boxplot(df_boston['DIS'])

# Position of the Outlier
print(np.where(df_boston['DIS']>10))


########### 2 Método - Using ScatterPlot ###########
# Scatter plot
fig, ax = plt.subplots(figsize = (18,10))
ax.scatter(df_boston['INDUS'], df_boston['TAX'])
 
# x-axis label
ax.set_xlabel('(Proportion non-retail business acres)/(town)')
 
# y-axis label
ax.set_ylabel('(Full-value property-tax rate)/( $10,000)')
plt.show()

# Position of the Outlier
print(np.where((df_boston['INDUS']>20) & (df_boston['TAX']>600)))

########### 3 Método - Using Z-Score ###########
# Z score
from scipy import stats
import numpy as np
 
z = np.abs(stats.zscore(df_boston['DIS']))
print(z)

threshold = 3
 
# Position of the outlier
print(np.where(z > 3))

########### 4 Método - IQR (Inter Quartile Range) ###########
# IQR
Q1 = np.percentile(df_boston['DIS'], 25,
                   interpolation = 'midpoint')
 
Q3 = np.percentile(df_boston['DIS'], 75,
                   interpolation = 'midpoint')
IQR = Q3 - Q1

# Above Upper bound
upper = df_boston['DIS'] >= (Q3+1.5*IQR)
 
print("Upper bound:",upper)
print(np.where(upper))
 
# Below Lower bound
lower = df_boston['DIS'] <= (Q1-1.5*IQR)
print("Lower bound:", lower)
print(np.where(lower))