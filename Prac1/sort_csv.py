import numpy as np
import DSAsorts as sort


class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name


def read_ids_to_array(filename):
    f = open(filename, "r")
    try:
        students = []
        for line in f:
            id, name = line.split(",")
            students.append(Student(id, name))
    except Exception as e:
        print("Error: ", e)
    f.close()

    ids_array = np.zeros(len(students))
    for i in range(len(ids_array)):
        ids_array[i] = students[i].id
    return ids_array


def save_names(students):
    f = open("output.csv", "w")
    try:
        for i in range(len(students)):
            f.write(str(students[i])+"\n")
    except Exception as e:
        print("Error ", e)
    f.close()


def main():
    ids = read_ids_to_array("RandomNames7000(2).csv")
    sorted = sort.selectionSort(ids)
    save_names(sorted)


if __name__ == "__main__":
    main()
