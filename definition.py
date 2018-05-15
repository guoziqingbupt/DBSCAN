import numpy as np


class DataPoint(object):
    def __init__(self, coordinates):
        """
        :param coordinates: the ndarray object
        """
        self.coordinates = coordinates
        self.neighborhood = set()

    def isCore(self, db, radius, minPts):
        """

        :param db: the database whose elements are DataPoint objects.
        :param radius: the radius of a point's neighborhood
        :param minPts:
        :return:
        """
        for i in db:
            if np.linalg.norm(self.coordinates - i.coordinates) <= radius:
                self.neighborhood.add(i)

        if len(self.neighborhood) >= minPts:
            return True
        return False
