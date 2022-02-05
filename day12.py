def adj_list(edges):
    graph = {}

    for v, w in edges:
        graph.setdefault(v, []).append(w)
        graph.setdefault(w, []).append(v)

    return graph

def num_paths(graph, start, end, visited):
    paths = 0

    if start == end:
        return 1

    if start.islower():
        visited.add(start)

    for n in graph[start]:
        if n not in visited:
            paths += num_paths(graph, n, end, visited)

    visited.discard(start)

    return paths

def main():
    with open("day12_input.txt") as f:
        graph = adj_list(map(str.strip, l.split("-")) for l in f)
        print(f"There are {num_paths(graph, 'start', 'end', set())} total paths!")

if __name__ == "__main__":
    main()
