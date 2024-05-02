from time import perf_counter

searchTree = {
    'Arad': ['Zerind','Sibiu', 'Timisoara'],
    'Zerind': ['Ordea'],
    'Ordea': ['Sibiu'],
    'Timisoara': ['Lugoj'],
    'Lugoj': ['Mehadia'],
    'Mehadia': ['Drobeta'],
    'Drobeta': ['Craiova'],
    'Craiova': ['Rimmnicu Vicea'],
    'Sibiu': ['Fagaras','Rimnicu Vicea'],
    'Fagaras': ['Bucharest'],
    'Rimnicu Vicea': ['Piesti', 'Craiova'],
    'Piesti': ['Craiova', 'Bucharest'],
    'Bucharest': ['Giurgiu', 'Urziceni'],
    'Giurgiu': [],
    'Urziceni': ['Hirsova', 'Vaslui'],
    'Hirsova': ['Eforie'],
    'Eforie': [],
    'Vaslui': ['Iasi'],
    'Iasi': ['Neamt'],
    'Neamt': []
}

visited = []
queue = []

def bfs(tree = {} , start = str, destination = str):
    '''
    The Breadth First Search model is a little abstract and not entirely useful for a route guidance problem,
    Remember that it ignores cost (i.e. distance) and opens up whole layers at a time, resulting in some illogical looking
    paths.
    Whilst the display reads Arad --> Zerid ---->Sibiu (skipping Oradea), it is not skipping Oradea it is the algorithm expanding
    the 'Arad' layer and exploring its contents and then sequentially moving down to the 'Zerind' layer, exploring it and so on until 
    the target is found.

    Breadth first searches are good for exhaustive searches on small datasets in a 'is it even here' approach.
    For anything large, you would want Depth First Search.
    To do any kind of route guidance, you would want a cost function.
    
    '''

    #A timer is used to compare different search algorithms
    t1 = perf_counter()

    if start == destination:
        Exception("Start destination cannot be the same as Final destination")
    elif start not in tree:
        Exception("Start destination must exist in the Tree")
    
    path = set()
    path.add(start)
    queue.append(start)
    visited.append(start)

    while queue:
        node = queue.pop(0)
        print (node,' --> ', end=" ")
        
        for item in tree[node]:
            path.add(item)
            if item == destination:
                t2 = perf_counter()
                return round((t2-t1)*1000,2)
            if item not in visited:
                visited.append(item)
                queue.append(item)
    return path 



print(bfs(searchTree,'Arad', 'Bucharest'))


