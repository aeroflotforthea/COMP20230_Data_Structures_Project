# Implementing Graphs in Python

**Edge**: This a connection between nodes  
**Vertex**: This is a node

## Adjacency List

A: B, C, E  
B, A, C  
C: A,B,D,E  
D: C  
E: A, C  


## Adjacency Matrix
This is where you have a grid, and there's a 1 if there's a vertex, and a 0 if there isn't. 

A graph with weighted edges is much easier to implement with a matrix. You can put the weight in the matrix. 


A **sparse** graph is one where you have roughly the same number of edges and verticies. A **dense** graph is one where you have n^2 edges where n is the number of vertices.  

Adjacency list is better with sparse graphs, while a matrix is much faster for dense graphs, but takes up more space.  