import random
'''
* Randomly generates a hamiltonan circuit with the number number of vertices over
* a determined number of steps. Please represent the circuit as a list of objects
* as described with the circuit variable below. Each entry in the circuit list
* should have two attributes: children and distances. These are parallel arrays
* where children[i] represents the index value of the ith child, and distances[i]
* represents the distance to the ith child. Please only include direct children in
* these lists (do not include grandchildren, etc.)
*
* num_vertices: number of vertices in the graph
* s: number of iterations to take
*
* Returns the circuit representation as described above
'''

def create_circuit(num_vertices: int, s: int):
  # create an empty graph with num_vertices vertices
  graph = {i: [] for i in range(num_vertices)}
    
  # add edges randomly for s iterations
  for i in range(s):
    # choose two vertices at random
    u, v = random.sample(range(num_vertices), 2)
    # add an edge between them if they are not already connected
    if v not in graph[u]:
      graph[u].append(v)
      graph[v].append(u)
    
    # add edges to vertices with no neighbors
    for i in range(num_vertices):
      if not graph[i]:
        u, v = random.sample(range(num_vertices), 2)
        graph[i].append(u)
        graph[u].append(i)
    
  # find a Hamiltonian circuit in the graph
  visited = set()
  start = random.randrange(num_vertices)
  path = [start]
  visited.add(start)
  while len(visited) < num_vertices:
    # find the vertex with the fewest unvisited neighbors
    neighbors = [v for v in graph[path[-1]] if v not in visited]
    min_neighbors = float('inf')
    next_vertex = None
    for v in neighbors:
      unvisited_neighbors = len([u for u in graph[v] if u not in visited])
      if unvisited_neighbors < min_neighbors:
        min_neighbors = unvisited_neighbors
        next_vertex = v
        
        if next_vertex is None:
          # backtrack if no neighbors are available
          path.pop()
          visited.remove(path[-1])
        else:
          # add the next vertex to the path and mark it as visited
          path.append(next_vertex)
          visited.add(next_vertex)
    
  # create the circuit representation
  circuit = []
  for i in range(num_vertices):
    children = [graph[i][j] for j in range(len(graph[i])) if graph[i][j] in path and graph[i][j] != path[(path.index(i) + 1) % num_vertices]]
    distances = [1] * len(children)
    circuit.append({'children': children, 'distances': distances})
    
  return circuit


'''
* This is a stub that you can use to test the rest of the program. The code in this
* method will not be executed during grading, so you don't need to worry about user
* input.
'''
def main():
  num_vertices = 10
  s = 20
  
  circuit = create_circuit(num_vertices, 20)
  print(circuit)


main()