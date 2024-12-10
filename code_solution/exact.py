import sys
from itertools import permutations

def read_graph():
    input_data = sys.stdin.read().strip().split('\n')
    E = int(input_data[0])
    edges = []
    vertices = set()
    for i in range(1, E+1):
        u, v = input_data[i].split()
        edges.append((u, v))
        vertices.add(u)
        vertices.add(v)
    return list(vertices), edges

def all_edges_covered(cover_set, edges):
    cover = set(cover_set)
    for (u, v) in edges:
        if u not in cover and v not in cover:
            return False
    return True

def find_min_vertex_cover_permutation(vertices, edges):
    best_cover = None
    # Generate all permutations of vertices
    for perm in permutations(vertices):
        cover = set()
        for v in perm:
            cover.add(v)
            if all_edges_covered(cover, edges):
                # Check if this cover is better than the best found so far
                if best_cover is None or len(cover) < len(best_cover):
                    best_cover = cover.copy()
                # Once we found a cover for this permutation, we can break
                # because continuing would only add more vertices and not be minimal for that permutation
                break

        # If we found a cover of size 1 (the smallest possible) we can stop early
        if best_cover and len(best_cover) == 1:
            break
    return best_cover

if __name__ == "__main__":
    vertices, edges = read_graph()
    min_cover = find_min_vertex_cover_permutation(vertices, edges)
    if min_cover is not None:
        print("Minimum Vertex Cover:", " ".join(sorted(min_cover)))
    else:
        print("No vertex cover found.")
