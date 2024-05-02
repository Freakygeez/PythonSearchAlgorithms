# A* Search Pseudo code

A* search implements a cost function (i.e. distance) whilst avoiding the issue of getting stuck in loops

    searchTree <-- dictionary containing the nodes
    path <-- list
    queue <-- list

    FUNCTION A_Star(searchTree, [start , destination] = word or number) Returns path or failure

        queue <-- LIFO queue containing one level of tree
        cost < -- 0

        IF start == destination:
        RETURN error "You are already at your destination"

        ELSE IF start NOT IN tree:
        return error "START must exist in the tree"

        WHILE queue NOT empty:
            node <-- queue.pop(0)
            IF item == DESTINATION:
                RETURN path, cost

            FOR item IN Search(tree, node):
                item <-- node
                IF node NOT IN path OR node[cost] < reached[node][cost]: #if the node is not in the path or if the node is cheaper, use that one
                path[node] <-- item
                queue.append(item) 
                cost += node[cost]

        RETURN FAILURE "A path could not be found"


