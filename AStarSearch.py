from time import perf_counter
import pandas as pd

queue = []
reached = []

#print(tree['Arad']['connected']['Zerind']['cost'] )

def A_Star_Search(tree=str, penalty=1000, start = str, destination=str):
    
    tree = pd.read_json(tree)
    t1 = perf_counter()
    total_path_cost = 0 
    path = set()
    cost_queue = []

    if start == destination:
        Exception ("Start is the the same as destination")
    elif start or destination not in tree:
        Exception ("start or destination does not exist in the searchTree")
    path.add(start)

    #Load the connecting nodes
    for node in tree[start]['connected']:
        queue.append(node)
        
    print (queue)

    #Load cost queue
    for item in queue:
        cost_queue.append(tree[start]['connected'][item]['cost'])
    
    print(cost_queue)

    '''    
    #for i in tree['Nodes'].loc[(tree[start] < penalty)]:
        queue.append(i)
    for i in tree[start].loc[(tree[start] < penalty)]:
        reached.append(i)
    total_path_cost = 0

    while queue:
        #if reached:
        #    reached.pop(-1)
        #queue.pop(-1)
        print (path, '-->', end=' ') # for debug
        for node in queue:
            if node == destination:
                path.add(destination)# skips the end node otherwise 
                print ((perf_counter()- t1)/1000)
                return
            current_node_cost = min(tree[node].loc[(tree[node] < penalty)])
            if node not in path and current_node_cost < min(reached):
                cost_queue.append(current_node_cost)
        
        total_path_cost += min(cost_queue)
        

            
        reached.pop(0)
        queue.pop(0)
    '''

    


print(A_Star_Search('nodes.json', 1000, 'Arad', 'Bucharest'))





