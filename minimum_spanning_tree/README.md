# MST
THe `minimum spanning tree` for any graph is a `acyclic` and `connected` graph with the `minimum weight` subset. We can use greedy paradigm to compute the MST for any undirected and connected graph.

## Kruskals
### Algorithm 
1. Sort edges by increasing weight
2. `mst_edges` = []
3. For every edge: Add it to mst_edges if adding it does not create a cycle.

### How to check if cycle is present
1. Maintain an map `A` with an entry for each vertex that indicates which connected component it belongs to.
2. Intially all the vertices are connected to only themselves, so each elemnent in the map has the value equal to itself.
3. When considering each edge, check the values for both the end points of the edge in the map. If the valeus are same, then adding the edge will create a cycle.
4. If the edge is added, update the both vertices in the map to the lower of the two vertices.

### Time Complexity
1. Sorting the edges by weight takes `O(|E|log|E|)` steps.
2. Check for cycles - `|E|` checks each taking `O(1)` steps.
3. Adding an edge to `mst_edges` - Updating array takes `O(|V|)` time and array is updated exactly `|V | - 1` times.
4. Total running time = `O(|E|log|E|+|V|^2)`

## Prims
### Algorithm 
1. Sort edges by increasing weight
2. Let `S` = {`a`} for some vertex `a`.
3. While `S` != `V`, add next edge `e(u, v)`, such that `u ∈ S` and `v ∉ V`. (Note: `V` is set of all vertices)

### Time Complexity
1. Sorting the edges by weight takes `O(|E|log|E|)` steps.
2. The while loop will run atmost `|V|` times.
3. The inner for loop runs atmost `|E|` times.
4. Total running time = `O(|E|log|E|+|V||E|)`

For detailed explanation, refer [Prof. Andrew McGregor's lecture slides](https://people.cs.umass.edu/~mcgregor/611S24/lec04.pdf).