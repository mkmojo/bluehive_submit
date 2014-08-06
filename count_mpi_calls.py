__author__ = 'qiuqiyuan'

import numpy as np
import os
import sys


def main():
    # this function will parse the output file and count mpi count
    for file_name in sys.argv[1:]:
        data = np.loadtxt(file_name, dtype=int)
        list = file_name.split("_")
        num_proc = int( list[0] )
        cycle = num_proc * 2
        m = np.resize(data, (len(data) / (cycle * 2), cycle * 2))

    for i, row in enumerate(m):
        if i+1 < (len(data) / (cycle * 2)):
            print m[i + 1, :] - m[i, :]


if __name__ == "__main__":
    main()
