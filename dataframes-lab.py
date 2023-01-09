# let us import the Pandas Library
import pandas as pd

#Define a dictionary 'x'

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
print(df)

#Retrieving the "ID" column and assigning it to a variable x
x = df[['ID']]
print(type(x))

#Retrieving the Department, Salary and ID columns and assigning it to a variable z

z = df[['Department','Salary','ID']]
print(z)

# Access the value on the first row and the third column

df.iloc[0,2]

# Access the column using the name

print(df.loc[0, 'Salary'])

df2=df
df2=df2.set_index("Name")

#Now, let us access the column using the name
df2.loc['Jane', 'Salary']

#let us do the slicing using loc() function on old dataframe df where index column is having labels as 0,1,2
df.loc[0:2,'ID':'Department']

##########################################################################

# Read data from CSV file

csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)

# Print first five rows of the dataframe

print("\n\n\n\n\n\n\n",df.head())

# Read data from Excel File and print the first five rows

xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'

df = pd.read_excel(xlsx_path)
print("\n\n\n\n\n\n",df.head())


# Access to the column Length

x = df[['Length']]
print(x)


# Access to multiple columns

y = df[['Artist','Length','Genre']]
print(y)