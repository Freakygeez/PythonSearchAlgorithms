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

queue = []

def dfs(tree = {} , start = str, destination = str):
    '''
    The Depth First Search model, much like BFS, is a little abstract and not entirely useful for a route guidance problem,
    Remember that it ignores cost (i.e. distance) and works by following one branch to the leaf at a time
    
    Depth first searches are good for exhaustive searches on very large datasets as they require much less memory, at the cost of time.
    
    CAUTION: DFS algorithms are prone to getting stuck or erroring on loops, which is why this algorithm errors on 'Rimmnicu Vicea'
    
    '''

    #A timer is used to compare different search algorithms
    t1 = perf_counter()

    if start == destination:
        Exception("Start destination cannot be the same as Final destination")
    elif start not in tree:
        Exception("Start destination must exist in the Tree")
    
    queue.append(start)

    while queue:
        node = queue.pop(-1)
        print (node,' --> ', end=" ")
        
        for item in tree[node]:
            if item == destination:
                t2 = perf_counter()
                return round((t2-t1)*1000,2)
            else: 
                queue.append(item)



print(dfs(searchTree,'Arad', 'Bucharest'))


