# a dataframe is simply a table: a dta structure with rows and columns
#let's create a dataframe
import pandas as pd
import numpy as np

#first we need data
data = [
    ['Nissan','Stanza', 1991,138,4, 'MANUAL', 'sedan', 2000],
    ['Hyundai', 'Sonata', 2017, None, 4, 'AUTOMATIC', 'Sedan', 27150],
    ['Lotus', 'Elise', 2010, 218, 4, 'MANUAL', 'convertible', 54990],
    ['GMC', 'Acadia', 2017, 194, 4, 'AUTOMATIC', '4dr SUV', 34450],
    ['Nissan', 'Frontier', 2017, 261, 6, 'MANUAL', 'Pickup', 32340]    
]

# When creating a DAtaframe we need to know what each column contains

columns = [
    'Make','Model', 'Year', 'Engine HP', 'Engine Cylinders', 'Transmission Type', 'Vehicle_Style', 'MSRP'
]
# Now we are ready to create a DataFrame

df = pd.DataFrame(data, columns = columns)

# the first thing, use of head
df.head(n=2) # : n = number of rows

# data = [  vamos a hacer una lista de diccionarios, otra forma de crear dataframes
#     {
#         "Make" : "Nissan",
#         "Model": "Stanza",
#         "Year" : 1991,
#         "Engine HP" : 138.0,
#         "Engine Cylinders" : 4,
#         "Transmission Type" : "MANUAL",
#         "Vehicle_Style" : "Sedan",
#         "MSRP" : 2000
#     },

#     ... MORE ROWS

# ]

# df = pd,DataFrame(data)  Aquí no especificamos las columnas


# Each column in a DataFrame is a SERIES, a special data structure for containing values of one type. In a way it's similar to one dimensional NumPy Arrays
# We can acces the values of a column in two ways
# Dot notation:
df.Make # df es la variable, y Make es el nombre de la columna
# other way is brackets notation
df['Make']
# if a column name contains spaces or other special characters, then we can use only brackets notation
#the bracket notation is more flexible, we can keep de the name of a column in a variable
col_name = 'Engine HP'
df[col_name]
# if we need to select a subset of colñumns, we use the brackets notation
df[['Make', 'Model', 'MSRP']]

# To add a column to a DataFrame we also use the brackets
df['id'] = ['nis1', 'hyu1', 'lot2', 'gmc1', 'nis2']

# if id exists, then the code overwrites the existing values
# to delete a column
del df['id']

#df.index to obtain info about index
# everything that works to series, also works to indexes
# df.columns

################
#Accesing Rows
# #############

#let's start with iloc, we use it to acces the rows of a DataFrame using their positional numbers
df.iloc[0]

#multiple rows, we use a list of integers numbers
df.iloc[[2,3,0]]

# let's play whit shuffle
idx = np.arange(5) # this creates an array with integers from 0 to 4

#now we can shuffle this array
np.random.seed(2)
np.random.shuffle(idx)

#finally we use this array with iloc to get the rows in shuffled order
df.iloc[idx]

df = df.iloc[idx]

df.iloc[[0,1,2]]

df.loc[[0,1]]

#now let's set the index back to the default
df.reset_index(drop=True)

## Splitting a dataFrame
n_train = 3 ## training
n_val = 1 ## validation
n_test = 1 ## testing

# let's split the DataFrame
df_train = df.iloc[:n_train]  # Select's rows for train data
df_val   = df.iloc[n_train:n_train+n_val] # Selects rows for validation
df_test  = df.iloc[n_train+n_val:]  # for test data

#################
###Operations
#################

# in operations in series, we obtain other serie as a result
# and we dont need to write loops
df['Engine HP'] * 2
# we also can use logical operations
df['Year'] > 2000
# this expression returns a boolean series
(df['Year'] > 2000) & (df['Make'] == 'Nissan') # applied elements

###### Filtering

df[df['Make'] == 'Nissan']

df[(df['Year'] > 2010) & (df['Transmission Type'] == 'AUTOMATIC')]


### string operations
df['Vehicle_Style'].str.lower()

# chain string operations
df['Vehicle_Style'].str.lower().str.replace(' ', '_')

#normalization to the columns
df.columns = df.columns.str.lower().str.replace(' ', '_')

# the next line give us a series with object dtype columns only
df.dtypes[df.dtypes == 'object']

# but we need the each index
df.dtypes[df.dtypes == 'object'].index

# now let's apply the normalization to the data
string_columns = df.dtypes[df.dtypes == 'object'].index
for col in string_columns:
    df[col] = df[col].str.lower().str.replace(' ', '_')

# SUmmarizing operations. OJO QUE ESTAMOS OBTENIENDO LOS DATOS DE LA COLUMNA MSRP
# to compute the average of all values in a column
df.msrp.mean()

#Other methods:
# sum, min, max, std

# we can use DESCRIBE to get all these values at once
df.msrp.describe()

# when we invoke mean on the entire DataFrame, it computes the mean for all columns
df.mean()

# para redondear ceros, usamos round(n):n = cantidad de ceros
df.describe().round(2) 

# to9 see missing values:
df.isnull()

# this is impractical when we have large DataFrames, so use:
df.isnull().sum() # this return a series with the number of missing values per column

# to replace the missing values with some actual values, use:
df.engine_hp.fillna(0)
# ahí cambiamos el único valor NaN, el de engine_hp con un cero

# alternativelky, we can replace it by getting the mean
df.engine_hp.fillna(df.engine_hp.mean())

# to write back the results:
df.engine_hp = df.engine_hp.fillna(df.engine_hp.mean())

##############################3
# Working on DataFrames
#############################

# Sorting
df.sort_values(by='msrp') # this sort from the smallest to the largest MSRP

# if we want the largest values first:
df.sort_values(by='msrp', ascending=False)

# Grouping, let's calculate the average price per transmission type
df.groupby('transmission_type').msrp.mean()

# number of records per each type:
df.groupby('transmission_type').msrp.agg(['mean', 'count'])