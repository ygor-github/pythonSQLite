import  pandas as pd

Author = ["Sun Tzu", "Fernando Pessoa", "Thomas Mann", "Joao Guimaraes Rosa"]
Book = ["A Arte da Guerra", "Poesias Seleccionadas", "A montanha Mágica", "Primeiras Estórias"]
Year = [2000, 2004, 2015, 2017]

database = {
    "Author":Author,
    "Book":Book,
    "Year":Year
}

authors = pd.DataFrame(database)
print(authors, "\n", type(authors))

df = pd.DataFrame(authors)
#print(df)

#Creating a Csv File
df.to_csv("authors.csv")

#Adding Index Argument
authors = pd.read_csv('authors.csv', index_col=0)
#Show indexs
authors.head()

#Getting Information about de file
authors.info()

#Getting Columns
print(authors.columns)
#Getting Index
print(authors.index)


file_path = '/content/sample_data/california_housing_train.csv'
df = pd.read_csv(file_path)
print(df.head())

ado