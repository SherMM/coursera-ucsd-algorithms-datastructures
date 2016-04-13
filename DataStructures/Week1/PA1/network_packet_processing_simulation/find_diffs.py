import sys

def find_diffs(file1, file2):
    with open(file1) as f1:
        data1 = [line.strip() for line in f1]

    with open(file2) as f2:
        data2 = [line.strip() for line in f2]

    print("File 1 has {} lines".format(len(data1)))
    print("File 2 has {} lines".format(len(data2)))
    for i in range(len(data1)):
        if data1[i] != data2[i]:
            print("Difference at line {}".format(i))
            print("File 1 line {} is {}".format(i, data1[i]))
            print("File 2 line {} is {}".format(i, data2[i]))

if __name__ == "__main__":
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    find_diffs(file1, file2)
