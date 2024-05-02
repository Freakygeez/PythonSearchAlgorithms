from time import perf_counter


searchTree = {
    'Arad': {
        'Zerind': 75,
        'Sibiu': 140, 
        'Timisoara': 118},
    
    'Zerind': {
        'Ordea': 71},

    'Ordea': {
        'Sibiu': 151
              },

    'Timisoara': {
        'Lugoj': 111
        },

    'Lugoj': {
        'Mehadia': 70
        },

    'Mehadia': {
        'Drobeta': 75
                },

    'Drobeta': {
        'Craiova': 120
        },
    'Craiova': {
        'Rimmnicu Vicea': 146 
        },

    'Sibiu': {
        'Fagaras': 99,
        'Rimnicu Vicea': 80},

    'Fagaras': {
        'Bucharest': 211},

    'Rimnicu Vicea': {
        'Piesti': 97, 
        'Craiova': 146},

    'Piesti': {
        'Craiova': 138, 
        'Bucharest': 101},

    'Bucharest': {
        'Giurgiu': 90, 
        'Urziceni': 142},

    'Giurgiu': {},

    'Urziceni': {
        'Hirsova': 98, 
        'Vaslui': 142},

    'Hirsova': {
        'Eforie': 86},

    'Eforie': {},

    'Vaslui': {
        'Iasi': 92},

    'Iasi': {
        'Neamt': 87},

    'Neamt': {}
}

queue = []
cost_queue = []


def A_Star_Search(tree, start, destination):

    total_path_cost = 0 
    path = set()

    if start == destination:
        Exception ("Start is the the same as destination")
    elif start or destination not in tree:
        Exception ("start or destination does not exist in the searchTree")
    
    queue.append(start)
    print(queue)
    path.add(start)

    #Each node may have several nodes, with several distances, attached
    #So, we append the initial here and then again in a general form later
    for distance in searchTree[start]:
        cost_queue.append(searchTree[start][distance])

    while queue:
        node = queue.pop(-1)
        cost = min(cost_queue)
        cost_queue.remove(cost) #removes by value rather than ID, bit slower though
        print (node,' --> ', end=" ")
        
        for item in tree[node]:
            item = node
            path.add(item)
            if item == destination:
                return (path, total_path_cost)
            for distance in tree[item]:
                cost_queue.append(tree[item][distance])
            
            if node not in path:
                path.append(item)
                queue.append(item)
                total_path_cost += cost
    
        return Exception ("No path could be found")
    
    return path



print(A_Star_Search(searchTree,'Arad','Bucharest'))





