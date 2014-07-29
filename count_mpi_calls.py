__author__ = 'qiuqiyuan'

import numpy as np


def main():
    # this function will parse the output file and count mpi count
    data = np.loadtxt("2_1", dtype=int)
    print data
    cycle = 2 * 2
    m = np.resize(data, (len(data) / (cycle * 2), cycle * 2))

    for i, row in enumerate(m):
        if i+1 < (len(data) / (cycle * 2)):
            print m[i + 1, :] - m[i, :]


if __name__ == "__main__":
    main()