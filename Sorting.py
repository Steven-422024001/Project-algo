class Sorting:
    def insertion_sort(self, arr):
        """
        Implementation of Insertion Sort algorithm.
        :param arr: List of elements to be sorted
        :return: Sorted list
        """
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def selection_sort(self, arr):
        """
        Implementation of Selection Sort algorithm.
        :param arr: List of elements to be sorted
        :return: Sorted list
        """
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
