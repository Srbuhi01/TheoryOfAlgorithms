import math
import matplotlib.pyplot as plt

#  orientation of  (p, q, r)
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    return 1 if val > 0 else 2  # 1 -> Clockwise, 2 -> Counter-clockwise

#  distance between two points
def distance(p, q):
    return (q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2

def graham_scan(points):
    #  lowest y-coordinate (and leftmost)
    start = min(points, key=lambda p: (p[1], p[0]))

    #  Sort the points based on polar angle with respect to the 'start' point
    sorted_points = sorted(points, key=lambda p: (math.atan2(p[1] - start[1], p[0] - start[0]), distance(start, p)))

    # Step 3: Initialize the hull with the start point and the first point in the sorted list
    hull = [start, sorted_points[0]]

    # Process each point
    for p in sorted_points[1:]:
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], p) != 2:
            hull.pop()  # Remove the last point if we make a clockwise turn
        hull.append(p)  # Add the new point to the hull

    return hull

# Example usage
points = [(0, 0), (2, 1), (1, 2), (3, 3), (4, 0), (5, 2), (2, 3), (2, 5), (3, 7), (2, 2)]

# Perform Graham's Scan to find the Convex Hull
convex_hull = graham_scan(points)

# Output the Convex Hull
print("Convex Hull:", convex_hull)

# Plotting the points and Convex Hull
x_points, y_points = zip(*points)
x_hull, y_hull = zip(*convex_hull)

plt.figure(figsize=(6, 6))
plt.scatter(x_points, y_points, color='blue', label='Points')  # Plot original points
plt.plot(x_hull + (x_hull[0],), y_hull + (y_hull[0],), color='red', label='Convex Hull')  # Plot Convex Hull

plt.fill(x_hull + (x_hull[0],), y_hull + (y_hull[0],), color='lightblue', alpha=0.5)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Convex Hull using Graham\'s Scan')
plt.legend()
plt.show()
