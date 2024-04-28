# Breadth First Search Pseudo code

A Breadth First search algorithm is faster than, say, a Depth First Search at the expense of requiring more ram.

This type of algorithm works by loading whole layers at a time into the queue, whilst not an issue for small problems it would not be reccomended for anything complex.

Breadth First Search does not use a cost function and may sometimes be referred to as a *uniform cost search*

    FUNCTION bfs(tree = dictionary, [start , destination] = word or number) Returns path or failure

        path <-- an empty list
        queue <-- FIFO queue containing one level of tree

        IF start == destination:
        RETURN error "You are already at your destination"

        ELSE IF start NOT IN tree:
        return error "START must exist in the tree"

        WHILE queue NOT empty:
            tree.pop(one dictionary item)

            FOR item IN tree:
                path.push(item)
                IF item == DESTINATION:
                RETURN path

        RETURN FAILURE "A path could not be found"

