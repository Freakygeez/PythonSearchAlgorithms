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
#Path cost is seperated out into its own dictionary as it becomes much easier to reference
pathCost = {
    'Arad': [75, 140, 118],
    'Zerind': [71],
    'Ordea': [151],
    'Timisoara': [111],
    'Lugoj': [70],
    'Mehadia': [75],
    'Drobeta': [120],
    'Craiova': [146],
    'Sibiu': [99, 80],
    'Fagaras': [211],
    'Rimnicu Vicea': [97, 146],
    'Piesti': [138, 101],
    'Bucharest': [90, 142],
    'Giurgiu': [],
    'Urziceni': [98, 142],
    'Hirsova': [86],
    'Eforie': [],
    'Vaslui': [92],
    'Iasi': [87],
    'Neamt': []
}

queue = []
costQueue = []


#print(pathCost['Arad'][0])


def A_Star_Search(tree, cost, start, destination):

    total_path_cost = 0 
    path = []

    if start == destination:
        Exception ("Start is the the same as destination")
    elif start or destination not in tree:
        Exception ("start or destination does not exist in the searchTree")
    
    while queue:
        node = queue.pop(-1)
        nodeCost = costQueue.pop(-1)

        if item == destination:
            return (path, total_path_cost)
        
        for item in tree:
            item = node
            if node not in path or cost[nodeCost][0] < costQueue[-1]:
                path.append(item)
                queue.append(item)
                costQueue.append(item)
                total_path_cost += cost[nodeCost[0]]
    
    return Exception ("No path could be found")



print(A_Star_Search(searchTree,pathCost,'Arad','Bucharest'))






