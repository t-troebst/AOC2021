def adj_list(edges):
    graph = {}

    for v, w in edges:
        graph.setdefault(v, []).append(w)
        graph.setdefault(w, []).append(v)

    return graph

def num_paths(graph, start, end, visited, visited_twice_ex, visited_twice=False):
    paths = 0

    if start == end:
        return 1

    vt = False

    if start.islower():
        if start in visited:
            vt = True
        else:
            visited.add(start)

    if not visited_twice:
        for n in graph[start]:
            if n in visited and n not in visited_twice_ex:
                paths += num_paths(graph, n, end, visited, visited_twice_ex, True)


    for n in graph[start]:
        if n not in visited:
            paths += num_paths(graph, n, end, visited, visited_twice_ex, visited_twice)

    if not vt:
        visited.discard(start)

    return paths

def main():
    with open("day12_input.txt") as f:
        graph = adj_list(map(str.strip, l.split("-")) for l in f)
        np = num_paths(graph, "start", "end", set(), {"start", "end"})
        print(f"There are {np} total paths!")

if __name__ == "__main__":
    main()
