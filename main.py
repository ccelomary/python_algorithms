from short_path import short_path

graph = {
    'A' : {'B': 1, 'C': 3},
    'B': {'G': 3, 'A': 1},
    'C': {'D': 3, 'E': 2, 'A': 3},
    'D': {'F': 3, 'C': 2},
    'E': {'F': 1, 'C': 2},
    'F': {'E': 1, 'D': 3, 'G': 3},
    'G': {'F': 1, 'B': 3}
}


if __name__ == '__main__':
    print(short_path(graph, 'A', 'F'))