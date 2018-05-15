import random
import csv
import matplotlib.pyplot as plt


def conData():
    """
    1. Construct data points who are in the cluster and the noise points
    2. Write these data points in a csv file
    :return: None
    """

    # construct the cluster points
    x1, y1 = [], []
    x2, y2 = [], []
    xlow1, ylow1 = 2, 3
    delta1, delta2 = 0.2, 0.5
    range1, range2 = [3.5, 7], [5, 5.3]

    index = 0
    while index < 400:
        for i in range(20):
            x1.append(random.uniform(xlow1, xlow1 + delta1))
            y1.append(random.uniform(ylow1, ylow1 + delta2))

            x2.append(random.uniform(range1[0], range1[1]))
            y2.append(random.uniform(range2[0], range2[1]))

        xlow1 += delta1/2
        ylow1 += delta2/2
        index += 20

    # construct the noise points
    noise_x = [2.1, 5.8, 5.6, 1.52, 4, 3.2, 7.6, 4.9, 5.3, 1.6, 3.7]
    noise_y = [6.1, 7, 2.7, 7.92, 6.1, 2.9, 5.2, 8.4, 3.5, 7.8, 3.5]

    # write all the data points in csv file "data.scv"
    csvFile = open("data.csv", "w")
    fileHeader = ["x", "y"]
    writer = csv.writer(csvFile)

    writer.writerow(fileHeader)
    for i in range(400):
        writer.writerow([x1[i], y1[i]])
        writer.writerow([x2[i], y2[i]])

    for i in range(len(noise_x)):
        writer.writerow([noise_x[i], noise_y[i]])

    csvFile.close()


if __name__ == "__main__":

    # construct data
    conData()

    # read the constructed data
    csvFile = open("data.csv", "r")
    reader = csv.reader(csvFile)
    x, y = [], []
    for item in reader:
        if reader.line_num == 1:
            continue
        x.append(item[0])
        y.append(item[1])
    csvFile.close()

    # plot the constructed data
    plt.axis([1, 8, 2, 9])
    plt.scatter(x, y, c="k", marker=".")
    plt.show()

