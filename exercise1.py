from collections import  deque
lista = [8, 9]
lista.append(10)
print(lista)
lista.append('word')
print(lista)
lista.insert(0,7)
print(lista)
lista = [5,6] + lista
print(lista)
lista1 = deque([1,2,3])
lista1.appendleft(4)
total = (list(lista1) + lista)
print(total)
total_ordering = sorted(total, key=str)
#ordenar con str
print(total_ordering)
total_ordering.remove('word')
print(total_ordering)
new_list = list(map(int, total_ordering))
new_list.sort()
print(new_list)