graph = {
        's': {'a': 6, 'b': 5, 'c': 5},
        'a': {'d': -1},
        'b': {'a': -2, 'd': 1},
        'c': {'b': -2, 'e': -1},
        'd': {'f': 3},
        'e': {'f': 3},
        'f': {}
        }

inf = float('inf')
dist_vals = {}
paths = {}
for v in graph:
    dist_vals[v] = inf

dist_vals['s'] = 0

def run_algorithm ():
    changed = False
    for v in graph:
        for edge in graph[v]:
            if dist_vals[v] + graph[v][edge] < dist_vals[edge]:
                #if current vector + edge is less than connecting vector distance, set to current vector + edge
                dist_vals[edge] = dist_vals[v] + graph[v][edge]
                paths[edge] = v
                changed = True
    return changed

for i in range(len(graph)-1):
    if not run_algorithm():
        break

print("a) Shortest distance from source to each node (Source 's' included):")
print(dist_vals)

print("\nb) Shortest Paths from Source to Node:")
source = 's'
for vertex in paths:
    current = vertex
    out_string = vertex
    while current != source:
        current = paths[current]
        out_string = current + "->" + out_string
    print(out_string)


print('\nc) Was a negative cycle detected?: ')
print(run_algorithm())
