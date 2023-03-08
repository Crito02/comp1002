import argparse
from concurrent.futures import ThreadPoolExecutor
from SortCSV import read_ids_to_array_no_list, save_to_file
from DSAsorts import bubbleSortStudentObject,\
                     insertionSortStudentObject,\
                     selectionSortStudentObject

def main(filename):
    # Read objects from file
    ids = read_ids_to_array_no_list(filename)

    # Sort using ids
    with ThreadPoolExecutor(max_workers=3) as executor:
        bubble_sort = executor.submit(bubbleSortStudentObject, ids)
        insertion_sort = executor.submit(insertionSortStudentObject, ids)
        selection_sort = executor.submit(selectionSortStudentObject, ids)

    # save sorted ids to file
    save_to_file(bubble_sort.result(), "bubble_sort.csv")
    save_to_file(insertion_sort.result(), "insertion_sort.csv")
    save_to_file(selection_sort.result(), "selection_sort.csv")


if __name__ == "__main__":
    # Filename from command line
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help="The file to read from")
    args = parser.parse_args()
    main(args.filename)
