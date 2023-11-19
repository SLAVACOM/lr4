from pandas import *


count_vertex = int(input("Введите кол-во вершин: "))
count = int(input("Введите кол-во дорог: "))
graph = [[0 for i in range(count_vertex)] for j in range(count_vertex)]
for i in range(count):
    a, b = map(int, input().split())
    graph[a][b] = -1
    graph[b][a] = 1

print()
print(DataFrame(graph))
print("\n-1 означает что из пункта i исходит дорога в j пункт")
print("1 означает что из пункта i приходит дорога в j пункт\n")

rez_a = [i for i in range(count_vertex) if graph[i].count(-1) > 2]
rez_b = [i for i in range(count_vertex) if graph[i].count(1) == 0]
rez_c = []
rez_d = [i for i in range(count_vertex) if graph[i].count(-1) ==1]

for i in range(count_vertex):
    r = []
    for j in range(count_vertex):
        if graph[i][j] == 1:
            r.append(j)
    rez_c.append(r)

print("а) Номера вершин, имеющих более двух преемников:", *rez_a)
print("б) Номера вершин, не имеющих предшественников:", *rez_b)
print("в)")
for i in range(count_vertex):
    if len(rez_c[i]) > 0:
        print(f"    Номера всех предшественников вершины №{i}:", *rez_c[i])
    else:
        print(f"    Вершина №{i} не имеет предшественников")
print("г) Номера вершин, имеющие ровно одного преемника:", *rez_d)
