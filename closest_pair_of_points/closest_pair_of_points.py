import random
import math
import time


def generate_points(num_points=20, x_min=0, x_max=100, y_min=0, y_max=100):
    points = set()
    while len(points) < num_points:
        x = random.randint(x_min, x_max)
        y = random.randint(y_min, y_max)
        points.add((x, y))
    return list(points)


def sort_points_by_x(points):
    return sorted(points, key=lambda point: point[0])


def sort_points_by_y(points):
    return sorted(points, key=lambda point: point[1])


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def closest_pair_of_points(x_sorted_points, y_sorted_points):

    points = x_sorted_points

    if len(points) < 2:
        print("Atleast 2 points required to compute distance")

    elif len(points) == 2:
        return distance(points[0], points[1])

    elif len(points) == 3:
        d_1 = distance(points[0], points[1])
        d_2 = distance(points[1], points[2])
        d_3 = distance(points[0], points[2])

        return min(d_1, d_2, d_3)

    else:
        mid = len(points) // 2
        points_l = points[:mid]
        points_r = points[mid:]

        d_l = closest_pair_of_points(points_l, y_sorted_points)
        d_r = closest_pair_of_points(points_r, y_sorted_points)

        d = min(d_l, d_r)

        m = (points_l[-1][0] + points_r[0][0]) / 2

        points_m = [
            point for point in y_sorted_points if point[0] > m - d and point[0] < m + d
        ]

        d_m = 999

        for i in range(len(points_m)):
            for j in range(i + 1, i + 8):
                if j >= len(points_m):
                    break
                d_m = min(d_m, distance(points_m[i], points_m[j]))

        return min(d_m, d)


def naive_closest_pair_of_points(points):

    d = 999
    for point_1 in points:
        for point_2 in points:
            if point_1 == point_2:
                continue
            d = min(d, distance(point_1, point_2))

    return d


def main():
    print(
        "Minimum Distance Between Pair of Points in a Plane using Divide and Conquer Approach\n"
    )
    n = 20
    x_min = 0
    x_max = 100
    y_min = 0
    y_max = 100
    print(f"n = {n} points, where {x_min}<=x<={x_max} and {y_min}<=y<={y_max}.\n")

    points = generate_points(n, x_min, x_max, y_min, y_max)

    x_sorted_points = sort_points_by_x(points)
    y_sorted_points = sort_points_by_y(points)

    print("Points are : \n")
    for point in points:
        print(point)

    print("\nUsing naive O(n^2) approach - ")
    start = time.time()
    d_naive = naive_closest_pair_of_points(points)
    end = time.time()
    print(f"Time taken - {(end-start):8f}")
    print(f"Distance between closest pair of points = {d_naive:4f}\n")

    print("Using divide and conquer O(nlogn) approach - ")
    start = time.time()
    d_algo = closest_pair_of_points(x_sorted_points, y_sorted_points)
    end = time.time()
    print(f"Time taken - {(end-start):4f}")
    print(f"Distance between closest pair of points = {d_algo:4f}\n")


if __name__ == "__main__":
    main()
