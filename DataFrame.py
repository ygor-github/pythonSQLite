import pandas as pd

disciplinas = {'Cursos': ['Estadística','Economía','Cálculo','Geometría'],'Créditos':[90,60,90,40],'Requisitos':[True, False,True,False]}

data = pd.DataFrame(disciplinas)
print(f'{data}\n')

nome_cidade = pd.Series(['Maringá', 'Itabira','Uberlándia'])
populacao = pd.Series([403.063,120.904,699.097])

poblacion = pd.DataFrame({'Cuidad': nome_cidade, 'Población': populacao})
print(f'{poblacion}\n')
