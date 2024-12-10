#  orientation  
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0                    # Collinear
    return 1 if val > 0 else 2      # 1 -> Clockwise, 2 -> Counter-clockwise

def jarvis_march(points):
    # Find the leftmost point
    leftmost = min(points, key=lambda p: p[0])

    # Initialize the hull
    hull = []
    p = leftmost
    while True:
        # Add the current point to the hull
        hull.append(p)
        # Find the next point
        q = points[0]
        for r in points:
            if q == p or orientation(p, q, r) == 2:  # Counter-clockwise
                q = r
        # If we reached the first point, break
        if q == leftmost:
            break
        p = q  # Move to the next point
    return hull

points = [(0, 0), (2, 1), (1, 2), (3, 3), (4, 0), (5, 2), (2, 3), (2, 5), (3, 7), (2, 2)]

convex_hull = jarvis_march(points)

print("Convex Hull:", convex_hull)

import matplotlib.pyplot as plt

x_points, y_points = zip(*points)
x_hull, y_hull = zip(*convex_hull)

plt.figure(figsize=(6, 6))
plt.scatter(x_points, y_points, color='blue', label='Points')  # Plot original points
plt.plot(x_hull + (x_hull[0],), y_hull + (y_hull[0],), color='red', label='Convex Hull')  # Plot Convex Hull

plt.fill(x_hull + (x_hull[0],), y_hull + (y_hull[0],), color='lightblue', alpha=0.5)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Convex Hull using Jarvis March (Gift Wrapping)')
plt.legend()
plt.show()
