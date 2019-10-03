def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))

    return edges

def find_isolated_nodes(graph):
  isolated = []
  for node in graph:
    if not graph[node]:
      isolated += node
  return isolated

def isconnected(graph):
  length=len(find_isolated_nodes(graph))
  if length==0:
    return "Connceted"
  else:
    return "Unconnected"

def isdirected(graph):
  for node in graph:
    for orientpath in graph:
      if node not in graph[orientpath]:
        return "Not directed"
  return "Directed"

def cyclic(graph):
  path = set()
  def visit(vertex):
    path.add(vertex)
    for neighbour in graph.get(vertex, ()):
      if neighbour in path or visit(neighbour):
        return True
    path.remove(vertex)
    return False

  return any(visit(v) for v in graph)

def iscomplete(graph):
  if cyclic(graph)==True:
    return "Completed"
  else:
    return "Uncompleted"


graph1= {
  "A" : ["B","C"],
  "B" : ["A","C"],
  "C" : ["A","B","D","E","F"],
  "D" : ["C"],
  "E" : ["C"],
  "F" : ["C"]
}

graph2={
  "A":["B","C"],
  "B":["A","D"],
  "C":["A","D"],
  "D":["B","C"],
  "E":[]
}

graph3={
  "A":["B","C","D"],
  "B":["A","D","C"],
  "C":["A","B","D"],
  "D":["B","C","D"]
}

graph4={
  "A":["B","D"],
  "B":["A","C"],
  "C":["D"],
  "D":["E","A"],
  "E":["A"]
}

generate_edges(graph1)
generate_edges(graph2)
generate_edges(graph3)
generate_edges(graph4)

print("Graph1 ",isconnected(graph1))
print("Graph2 ",isconnected(graph2))
print("Graph3 ",isconnected(graph3))
print("Graph4 ",isconnected(graph4))

print("Graph1 ",iscomplete(graph1))
print("Graph2 ",iscomplete(graph2))
print("Graph3 ",iscomplete(graph3))
print("Graph4 ",iscomplete(graph4))

print("Graph1 ",isdirected(graph1))
print("Graph2 ",isdirected(graph2))
print("Graph3 ",isdirected(graph3))
print("Graph4 ",isdirected(graph4))
