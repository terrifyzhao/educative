from heapq import *


# 最接近远点的k个点

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

    def __lt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()

    def distance_from_origin(self):
        return self.x * self.x + self.y * self.y


def find_closest_points(points, k):
    result = []

    for i in range(k):
        heappush(result, points[i])

    for p in points[k:]:
        if p.distance_from_origin() < result[0].distance_from_origin():
            heappop(result)
            heappush(result, p)

    return result


def main():
    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()


main()
