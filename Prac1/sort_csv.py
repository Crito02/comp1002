import numpy as np
import DSAsorts as sort


class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name


def read_ids_to_array2(filename):
    """
    read ids from file and return as numpy array
    """
    try:
        with open(filename, "r") as f:
            # read student id and name into numpy array of Student objects
            students = np.genfromtxt(f, delimiter=",", dtype=[("Student.id", int), ("Student.name", "U20")])
    except Exception as e:
        print("Error: ", e)
    return students

def read_ids_to_array(filename):
    try:
        with open(filename, "r") as f:
            students = []
            for line in f:
                id, name = line.split(",")
                students.append(Student(id, name))
    except Exception as e:
        print("Error: ", e)

    ids_array = np.zeros(len(students))
    for i in range(len(ids_array)):
        ids_array[i] = students[i].id
    return ids_array


def save_names(students):
    try:
        with open("output.csv", "w") as f:
            for i in range(len(students)):
                f.write(str(students[i])+"\n")
    except Exception as e:
        print("Error ", e)


def main():
    ids = read_ids_to_array2("RandomNames7000(2).csv")
    # sorted = sort.selectionSort(ids)
    # for i in range(len(sorted)-1):
    #     if sorted[i] > sorted[i+1]:
    #         raise Exception("you broke it")
    # save_names(sorted)
    print(type(ids[0]))


if __name__ == "__main__":
    main()
