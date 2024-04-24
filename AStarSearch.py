from time import perf_counter
searchTree = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Ordea':71},
    'Ordea': {'Sibiu': 151},
    'Timisoara': {'Lugoj': 111},
    'Lugoj': {'Mehadia': 70},
    'Mehadia': {'Drobeta': 75},
    'Drobeta': {'Craiova': 120},
    'Craiova': {'Rimmnicu Vicea': 146},
    'Sibiu': {'Fagaras': 99, 'Rimnicu Vicea': 80},
    'Fagaras': {'Bucharest': 211},
    'Rimnicu Vicea': {'Piesti': 97, 'Craiova': 146},
    'Piesti': {'Craiova':138, 'Bucharest':101},
    'Bucharest': {'Giurgiu': 90, 'Urziceni': 142},
    'Giurgiu': {},
    'Urziceni': {'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Eforie': 86},
    'Eforie': {},
    'Vaslui': {'Iasi': 92},
    'Iasi': {'Neamt': 87},
    'Neamt': {}

}

visited = []
queue = []




bfs(visited,searchTree,'START')
#result:
#START 1 2 3 4 5 6 7 8 9 10 11 12 13 14 FINISH
