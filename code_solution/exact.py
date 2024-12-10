import sys
import time
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

    for perm in permutations(vertices):     # Generate all permutations of vertices O(N!)
        cover = set()   #O(1)
        for v in perm:  # O(N)
            cover.add(v)   # O(1)
            if all_edges_covered(cover, edges):    # O(N)
                if best_cover is None or len(cover) < len(best_cover): # Check if it's the best cover
                    best_cover = cover.copy()
                
                break

        # If we found a cover of size 1 we can stop early
        if best_cover and len(best_cover) == 1:
            break
    return best_cover

if __name__ == "__main__":
    start_time = time.time()
    vertices, edges = read_graph()
    min_cover = find_min_vertex_cover_permutation(vertices, edges)
    if min_cover is not None:
        print("Minimum Vertex Cover:", " ".join(min_cover))
    else:
        print("No vertex cover found.")

    end_time = time.time()

    print(f"Time taken: {end_time - start_time:.6f} seconds")
