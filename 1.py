from pandas import *

count_vertex = int(input("Введите кол-во вершин: "))
count = int(input("Введите кол-во дорог: "))
graph = [[0 for i in range(count_vertex)] for j in range(count_vertex)]
for i in range(count):
    a, b = map(int, input().split())
    graph[a][b] = 1

print(DataFrame(graph))

rez_a = [i for i in range(count_vertex) if graph[i].count(1) > 2]
rez_b = []
rez_c = []
rez_d = [i for i in range(count_vertex) if graph[i].count(1) == 1]

for i in range(count_vertex):
    r = []
    for j in range(count_vertex):
        if graph[i][j] == 1:
            r.append(j)
    if len(r) == 0: rez_b.append(i)
    rez_c.append(r)

if len(rez_a) > 0:
    print("а) Номера вершин, имеющих более двух преемников:", *rez_a)
else: print("а) Отсутствуют вершины имеющие более двух преемников")

if len(rez_b) > 0:
    print("б) Номера вершин, не имеющих предшественников:", *rez_b)
else:
    print("б) Отсутствуют вершины не имеющие предшественников")

print("в)")
for i in range(count_vertex):
    if len(rez_c[i]) > 0:
        print(f"    Номера всех предшественников вершины №{i}:", *rez_c[i])
    else:
        print(f"    Вершина №{i} не имеет предшественников")
if len(rez_d) > 0:
    print("г) Номера вершин, имеющие ровно одного преемника:", *rez_d)
else:
    print("г) Отсутствуют вершины имеющие ровно одного преемника")