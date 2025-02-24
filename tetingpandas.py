import pandas as pd
print(pd.__version__)

series_obj = pd.Series([1,7,9,13,17,99])
print(f'{series_obj}\n')

series_objeto2 = pd.Series ([4,7,8,-2], index = ['alfa','beta','teta','gama'])
print(f'{series_objeto2}\n')

disciplinas = {'Cursos': ['Estadística','Economía','Cálculo','Geometría'],'Créditos':[90,60,90,40],'Requisitos':[True, False,True,False]}

data = pd.DataFrame(disciplinas)
print(f'{data}\n')

nome_cidade = pd.Series(['Maringá', 'Itabira','Uberlándia'])
populacao = pd.Series([403.063,120.904,699.097])

poblacion = pd.DataFrame({'Cuidad': nome_cidade, 'Población': populacao})
print(f'{poblacion}\n')
