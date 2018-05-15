import csv
from definition import *
import matplotlib.pyplot as plt


def dbscan(db, radius, minPts):
    """

    :param db:
    :param radius:
    :param minPts:
    :return:
    """
    visited = set()
    noise = set()
    results = []

    while len(visited) < len(db):

        core = None
        C = set()

        # find the core point
        temp = set()
        for point in db - visited:
            temp.add(point)
            if point.isCore(db - {point}, radius, minPts):
                core = point
                break
            else:
                noise.add(point)
        visited.update(temp)

        # can't find any core point, i.e., the cluster process should be terminated
        if not core:
            break

        # construct the new cluster C
        flag = True
        candidates = {core}

        # flag denotes whether there is at least one core point in candidates
        while flag:

            flag = False
            tempCandidates = set()
            for member in candidates:

                # remove the boundary points in noise
                if member in noise:
                    noise.remove(member)

                # label the cur as visited
                if member not in visited:
                    visited.add(member)

                # if cur not belongs to other clusters, add it in the cluster C
                belongToOtherCluster = False
                for cluster in results:
                    if member in cluster:
                        belongToOtherCluster = True
                        break
                if not belongToOtherCluster:
                    C.add(member)

                # if cur is core, add its neighborhood in tempCandidates
                if member.isCore(db - {member}, radius, minPts):
                    tempCandidates.update(member.neighborhood - C)
                    flag = True
            candidates = set() | tempCandidates
        results.append(C)
    return results


def conDB():

    db = set()

    csvFile = open("data.csv", "r")
    reader = csv.reader(csvFile)
    for item in reader:
        if reader.line_num == 1:
            continue
        db.add(DataPoint(np.array([float(item[0]), float(item[1])])))
    csvFile.close()
    return db

if __name__ == "__main__":

    db = conDB()
    plt.axis([1, 8, 2, 9])

    for cluster in dbscan(db, 0.2, 3):
        x = [i.coordinates[0] for i in cluster]
        y = [i.coordinates[1] for i in cluster]
        plt.scatter(x, y, marker='.')
    plt.show()