# Depth First Search Pseudo code

A Depth First Search algorithm is better for searching very large datasets but can be slightly slower, due to the way it works.

This type of algorithm works by decending straight to the leaf of the left most branch, checking if that contains the desired value and then mosts the the next leaf of the next branch across until the entire tree is eventually searched.

*Like BFS, it returns as soon as the desired value is found within the tree; it ignores cost*


    FUNCTION dfs(tree = dictionary, [start , destination] = word or number) Returns path or failure

        queue <-- LIFO queue containing one level of tree

        IF start == destination:
        RETURN error "You are already at your destination"

        ELSE IF start NOT IN tree:
        return error "START must exist in the tree"

        WHILE queue NOT empty:
            node <-- queue.pop(0)
            FOR item IN tree:
                IF item == DESTINATION:
                RETURN 

        RETURN FAILURE "A path could not be found"

