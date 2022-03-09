import math


class Geometry:

    @staticmethod
    def take_distance(tuple1, tuple2, init=0):
        """
            returns the distance of two point
        """
        x1, x2 = tuple1[0], tuple2[0]
        y1, y2 = tuple1[1], tuple2[1]
        m = int(math.sqrt(
            math.pow((x1-x2), 2) + math.pow((y1-y2), 2)
        ))
        if init == 1:
            return abs(m//2)
        else:
            return abs(m)

    @staticmethod
    def take_center(tuple1, tuple2):
        """
            return the center of rect
        """
        x1, x2 = tuple1[0], tuple2[0]
        y1, y2 = tuple1[1], tuple2[1]
        cx = (x1 + x2)//2
        cy = (y1 + y2)//2
        return cx, cy

    @staticmethod
    def is_in(point, tuple1, tuple2):
        """
            Must return An boolean value when the point is in the area of react
            function must be return True, else it returns false
            point is a tuple class
        """
        di = Geometry.take_distance(tuple1, tuple2, init=1)
        dp = Geometry.take_distance(
            point, Geometry.take_center(tuple1, tuple2)
        )
        if dp <= di:
            return True
        else:
            return False
