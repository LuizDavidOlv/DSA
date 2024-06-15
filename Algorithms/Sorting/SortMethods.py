from SelectionSort.Example1 import SelectionSort

class SortMethods:
    def __init__ (self, unsortedList: list[int]):
        self.unsortedList = unsortedList
    
    def selectionSort(self) -> list[int]:
        sortedList = SelectionSort.sort(self.unsortedList)
        return sortedList
    
    def bubbleSort(self):
        return 'Method not implemented yet'

    def insertionSort(self):
        return 'Method not implemented yet'

    def mergeSort(self):
        return 'Method not implemented yet'

    def quickSort(self):
        return 'Method not implemented yet'

    def heapSort(self):
        return 'Method not implemented yet'

    def radixSort(self):
        return 'Method not implemented yet'


if __name__ == '__main__':
    clear_terminal = "\033[H\033[J"
    print(clear_terminal)
    unsortedList = [64,25,12,22,11]
    SortMethod = SortMethods(unsortedList)
    sortedList = SortMethod.selectionSort()
    print("Sorted List")
    print(sortedList)
    print('\n')