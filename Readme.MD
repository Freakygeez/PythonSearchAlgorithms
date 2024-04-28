# Python search algorithms

Contained within this repo is the code for basic: 

* Breadth First Search
* Bidirectional Search
* Depth First Search
* Greedy Best First Search
* A* Search
* Bounded Cost Search

More ML ones coming soon...

## Algorithm visualisation 
This graph will be used in all future algorithms (and existing will be updated to use this too)


```mermaid

flowchart LR

Arad -- 75 --> Zerind
Arad -- 140 --> Sibiu
Arad -- 118 --> Timisoara

Timisoara -- 111 --> Lugoj
Lugoj -- 70 --> Mehadia
Mehadia -- 75 --> Drobeta
Drobeta -- 120 --> Craiova
Craiova -- 146 --> R



Zerind -- 71 --> Oradea


Oradea -- 151 --> Sibiu

Sibiu -- 99 -->  Fagaras
Fagaras -- 211 --> Bucharest
Sibiu -- 80 --> R[Rimnicu Vicea]

R -- 97 --> Piesti
Piesti -- 138 --> Craiova
Piesti -- 101 --> Bucharest
Bucharest -- 90 --> Giurgiu
Bucharest -- 85 --> Urziceni

Urziceni -- 98 --> Hirsova
Urziceni -- 142 --> Vaslui

Hirsova -- 86 --> Eforie

Vaslui -- 92 --> Iasi
Iasi -- 87 --> Neamt


```

## Breadth First Search Output:
Arad  -->  Zerind  -->  Sibiu  -->  Timisoara  -->  Ordea  -->  Fagaras  -->  0.23

## Depth First Search Output:
Arad  -->  Timisoara  -->  Lugoj  -->  Mehadia  -->  Drobeta  -->  Craiova  -->  Rimmnicu Vicea  --> ERROR due to circular path
