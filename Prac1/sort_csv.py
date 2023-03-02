import sys

import DSAsorts

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name


def read_names(filename):
    try:
        # Open a file
        f = open(filename, "r")

        # Read the file
        students = []
        for line in f:
            line = line.strip()
            parts = line.split(",")
            students.append(Student(parts[0], parts[1]))
    
    except Exception as e:
        print("Error: ", e)
    f.close()

    for s in students:
        print(s.id, s.name)
    return students

def main():
    students = read_names(sys.argv[1])
    bubble_sorted = DSAsorts.bubbleSort(students)
