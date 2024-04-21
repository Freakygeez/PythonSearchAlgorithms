from time import perf_counter
searchTree = {
    'START': ['1', '2'],
    '1': ['3','4'],
    '2': ['5', '6'],
    '3': ['7', '8'],
    '4': ['9', '10'],
    '5': ['11', '12'],
    '6': ['13', '14'],
    '7': ['FINISH'],
    '8': [],
    '9': [],
    '10': ['15'],
    '11': [],
    '12': [],
    '13': [],
    '14': ['16'],
    '15': ['FINISH'],
    '16': [],
    'FINISH': []

}

visited = []
queue = []

def bfs(visited = [], graph = {}, startNode = any, goalNode=any):
    visited.append(startNode)
    queue.append(startNode)
    t1 = perf_counter()

    while queue:
        i = queue.pop(0)
        print (i, end=" ")

        for nextNode in graph[i]:
            if nextNode == goalNode:
                return print(visited)
            if nextNode not in visited:
                visited.append(nextNode)
                queue.append(nextNode)
    t2 = perf_counter()
    print ('time taken: ', round((t2-t1)*1000,2), 'ms')



bfs(visited,searchTree,'START')
#result:
#START 1 2 3 4 5 6 7 8 9 10 11 12 13 14 FINISH
