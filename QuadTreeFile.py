import numpy as np


class Point:

    def __init__(self, payload=None):
        self.payload = payload
        self.x = payload.get_x()
        self.y = payload.get_y()
        print(self.y)
        print(self.x)

    def __repr__(self):
        return '{}: {}'.format(str((self.x, self.y)), repr(self.payload))

    def __str__(self):
        return 'P({:.2f}, {:.2f})'.format(self.x, self.y)

    def distance_to(self, other):
        try:
            other_x, other_y = other.x, other.y
        except AttributeError:
            other_x, other_y = other
        return np.hypot(self.x - other_x, self.y - other_y)


class Rectangle:

    def __init__(self, cx, cy, w, h):
        self.cx = cx
        self.cy = cy
        self.w = w
        self.h = h
        self.west_edge = cx - w / 2
        self.east_edge = cx + w / 2
        self.north_edge = cy - h / 2
        self.south_edge = cy + h / 2

    def __repr__(self):
        return str((self.west_edge, self.east_edge, self.north_edge,
                    self.south_edge))

    def __str__(self):
        return '({:.2f}, {:.2f}, {:.2f}, {:.2f})'.format(self.west_edge,
                                                         self.north_edge, self.east_edge, self.south_edge)

    def contains(self, point):
        try:
            point_x = point.x
            point_y = point.y
        except AttributeError:
            point_x = point
            point_y = point

        return (self.west_edge <= point_x < self.east_edge and
                self.north_edge <= point_y < self.south_edge)

    def intersects(self, other):
        return not (other.west_edge > self.east_edge or
                    other.east_edge < self.west_edge or
                    other.north_edge > self.south_edge or
                    other.south_edge < self.north_edge)


class QuadTree:

    def __init__(self, boundary, maxpoints=4, depth=0):
        self.boundary = boundary
        self.maxpoints = maxpoints
        self.points = []
        self.depth = depth
        self.divided = False
        # boundary is rect object max / min of area
        # max points is max points before node branches into four more nodes
        # depth is how deep node is

    def divide(self):  # divide branch / spawn more child nodes
        cx = self.boundary.cx
        cy = self.boundary.cy
        w = self.boundary.w / 2
        h = self.boundary.h / 2

        self.nw = QuadTree(Rectangle(cx - w / 2, cy - h / 2, w, h),
                           self.maxpoints, self.depth + 1)
        self.ne = QuadTree(Rectangle(cx + w / 2, cy - h / 2, w, h),
                           self.maxpoints, self.depth + 1)
        self.se = QuadTree(Rectangle(cx + w / 2, cy + h / 2, w, h),
                           self.maxpoints, self.depth + 1)
        self.sw = QuadTree(Rectangle(cx - w / 2, cy + h / 2, w, h),
                           self.maxpoints, self.depth + 1)
        self.divided = True

    def insert(self, point):
        if not self.boundary.contains(point):
            # point outside original rectangle boundaries
            return False
        if len(self.points) < self.maxpoints:
            # room for point without dividing quadtree
            self.points.append(point)
            return True

        if not self.divided:
            self.divide()

        return (self.ne.insert(point) or
                self.nw.insert(point) or
                self.se.insert(point) or
                self.sw.insert(point))

    def query(self, boundary, found_points):
        if not self.boundary.intersects(boundary):
            return False  # checking if boundary is in boundary
        for point in self.points:
            if boundary.contains(point):
                found_points.append(point)
        if self.divided:
            self.nw.query(boundary, found_points)
            self.ne.query(boundary, found_points)
            self.se.query(boundary, found_points)
            self.sw.query(boundary, found_points)
        return found_points

    def query_circle(self, boundary, center, radius, found_points):
        # boundary = rect obj
        # don't call directly call query_radius
        if not self.boundary.intersects(boundary):
            return False  # not in radius
        for point in self.points:
            if boundary.contains(point) and point.distance_to(center) <= radius:
                found_points.append(point)
            if self.divided:
                self.nw.query_circle(boundary, center, radius, found_points)
                self.ne.query_circle(boundary, center, radius, found_points)
                self.se.query_circle(boundary, center, radius, found_points)
                self.sw.query_circle(boundary, center, radius, found_points)
            return found_points

    def query_radius(self, center, radius, found_points):
        # find square that bounds the search circle as a rectangle object
        boundary = Rectangle(*center, 2 * center, 2 * radius)
        return self.query_circle(boundary, center, radius, found_points)

    def __len__(self):

        npoints = len(self.points)
        if self.divided:
            npoints += len(self.nw) + len(self.ne) + len(self.se) + len(self.sw)
        return npoints

    def reset(self,node):
        i = 0
        for i in range(len(self.points)):
            if self.points[i] == node:
                break
        else:
            print("Node not found")
        self.points.pop(i)
        self.insert(node)


    def __str__(self):
        sp = ' ' * self.depth * 2
        s = str(self.boundary) + '\n'
        s += sp + ', '.join(str(point) for point in self.points)
        if not self.divided:
            return s
        return s + '\n' + '\n'.join([
            sp + 'nw: ' + str(self.nw), sp + 'ne: ' + str(self.ne),
            sp + 'se: ' + str(self.se), sp + 'sw: ' + str(self.sw)])




# https://scipython.com/blog/quadtrees-2-implementation-in-python/

unitTree = QuadTree(Rectangle(268, 381, 482 - 54, 764))
