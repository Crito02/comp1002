import sys
import argparse
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


def main(input_filename, output_filename, sort_type):
    # Read ids from file
    ids = read_ids_to_array_no_list(input_filename)

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
            print("Error: Sort failed")
            sys.exit(1)

    # Save sorted ids to file
    save_to_file(ids, output_filename)


if __name__ == "__main__":
    # Take filename and sort type from command line
    parser = argparse.ArgumentParser()
    parser.add_argument("-f",
                        "--input_filename",
                        help="name of file to read")
    parser.add_argument("-o",
                        "--output_filename",
                        help="name of file to write sorted CSV to",
                        default="output.csv")
    parser.add_argument("-s",
                        "--sort_type",
                        help="type of sort to use",
                        choices=["bubble", "insertion", "selection"])
    args = parser.parse_args()

    # Call main function
    main(args.input_filename, args.output_filename, args.sort_type)
