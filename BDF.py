import numpy as np


def findNear(need_find, data):
    pos_point_near = []
    for i in range(len(data[0])):
        if(data[need_find][i]==1):
            pos_point_near.append(i)
    return pos_point_near


def BFS(data, start):
    result = []
    list_BFS = []   
    list_BFS.append(start)
    while(len(list_BFS)!=0):
        pos_point_near = findNear(list_BFS[0], data)
        result.append(list_BFS[0])
        list_BFS.pop(0)
        list_BFS += pos_point_near
    return result



# change A B C to number start 0
# if A can go to B data of col A row B is 1
# else is 0

       # A  B  C  D  E  F  G  H  I  J  K  L  M  N  O
data = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # A
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], # B
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], # C
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0], # D
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # E
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0], # F
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # G
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], # H
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # I
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # J
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # K
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # L
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # M
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # N
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # O
        ]



result = BFS(data, 0)
print(result)