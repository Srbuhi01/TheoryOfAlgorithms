import matplotlib.pyplot as plt

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0                   # Collinear
    return 1 if val > 0 else 2     # CW or CCW

def on_segment(p, q, r):
    return (min(p[0], q[0]) <= r[0] <= max(p[0], q[0]) and       # if r is  in pq line
            min(p[1], q[1]) <= r[1] <= max(p[1], q[1]))

def do_intersect(p1, q1, p2, q2):
    #  orientations
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    
    # hatvum en
    if o1 != o2 and o3 != o4:
        return True

    # collinear/ ardyoq inchvor ket myus gci vra e
    if o1 == 0 and on_segment(p1, q1, p2): return True
    if o2 == 0 and on_segment(p1, q1, q2): return True
    if o3 == 0 and on_segment(p2, q2, p1): return True
    if o4 == 0 and on_segment(p2, q2, q1): return True

    return False

def draw_segments(p1, q1, p2, q2):
    plt.figure(figsize=(8, 6))
    plt.plot([p1[0], q1[0]], [p1[1], q1[1]], label="Segment 1", color="blue", linewidth=2)
    plt.plot([p2[0], q2[0]], [p2[1], q2[1]], label="Segment 2", color="orange", linewidth=2)

    plt.scatter(*zip(*[p1, q1, p2, q2]), color="red", zorder=5)
    plt.text(p1[0], p1[1], "p1", fontsize=10, color="blue", ha="right")
    plt.text(q1[0], q1[1], "q1", fontsize=10, color="blue", ha="right")
    plt.text(p2[0], p2[1], "p2", fontsize=10, color="orange", ha="left")
    plt.text(q2[0], q2[1], "q2", fontsize=10, color="orange", ha="left")

    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.legend()
    plt.title("Visualization of Line Segments")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.xlim(0, max(q1[0], q2[0]) + 1)
    plt.ylim(0, max(q1[1], q2[1]) + 1)
    plt.show()

# Example
p1, q1 = (1, 1), (4, 4)  # Segment 1
p2, q2 = (1, 4), (4, 1)  # Segment 2

# Check if the segments intersect
result = do_intersect(p1, q1, p2, q2)
print(f"Do segments intersect? {'Yes' if result else 'No'}")

#  the segments
draw_segments(p1, q1, p2, q2)
