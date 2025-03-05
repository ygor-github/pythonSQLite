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
print(df)

#Creating a Csv File
df.to_csv("authors.csv")
