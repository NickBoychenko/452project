import sys

def solve_vertex_cover():
    lines = sys.stdin.read().strip().split('\n')
    m = int(lines[0])
    
    # Parse edges
    edges = []
    for i in range(1, m+1):
        u, v = lines[i].split()
        edges.append((u, v))

    vertex_cover = set()
    
    for (u, v) in edges:
        # If either vertex is in the cover, skip
        if u in vertex_cover or v in vertex_cover:
            continue

        # Add both edges
        vertex_cover.add(u)
        vertex_cover.add(v)

    print(" ".join(vertex_cover))


if __name__ == "__main__":
    solve_vertex_cover()
