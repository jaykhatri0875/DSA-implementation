# objective
# implement graph from scratch and all basic algorithms
from hashlib import new
    

g = {'a':['d','c'],
     'b':['d'],
     'c':['d'],
     'd':[]
}
def find_path(graph,start,end,path = []):
    path = path + [start]
    if start == end:
        return path
    for node in g.keys():
        if node not in path:
            newpath = find_path(graph,node,end,path)
            if newpath:
                return newpath
    return None

print(find_path(g,'a','d'))