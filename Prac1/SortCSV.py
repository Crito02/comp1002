import sys
import numpy as np
from DSAsorts import bubbleSortStudentObject,\
                     insertionSortStudentObject,\
                     selectionSortStudentObject


class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name


def read_ids_to_array_no_list(filename):
    """
    read ids from file and return as numpy array
    """
    try:
        with open(filename, "r") as f:
            # read student id and name into numpy array
            temp = np.genfromtxt(f,
                                 delimiter=",",
                                 dtype=[("id", int), ("name", "U20")])

            students = np.zeros(len(temp), dtype=Student)
            for i in range(len(temp)):
                students[i] = Student(temp[i][0], temp[i][1])

    except Exception as e:
        print("Error: ", e)
    return students


def read_ids_to_array_using_list(filename):
    try:
        with open(filename, "r") as f:
            students = []
            for line in f:
                id, name = line.split(",")
                students.append(Student(id, name))
    except FileNotFoundError as e:
        print("Error: ", e)

    ids_array = np.zeros(len(students), dtype=Student)
    for i in range(len(ids_array)):
        ids_array[i] = Student(students[i].id, students[i].name)
    return ids_array


def save_to_file(list, filename):
    try:
        with open(filename, "w") as f:
            for i in range(len(list)):
                f.write(str(list[i].id) + "," + list[i].name + "\n")
    except Exception as e:
        print("Error ", e)


def main(filename, sort_type):
    # Read ids from file
    ids = read_ids_to_array_no_list(filename)

    # Sort ids
    if sort_type == "bubble":
        bubbleSortStudentObject(ids)
    elif sort_type == "insertion":
        insertionSortStudentObject(ids)
    elif sort_type == "selection":
        selectionSortStudentObject(ids)
    else:
        raise NotImplementedError("Sort type not implemented")

    for i in range(len(ids)-1):
        if ids[i].id > ids[i+1].id:
            raise ValueError("Sort failed")


if __name__ == "__main__":
    # Take filename and sort type from command line
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("SortCSV.py <input_filename> <sort_type>")
        sys.exit()
    elif len(sys.argv) != 3:
        print("Incorrect number of arguments, use -h or --help for help")
        sys.exit()
    elif sys.argv[2] not in ["bubble", "insertion", "selection"]:
        print("Sort type not recognised, choose from: 'bubble', 'insertion'," \
              + "'selection'")
        sys.exit()

    # Call main function
    main(sys.argv[1], sys.argv[2])
