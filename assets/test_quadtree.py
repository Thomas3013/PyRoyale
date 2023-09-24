import unittest
from QuadTree import Point, Rectangle, QuadTree  # Import your QuadTree implementation

class TestQuadTree(unittest.TestCase):

    def setUp(self):
        # Create a QuadTree with a boundary
        boundary = Rectangle(0, 0, 100, 100)
        self.quadtree = QuadTree(boundary, maxpoints=4)

    def test_insert_and_query(self):
        # Insert some points
        points = [Point(10, 10), Point(20, 20), Point(30, 30)]
        for point in points:
            self.quadtree.insert(point)

        # Query points within a bounding box
        query_boundary = Rectangle(5, 5, 25, 25)
        found_points = self.quadtree.query(query_boundary, [])
        expected_points = [Point(10, 10), Point(20, 20)]
        self.assertEqual(found_points, expected_points)

    def test_query_radius(self):
        # Insert some points
        points = [Point(10, 10), Point(20, 20), Point(30, 30)]
        for point in points:
            self.quadtree.insert(point)

        # Query points within a radius
        center = (15, 15)
        radius = 10
        found_points = self.quadtree.query_radius(center, radius, [])
        expected_points = [Point(10, 10), Point(20, 20)]
        self.assertEqual(found_points, expected_points)

    # Define more test cases as needed

if __name__ == '__main__':
    unittest.main()
